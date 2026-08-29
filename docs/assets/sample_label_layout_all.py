# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_animated_svg.py

複数の SVG ファイルを「パラパラ漫画」のように切り替えるアニメーション SVG を
1 枚生成するスクリプト。

特徴
  * ベクターのまま : 各 SVG の中身をそのまま <g> として取り込むので、
                     ラスタ化も base64 埋め込みもしない（拡大しても綺麗）。
  * GitHub で動く  : <script> も外部参照も使わず、内部 <style> の
                     CSS @keyframes だけでフレームを切り替えるので、
                     README に貼った <img> 経由でもアニメーションする。
  * ID 衝突を自動回避 : 取り込む SVG ごとに id / class / @keyframes 名を
                     リネームし、url(#...) や href="#..." の参照も追随させる。
  * コマンドライン引数なし : 設定はすべて main() の先頭にある。

使い方
    main() 冒頭の設定を書き換えて
        python make_animated_svg.py

GitHub に貼るときの注意
  * README には  ![demo](docs/animation.svg)  や
    <img src="docs/animation.svg" width="480">  のように画像として貼る。
    Markdown に SVG のタグを直書きするとサニタイズで消えるので不可。
  * <img> 経由の SVG では外部リソースが読み込まれない。Web フォント指定や
    外部画像への参照が元の SVG に入っていると、そこだけ表示が崩れる。
    文字はパス化しておくか、汎用フォント（sans-serif など）にしておくと安全。
  * <foreignObject> の中身もレンダリングされないことがある。

依存ライブラリ: なし（標準ライブラリのみ / Python 3.8+）
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

# --------------------------------------------------------------------------
# 名前空間
# --------------------------------------------------------------------------
SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
INKSCAPE_NS = "http://www.inkscape.org/namespaces/inkscape"
SODIPODI_NS = "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK_NS)

# 生成する SVG 側で使うクラス名の接頭辞（取り込んだ SVG 側と衝突しない名前）
OWN_PREFIX = "asvg-"


# --------------------------------------------------------------------------
# 小物ユーティリティ
# --------------------------------------------------------------------------
_LENGTH_RE = re.compile(r"^\s*([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*([a-zA-Z%]*)\s*$")
_UNIT_TO_PX = {
    "": 1.0, "px": 1.0, "pt": 96.0 / 72.0, "pc": 16.0,
    "in": 96.0, "cm": 96.0 / 2.54, "mm": 96.0 / 25.4, "q": 96.0 / 101.6,
}
_URL_REF_RE = re.compile(r"url\(\s*(['\"]?)#([^)'\"\s]+)\1\s*\)")
_CSS_ID_RE = re.compile(r"#(-?[A-Za-z_][\w\-]*)")
_CSS_CLASS_RE = re.compile(r"\.(-?[A-Za-z_][\w\-]*)")
_CSS_KEYFRAMES_RE = re.compile(r"@(-webkit-)?keyframes\s+(-?[A-Za-z_][\w\-]*)")


def _num(value: float) -> str:
    """数値を短い文字列にする（1.0 -> '1'）。"""
    text = f"{value:.4f}".rstrip("0").rstrip(".")
    return text if text not in ("", "-") else "0"


def _parse_length(value: Optional[str]) -> Optional[float]:
    """'100', '100px', '10mm' などを px 換算で返す。'%' や不明値は None。"""
    if not value:
        return None
    m = _LENGTH_RE.match(value)
    if not m:
        return None
    number, unit = m.group(1), m.group(2).lower()
    if unit not in _UNIT_TO_PX:
        return None
    return float(number) * _UNIT_TO_PX[unit]


def _geometry(root: ET.Element,
              fallback: Tuple[float, float] = (300.0, 150.0)
              ) -> Tuple[float, float, List[float]]:
    """<svg> ルートから (幅px, 高さpx, viewBox4値) を推定する。"""
    view_box: Optional[List[float]] = None
    raw_vb = root.get("viewBox")
    if raw_vb:
        parts = [p for p in re.split(r"[\s,]+", raw_vb.strip()) if p]
        if len(parts) == 4:
            try:
                view_box = [float(p) for p in parts]
            except ValueError:
                view_box = None

    width = _parse_length(root.get("width"))
    height = _parse_length(root.get("height"))

    if view_box is not None:
        if width is None:
            width = view_box[2]
        if height is None:
            height = view_box[3]
    else:
        if width is None:
            width = fallback[0]
        if height is None:
            height = fallback[1]
        view_box = [0.0, 0.0, width, height]

    return width, height, view_box


def _parent_map(root: ET.Element) -> dict:
    return {child: parent for parent in root.iter() for child in parent}


def _strip_editor_junk(root: ET.Element) -> None:
    """Inkscape 等が残すメタデータを削って出力を軽くする（見た目には影響しない）。"""
    parents = _parent_map(root)
    doomed = []
    for el in root.iter():
        tag = el.tag
        if tag in (f"{{{SVG_NS}}}metadata", f"{{{SODIPODI_NS}}}namedview"):
            doomed.append(el)
    for el in doomed:
        parent = parents.get(el)
        if parent is not None:
            parent.remove(el)
    for el in root.iter():
        for key in list(el.attrib):
            if key.startswith(f"{{{INKSCAPE_NS}}}") or key.startswith(f"{{{SODIPODI_NS}}}"):
                del el.attrib[key]


# --------------------------------------------------------------------------
# id / class / @keyframes 名のリネーム（フレーム間の衝突回避）
# --------------------------------------------------------------------------
def _namespace_identifiers(root: ET.Element, prefix: str) -> None:
    """root 以下の id・class・@keyframes 名に prefix を付け、参照も書き換える。"""
    ids: set = set()
    classes: set = set()
    keyframes: set = set()
    style_elements: List[ET.Element] = []

    for el in root.iter():
        el_id = el.get("id")
        if el_id:
            ids.add(el_id)
        el_class = el.get("class")
        if el_class:
            classes.update(el_class.split())
        if el.tag == f"{{{SVG_NS}}}style":
            style_elements.append(el)

    for style in style_elements:
        text = style.text or ""
        classes.update(m.group(1) for m in _CSS_CLASS_RE.finditer(text))
        keyframes.update(m.group(2) for m in _CSS_KEYFRAMES_RE.finditer(text))

    if not (ids or classes or keyframes):
        return

    def new_id(name: str) -> str:
        return prefix + name if name in ids else name

    def new_class(name: str) -> str:
        return prefix + name if name in classes else name

    href_keys = ("href", f"{{{XLINK_NS}}}href")

    for el in root.iter():
        for key, value in list(el.attrib.items()):
            if key == "id":
                el.set(key, prefix + value)
            elif key == "class":
                el.set(key, " ".join(new_class(t) for t in value.split()))
            elif key in href_keys and value.startswith("#"):
                el.set(key, "#" + new_id(value[1:]))
            elif "url(" in value:
                el.set(key, _URL_REF_RE.sub(
                    lambda m: f"url(#{new_id(m.group(2))})", value))

    for style in style_elements:
        text = style.text or ""
        text = _CSS_ID_RE.sub(lambda m: "#" + new_id(m.group(1)), text)
        text = _CSS_CLASS_RE.sub(lambda m: "." + new_class(m.group(1)), text)
        if keyframes:
            def rename_kf(m: "re.Match") -> str:
                vendor = m.group(1) or ""
                return f"@{vendor}keyframes {prefix + m.group(2)}"
            text = _CSS_KEYFRAMES_RE.sub(rename_kf, text)
            for name in keyframes:
                # animation / animation-name の中の参照も置き換える
                text = re.sub(
                    r"(animation(?:-name)?\s*:[^;{}]*?)\b" + re.escape(name) + r"\b",
                    lambda m: m.group(1) + prefix + name, text)
        style.text = text


# --------------------------------------------------------------------------
# 1 フレーム分の <g> を作る
# --------------------------------------------------------------------------
def _build_frame(path: Path,
                 index: int,
                 canvas_w: float,
                 canvas_h: float,
                 fit_mode: str,
                 strip_metadata: bool) -> Tuple[ET.Element, float, float]:
    """SVG ファイルを読み、キャンバス上に配置した <g> 要素を返す。"""
    root = ET.parse(str(path)).getroot()
    if root.tag != f"{{{SVG_NS}}}svg":
        raise ValueError(f"{path}: ルート要素が <svg> ではありません（{root.tag}）")

    if strip_metadata:
        _strip_editor_junk(root)

    width, height, view_box = _geometry(root)
    _namespace_identifiers(root, f"f{index}_")

    # 元の <svg> を「入れ子の <svg>」に作り替える。
    # 入れ子 svg は独自のビューポートを持つので、座標系が混ざらない。
    nested = ET.Element(f"{{{SVG_NS}}}svg")
    skip = {"width", "height", "viewBox", "x", "y", "preserveAspectRatio",
            "version", "id", "{http://www.w3.org/XML/1998/namespace}space"}
    for key, value in root.attrib.items():
        if key in skip:
            continue
        nested.set(key, value)

    nested.set("viewBox", " ".join(_num(v) for v in view_box))

    if fit_mode == "none":            # 等倍のまま中央配置
        nested.set("x", _num((canvas_w - width) / 2.0))
        nested.set("y", _num((canvas_h - height) / 2.0))
        nested.set("width", _num(width))
        nested.set("height", _num(height))
        par = root.get("preserveAspectRatio")
        if par:
            nested.set("preserveAspectRatio", par)
    else:                             # キャンバス全体に合わせる
        nested.set("x", "0")
        nested.set("y", "0")
        nested.set("width", _num(canvas_w))
        nested.set("height", _num(canvas_h))
        nested.set("preserveAspectRatio",
                   "none" if fit_mode == "stretch" else "xMidYMid meet")

    for child in list(root):
        nested.append(child)

    group = ET.Element(f"{{{SVG_NS}}}g")
    group.set("class", f"{OWN_PREFIX}frame {OWN_PREFIX}f{index}")
    # CSS アニメを解釈しないレンダラ（Inkscape での書き出し等）では
    # 1 枚目だけが見える静止画になるようにしておく。
    group.set("opacity", "1" if index == 0 else "0")
    group.append(nested)
    return group, width, height


# --------------------------------------------------------------------------
# CSS / SMIL の組み立て
# --------------------------------------------------------------------------
def _build_css(durations: Sequence[float], loop: int) -> str:
    total = sum(durations)
    finite = loop > 0
    lines = [
        f".{OWN_PREFIX}frame{{"
        f"animation-duration:{_num(total)}s;"
        f"animation-iteration-count:{loop if finite else 'infinite'};"
        f"animation-timing-function:step-end;"
        f"animation-fill-mode:{'forwards' if finite else 'none'};"
        f"animation-delay:0s}}"
    ]
    elapsed = 0.0
    for i, dur in enumerate(durations):
        start_pct = elapsed / total * 100.0
        elapsed += dur
        end_pct = elapsed / total * 100.0
        is_last = i == len(durations) - 1

        stops: List[Tuple[float, int]] = []
        if i == 0:
            stops.append((0.0, 1))
        else:
            stops.append((0.0, 0))
            stops.append((start_pct, 1))
        # 有限ループのときは最後のフレームを消さずに残す（fill-mode: forwards 用）
        if not (finite and is_last):
            stops.append((min(end_pct, 100.0), 0))
        # 0% と 100% は必ず明示する。省略するとブラウザが要素の元の値から
        # 暗黙のキーフレームを補ってしまい、末尾で先頭コマが再表示される。
        if stops[-1][0] < 100.0:
            stops.append((100.0, stops[-1][1]))

        body = "".join(f"{_num(p)}%{{opacity:{v}}}" for p, v in stops)
        lines.append(f".{OWN_PREFIX}f{i}{{animation-name:{OWN_PREFIX}kf{i}}}")
        lines.append(f"@keyframes {OWN_PREFIX}kf{i}{{{body}}}")
    return "\n".join(lines)


def _attach_smil(groups: Sequence[ET.Element],
                 durations: Sequence[float],
                 loop: int) -> None:
    """CSS の代わりに SMIL <animate> でフレームを切り替える。"""
    total = sum(durations)
    key_times, elapsed = [0.0], 0.0
    for dur in durations:
        elapsed += dur
        key_times.append(elapsed / total)
    key_times[-1] = 1.0

    for i, group in enumerate(groups):
        values = ["1" if j == i else "0" for j in range(len(durations))]
        values.append(values[0])          # keyTimes の最後(=1.0)に対応させる
        anim = ET.SubElement(group, f"{{{SVG_NS}}}animate")
        anim.set("attributeName", "opacity")
        anim.set("calcMode", "discrete")
        anim.set("values", ";".join(values))
        anim.set("keyTimes", ";".join(_num(t) for t in key_times))
        anim.set("dur", f"{_num(total)}s")
        anim.set("repeatCount", "indefinite" if loop <= 0 else str(loop))
        if loop > 0:
            anim.set("fill", "freeze")


# --------------------------------------------------------------------------
# 本体
# --------------------------------------------------------------------------
def build_animated_svg(svg_files: Sequence,
                       output_path,
                       frame_duration: float = 0.5,
                       durations: Optional[Sequence[float]] = None,
                       loop: int = 0,
                       fit_mode: str = "none",
                       canvas_size: Optional[Tuple[float, float]] = None,
                       padding: float = 0.0,
                       background: Optional[str] = None,
                       animation: str = "css",
                       strip_metadata: bool = True,
                       title: Optional[str] = None) -> Path:
    """SVG ファイル群からアニメーション SVG を 1 枚生成して書き出す。

    svg_files      : 表示順に並べた SVG ファイルのパスのリスト
    output_path    : 出力先 .svg
    frame_duration : 1 フレームあたりの表示秒数（durations 指定時は無視）
    durations      : フレームごとの表示秒数を個別指定するリスト（省略可）
    loop           : 0 なら無限ループ、1 以上ならその回数だけ再生して最後で停止
    fit_mode       : "none"    = 等倍のままキャンバス中央に配置
                     "contain" = 縦横比を保ってキャンバスに収める
                     "stretch" = 縦横比を無視してキャンバスいっぱいに伸ばす
    canvas_size    : (幅, 高さ) を明示指定。None なら全フレームの最大寸法
    padding        : キャンバスの四辺に足す余白 px
    background     : 背景色（"#ffffff" など）。None なら透明
    animation      : "css"（推奨・GitHub 向き）または "smil"
    strip_metadata : Inkscape 等のメタデータを削除するか
    title          : <title> に入れる文字列（アクセシビリティ用、省略可）
    """
    paths = [Path(p) for p in svg_files]
    if not paths:
        raise ValueError("svg_files が空です")
    missing = [str(p) for p in paths if not p.is_file()]
    if missing:
        raise FileNotFoundError("見つからないファイル: " + ", ".join(missing))
    if fit_mode not in ("none", "contain", "stretch"):
        raise ValueError(f"fit_mode が不正です: {fit_mode}")
    if animation not in ("css", "smil"):
        raise ValueError(f"animation が不正です: {animation}")

    if durations is None:
        frame_durations = [float(frame_duration)] * len(paths)
    else:
        if len(durations) != len(paths):
            raise ValueError("durations の長さが svg_files と一致しません")
        frame_durations = [float(d) for d in durations]
    if any(d <= 0 for d in frame_durations):
        raise ValueError("表示秒数は正の数にしてください")

    # --- キャンバスサイズを決める（先に全ファイルの寸法を測る） ---
    sizes = []
    for path in paths:
        root = ET.parse(str(path)).getroot()
        w, h, _ = _geometry(root)
        sizes.append((w, h))
    if canvas_size is not None:
        canvas_w, canvas_h = float(canvas_size[0]), float(canvas_size[1])
    else:
        canvas_w = max(w for w, _ in sizes)
        canvas_h = max(h for _, h in sizes)
    canvas_w += padding * 2
    canvas_h += padding * 2

    # --- 各フレームを組み立てる ---
    groups = []
    for i, path in enumerate(paths):
        group, _, _ = _build_frame(path, i, canvas_w, canvas_h,
                                   fit_mode, strip_metadata)
        groups.append(group)

    if animation == "smil" and len(paths) > 1:
        _attach_smil(groups, frame_durations, loop)

    # --- ドキュメント全体を文字列で組み立てる ---
    out: List[str] = ['<?xml version="1.0" encoding="UTF-8"?>']
    out.append(
        f'<svg xmlns="{SVG_NS}" xmlns:xlink="{XLINK_NS}" version="1.1"'
        f' width="{_num(canvas_w)}" height="{_num(canvas_h)}"'
        f' viewBox="0 0 {_num(canvas_w)} {_num(canvas_h)}">'
    )
    if title:
        out.append(f"  <title>{_escape_text(title)}</title>")
    if animation == "css" and len(paths) > 1:
        css = _build_css(frame_durations, loop)
        out.append("  <style>\n" + _indent(css, "    ") + "\n  </style>")
    if background:
        out.append(f'  <rect width="100%" height="100%" fill="{background}"/>')
    for group in groups:
        fragment = ET.tostring(group, encoding="unicode")
        # ルートの <svg> で宣言済みなので、断片側の重複宣言は削っておく
        fragment = fragment.replace(f' xmlns="{SVG_NS}"', "")
        fragment = fragment.replace(f' xmlns:xlink="{XLINK_NS}"', "")
        out.append(_indent(fragment, "  "))
    out.append("</svg>")
    out.append("")

    destination = Path(output_path)
    if destination.parent and not destination.parent.exists():
        destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(out), encoding="utf-8")
    return destination


