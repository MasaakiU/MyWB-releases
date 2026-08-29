# Settings

[← How to use MyWB](../user-guide.md)

Manage reusable presets and control whether figures copied to PowerPoint include source image data.

## Open Settings

- **macOS:** **MyWB > Settings...**
- **Windows:** **Edit > Settings...**

You can also open the relevant settings directly from:

- The <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/gear-solid_gray20.svg"><img src="../assets/gear-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Settings** button beside **Auto Fill** in the marker or sample label batch editor
- **SVG Preview > SVG Style > ... > Settings...**

## Settings pages

| Page                                              | What it controls                                             |
| ------------------------------------------------- | ------------------------------------------------------------ |
| [**Marker Auto Fill**](#auto-fill-presets)        | A complete list of molecular-weight marker labels            |
| [**Sample Prefix Auto Fill**](#auto-fill-presets) | A prefix for sequential sample labels such as `sample 1`, `sample 2`, ... |
| [**SVG Style**](#svg-style-presets)               | Figure appearance, including margins, fonts, image size, and label positions |
| [**PowerPoint Copy**](#powerpoint-copy-settings)  | Whether copied figures include source image data for later editing |

## Auto Fill presets

Auto Fill presets store reusable marker labels or sample label prefixes.

| Preset                      | Stores                                                       |
| --------------------------- | ------------------------------------------------------------ |
| **Marker Auto Fill**        | A complete list of molecular-weight marker labels            |
| **Sample Prefix Auto Fill** | A prefix for sequential sample labels such as `sample 1`, `sample 2`, ... |

### Use a preset

Click the **Label** button in the **Markers** or **Sample Details** panel to open the label batch editor, then select <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/wand-magic-sparkles-solid_gray20.svg"><img src="../assets/wand-magic-sparkles-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Auto Fill > Fill with "[preset name]"**.

The number of lines cannot exceed the number of existing positions in the corresponding **Markers** or **Sample Details** panel.

### Manage presets

1. Open **Settings > Label Presets > Marker Auto Fill** or **Settings > Label Presets > Sample Prefix Auto Fill**.
2. Make the required changes:
    - **Add:** Select **... > Add Preset...**, enter a name, then edit the preset contents. The new preset starts with the contents of the previously selected preset.
    - **Edit:** Select a preset from the drop-down list, then edit its contents.
    - **Rename:** Select the preset, then select **... > Rename Preset...** and enter a new name.
    - **Delete:** Select the preset, then select **... > Delete Preset...** and confirm with **Delete**.
3. Click **Save Settings** to save all changes.

For **Marker Auto Fill**, enter one molecular-weight value per line. For **Sample Prefix Auto Fill**, enter the prefix used to generate sequential sample labels.

## SVG Style presets

Use style presets to reuse the appearance of a figure, including margins, fonts, image size, marker and label positions, and other SVG settings.

### Apply or save a style in SVG Preview

1. In <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/eye-solid_gray20.svg"><img src="../assets/eye-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **SVG Preview**, open the **SVG Style** tab.
2. Click the `...` menu button.
3. Select an action:
   - Select **Load "[preset name]"** to load the preset you want.
   - Select **Load System Default** to load the system default style.
   - Select **Toggle Previous Style** to return to the previous style.
   - Select **Save Current Style As...** and then enter a new preset name to save the current style as a new preset. To replace an existing preset, select its name and confirm with **Overwrite**.

### Manage style presets in Settings

To add, edit, rename, or delete a preset:

1. Open **Settings > SVG > Style Presets**.
2. Make the required changes:
   - **Add:** Select **... > Add Preset...**, enter a name, then adjust the style options. The new preset starts with the style from the previously selected preset.
   - **Edit:** Select a preset from the drop-down list, then adjust its style options.
   - **Rename:** Select the preset, then select **... > Rename Preset...** and enter a new name.
   - **Delete:** Select the preset, then select **... > Delete Preset...** and confirm with **Delete**.
3. Click **Save Settings** to save all changes.

To reset the selected preset before saving, select **... > Load System Default**.

## PowerPoint Copy settings

By default, MyWB includes available source image pixels and channels in figures copied with **Copy SVG for PowerPoint**. This allows full editing when a figure in a PowerPoint file is reopened in MyWB, but the added source data can make PowerPoint files much larger.

To make future PowerPoint copies smaller:

1. Open **Settings > PowerPoint > Copy**.
2. Uncheck the **Include source image data in PowerPoint copies** checkbox.
3. Click **Save Settings**.
4. Copy and paste the figure again. To reduce the size of an existing presentation, replace the previously pasted copy with the new one.

> [!CAUTION]
> The new copy looks the same in PowerPoint. Annotations, sample labels, markers, blot inversion, and saturated-pixel highlighting remain editable. **However, when the figure is reopened in MyWB from PowerPoint, the full MyWB editing state may not be recoverable**. Geometry, contrast, channel selection, quantification, and original-intensity image export are unavailable.

This setting affects only future PowerPoint copies. It does not change figures already in PowerPoint or saved `.mywb.svg` files.

## Continue with

- [Add, change, or remove molecular-weight marker labels](edit-roi-and-labels.md#add-marker-and-sample-positions)
- [Add, change, or remove sample labels](edit-roi-and-labels.md#add-marker-and-sample-positions)
- [Adjust fonts, spacing, margins, and image size](design-and-preview-figure.md#edit-svg-style)
