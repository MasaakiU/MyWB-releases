# MyWB App

MyWB is an end-to-end desktop app for processing and analyzing western blot images (and other gel images, too).

### Do any of these challenges sound familiar?

<p align="center"><img src="docs/assets/challenges-comic.webp" alt="Common challenges in western blot figure preparation" width="600"></p>

Leave the back-and-forth behind. MyWB unites everything from source images to analysis and presentation in one seamless workflow, where you can align, rotate, tune intensity, crop, label, quantify, and export. It also lays the groundwork for easier figure traceability in PowerPoint.

<p align="center"><strong>Download the latest version</strong></p>

<p align="center">
  <a href="https://download.mybioapps.com/mywb/download/latest/macos/arm64"><img src="docs/assets/download-macos-arm64.svg" alt="Download the latest version of MyWB for Apple silicon Macs (arm64)" height="68"></a>
  <a href="https://download.mybioapps.com/mywb/download/latest/macos/x86_64"><img src="docs/assets/download-macos-x86_64.svg" alt="Download the latest version of MyWB for Intel Macs (x86_64)" height="68"></a>
  <a href="https://download.mybioapps.com/mywb/download/latest/windows/x86_64"><img src="docs/assets/download-windows-x86_64.svg" alt="Download the latest version of MyWB for Windows x86_64" height="68"></a>
</p>

<p align="center">
  <a href="https://github.com/MasaakiU/MyWB-releases/releases">Release notes and previous versions</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="docs/installation.md#system-requirements">System requirements</a>
</p>

## Contents

- [Features](#features)
- [System requirements](docs/installation.md#system-requirements)
- [Installation](docs/installation.md)
- [User Guide](docs/user-guide.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Legal and Privacy](#legal-and-privacy)

## Features

### Four Controls, One Workflow

From image preparation to analysis and presentation, every step stays within easy reach.

<table>
  <thead>
    <tr>
      <th align="left">Button</th>
      <th align="left">What it does</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="middle" nowrap="nowrap">
        <a href="docs/user-guide.md#from-blot-to-figure" aria-label="Marker/blot view"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/table-columns-solid_gray20.svg"><img src="docs/assets/table-columns-solid.svg" alt="" width="28" height="28" align="middle"></picture></a>&nbsp;<a href="docs/user-guide.md#from-blot-to-figure"><strong>Marker/blot&nbsp;view</strong></a>
      </td>
      <td valign="middle">Adjust marker and blot images, select an ROI, and add labels.</td>
    </tr>
    <tr>
      <td valign="middle" nowrap="nowrap">
        <a href="docs/user-guide.md#from-blot-to-figure" aria-label="SVG preview"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/eye-solid_gray20.svg"><img src="docs/assets/eye-solid.svg" alt="" width="28" height="28" align="middle"></picture></a>&nbsp;<a href="docs/user-guide.md#from-blot-to-figure"><strong>SVG&nbsp;preview</strong></a>
      </td>
      <td valign="middle">Review the SVG output and edit its styles before saving.</td>
    </tr>
    <tr>
      <td valign="middle" nowrap="nowrap">
        <a href="docs/user-guide.md#quantification-access" aria-label="Quantification"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/square-minus-regular_WB_gray20.svg"><img src="docs/assets/square-minus-regular_WB.svg" alt="" width="28" height="28" align="middle"></picture></a>&nbsp;<a href="docs/user-guide.md#quantification-access"><strong>Quantification</strong></a>
      </td>
      <td valign="middle">Analyze lanes in the selected ROI (Premium feature).</td>
    </tr>
    <tr>
      <td valign="middle" nowrap="nowrap">
        <a href="docs/user-guide.md#powerpoint-workflow" aria-label="Copy SVG for PowerPoint"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/copy_to_powerpoint_gray20.svg"><img src="docs/assets/copy_to_powerpoint.svg" alt="" width="28" height="28" align="middle"></picture></a>&nbsp;<a href="docs/user-guide.md#powerpoint-workflow"><strong>Copy&nbsp;for&nbsp;PowerPoint</strong></a>&nbsp;&nbsp;
      </td>
      <td valign="middle">More than a simple image copy—preserve MyWB metadata for future traceability.</td>
    </tr>
  </tbody>
</table>

### Flexible output layouts

Choose from a variety of sample-label layouts—with more to come!

<p align="center"><img src="docs/assets/sample_label_layout_basic.svg" alt="Basic sample-label layout" width="510"></p>

<p align="center"><img src="docs/assets/sample_label_layout_rotated.svg" alt="Rotated sample-label layout" width="510"></p>

<p align="center"><img src="docs/assets/sample_label_layout_table_per_lane.svg" alt="Table sample-label layout with per-lane labels" width="510"></p>

<p align="center"><img src="docs/assets/sample_label_layout_table_line_span.svg" alt="Table sample-label layout with line spans" width="510"></p>

<p align="center"><img src="docs/assets/sample_label_layout_table_bracket_span.svg" alt="Table sample-label layout with bracket spans" width="510"></p>

## Legal and Privacy

- See [`LICENSE`](LICENSE) for the MyWB license.
- See the [MyWB Privacy Policy](docs/legal/privacy-policy.md).
- See the [macOS third-party software notices](docs/legal/THIRD_PARTY_NOTICES.txt).
- For macOS, see the Qt/PySide6 [corresponding-source offer](docs/legal/third_party/qt/SOURCE-CODE-OFFER.txt)
  and [replacement and re-signing instructions](docs/legal/third_party/qt/RELINKING-INSTRUCTIONS.txt)
  for exercising the rights provided by their LGPL terms.
- Windows-specific notices and legal materials are included with the Windows application and are available through **Help > About > Legal Information**.