def _escape_text(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _indent(text: str, pad: str) -> str:
    return "\n".join(pad + line if line.strip() else line
                     for line in text.split("\n"))


# --------------------------------------------------------------------------
# 設定はここ（コマンドライン引数の代わり）
# --------------------------------------------------------------------------
def main() -> None:
    # ---- 入力：表示したい順に並べる ----------------------------------
    svg_files = [
        "sample_label_layout_basic.svg",
        "sample_label_layout_rotated.svg",
        "sample_label_layout_table_bracket_span.svg",
        "sample_label_layout_table_line_span.svg",
        "sample_label_layout_table_per_lane.svg"
    ]
    # フォルダからまとめて拾いたい場合はこちら（連番ファイル向けの自然順ソート）:
    # svg_files = sorted(
    #     Path("frames").glob("*.svg"),
    #     key=lambda p: [int(s) if s.isdigit() else s.lower()
    #                    for s in re.split(r"(\d+)", p.name)],
    # )

    # ---- 出力 --------------------------------------------------------
    output_path = Path(__file__).with_suffix(".svg")
    # if output_path.exists():
    #     raise SystemExit(f"出力先が既に存在します: {output_path}")

    # ---- アニメーション ----------------------------------------------
    frame_duration = 1.3      # 1 コマの表示秒数
    durations = None          # 例: [1.0, 0.3, 0.3] でコマ別に指定（None なら上を使用）
    loop = 0                  # 0 = 無限ループ / 3 = 3 周して最後のコマで停止

    # ---- レイアウト --------------------------------------------------
    fit_mode = "none"         # "none"(等倍・中央) / "contain" / "stretch"
    canvas_size = None        # 例: (800, 600)。None なら全コマの最大寸法に合わせる
    padding = 0.0             # 四辺の余白 px
    background = None         # 例: "#ffffff"。None なら透明のまま

    # ---- その他 ------------------------------------------------------
    animation = "css"         # "css"（推奨・GitHub でも動く）/ "smil"
    strip_metadata = True     # Inkscape 等のメタデータを削って軽くする
    title = None              # 例: "デモアニメーション"（<title> に入る）

    written = build_animated_svg(
        svg_files=svg_files,
        output_path=output_path,
        frame_duration=frame_duration,
        durations=durations,
        loop=loop,
        fit_mode=fit_mode,
        canvas_size=canvas_size,
        padding=padding,
        background=background,
        animation=animation,
        strip_metadata=strip_metadata,
        title=title,
    )
    size_kb = written.stat().st_size / 1024
    print(f"生成しました: {written}  ({len(svg_files)} コマ / {size_kb:.1f} KB)")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError) as exc:
        raise SystemExit(f"エラー: {exc}")