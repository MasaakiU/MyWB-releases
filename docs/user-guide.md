# How to use MyWB

[← Back to MyWB](../README.md)

[Window overview](user-guide/window-overview.md) — find the names, locations, and roles of the main parts of the window.

## Common workflows

- **[Create a figure from a blot](user-guide/from-blot-to-figure.md)** — open the blot image and an optional marker image, select the figure area, add labels, preview, and save the result.
- **[Quantify bands](user-guide/quantify-bands.md)** <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a> — select an ROI, check lane boundaries, and copy or export the measurements.
- **[Manage MyWB files](user-guide/manage-mywb-files.md#common-mywb-file-operations)** — reopen a `.gel.svg` file with its MyWB data.
- **[Use MyWB with PowerPoint](user-guide/powerpoint-workflow.md#powerpoint-workflow)** — copy figures to PowerPoint and restore them later in MyWB.
  - Copying a figure is a Basic feature; restoring one, by pasting it or by opening the MyWB figures of a `.pptx` file, uses Premium Access. <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
- **[Use MyWB with an AI assistant](user-guide/ai-assistant.md)** <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a> — install the MyWB plugin in Claude Desktop or the ChatGPT desktop app, and let an assistant work in the window you have open.

## Prepare images

- [Open a marker or blot image](user-guide/open-images.md#open-a-marker-or-blot-image)
  - Open images from the image selectors, File menu, keyboard shortcuts, or by drag and drop.
- [Select an RGB channel](user-guide/open-images.md#select-an-rgb-channel)
- [Supported images](user-guide/open-images.md#supported-images)
- [ROI management](user-guide/edit-roi-and-labels.md#roi-management)
  - Create, move, resize, or delete an ROI.
- [Contrast](user-guide/adjust-images.md#contrast)
  - Adjust or reset contrast and change the histogram display.
- [Image controls and export settings](user-guide/adjust-images.md#image-controls-and-export-settings)
  - Check saturated pixels; invert, flip, or rotate images; link matching Marker and Blot controls; and select export bit depth.

## Add labels and design the figure

- [Add marker and sample positions](user-guide/edit-roi-and-labels.md#add-marker-and-sample-positions)
  - Add marker and sample positions, then enter molecular-weight values and sample details.
- [Modify marker or sample positions](user-guide/edit-roi-and-labels.md#modify-marker-or-sample-positions)
  - Move positions individually or together, or align and distribute selected positions.
- [Delete marker or sample positions](user-guide/edit-roi-and-labels.md#delete-marker-or-sample-positions)
- [Preview of the figure](user-guide/design-and-preview-figure.md#preview-of-the-figure)
- [Edit sample labels](user-guide/design-and-preview-figure.md#edit-sample-labels)
  - Choose Basic, Rotated, or table-based layouts and adjust their layout options.
- [Edit SVG style](user-guide/design-and-preview-figure.md#edit-svg-style)
  - Adjust margins, fonts, image size, marker and label positions, the marker unit, band names and ticks, details, and annotations.
- [Find a setting from the preview](user-guide/design-and-preview-figure.md#find-a-setting-from-the-preview)
  - Click a part of the figure to bring up the setting that changes it.

## Fluorescent channels and assemblies

- [Show a fluorescent blot's channels](user-guide/fluorescent-channels.md)
  - Show several channels together as Composite, set their colours and names, choose the reference channel, and detect and quantify each channel.
- [Put panels together as an assembly](user-guide/assemblies.md)
  - Combine MyWB files into one figure, arrange the panels in a grid, line up their lanes, and set how each panel looks.

## Save, export, and reuse

- [Common MyWB file operations](user-guide/manage-mywb-files.md#common-mywb-file-operations)
  - Create, open, save, discard, duplicate, rename, or move MyWB files to Trash.
- [Use the Files panel](user-guide/manage-mywb-files.md#use-the-files-panel)
  - Browse folders, open the panels of a file of several panels, and open the MyWB figures in a PowerPoint file.
- [Add notes to a MyWB file](user-guide/manage-mywb-files.md#add-notes-to-a-mywb-file)
- [Export a cropped image](user-guide/export-cropped-image.md#steps)
- [PowerPoint workflow](user-guide/powerpoint-workflow.md#powerpoint-workflow)
  - Copy a figure to PowerPoint; restore one by pasting it or by opening the `.pptx` file, with Premium Access. <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>

## Bands and quantification

- [Detect bands with Auto Detect](user-guide/detect-bands.md#run-auto-detect) <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
  - Find markers, bands, sample lanes and ROIs, check the result, and place it.
- [Use the band table](user-guide/detect-bands.md#use-the-band-table)
  - Add, move, name and rearrange bands by lane and row.
- [Show and hide marks on the pictures](user-guide/detect-bands.md#show-and-hide-marks-on-the-pictures)
- [Level the picture by the ROI](user-guide/detect-bands.md#level-the-picture-by-the-roi)
- [Quantification steps](user-guide/quantify-bands.md#steps) <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
  - Set the number of lanes; choose automatic, semi-automatic, or full-manual lane detection; invert the signal; adjust background subtraction; and copy or export the results.
  - Result labels show `unknown` when the number of sample positions in the ROI does not match the number of lanes.
- [Keep the results in the document](user-guide/quantify-bands.md#keep-the-results-in-the-document)

## Settings and Premium Access

- [Open Settings](user-guide/settings.md#open-settings)
- [Auto Fill presets](user-guide/settings.md#auto-fill-presets)
  - Reuse marker labels and sample label prefixes.
- [SVG Style presets](user-guide/settings.md#svg-style-presets)
  - Save and reuse figure styles.
- [Install MyWB in an assistant](user-guide/ai-assistant.md#install-extension-or-plugin) <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
  - Claude (chat, Cowork and Claude Code), ChatGPT (Work and Codex, not chat), or any other MCP client.
- [Turn AI assistant access on](user-guide/ai-assistant.md#turn-ai-assistant-access-on) <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
- [Save your usual instructions](user-guide/ai-assistant.md#save-your-usual-instructions) <a href="user-guide/premium-access.md"><img src="assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
  - Notes handed to an assistant when it connects, kept as presets.
- [Undo History settings](user-guide/settings.md#undo-history-settings)
  - How much memory retained undo steps may use.
- [Features that use Premium Access](user-guide/premium-access.md#features-that-use-premium-access)
- [Premium Access verification](user-guide/premium-access.md#verification)

## FAQ and support

- [The app does not open](troubleshooting.md#the-app-does-not-open)
- [The app cannot access files](troubleshooting.md#the-app-cannot-access-files)
- [PowerPoint troubleshooting](user-guide/powerpoint-workflow.md#troubleshooting)
  - Check why a MyWB figure cannot be restored or what to do when a figure is too large to copy.
- [Premium Access is unavailable](user-guide/premium-access.md#if-premium-features-are-unavailable)
- [AI assistant troubleshooting](user-guide/ai-assistant.md#troubleshooting)
- [Install or update MyWB](installation.md)
- [Legal and privacy information](legal-and-privacy.md)
- [Report a bug or ask a question](troubleshooting.md#report-a-bug-or-ask-a-question)
