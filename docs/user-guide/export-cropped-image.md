# Export images

[← How to use MyWB](../user-guide.md)

Choose which image you want to export:

| What you need | Command |
| --- | --- |
| The selected ROI, with the current rotation, flip, and inversion, plus optional contrast adjustment | [**Export Cropped Area**](#export-a-cropped-image) |
| The full source image before MyWB's image adjustments | [**Export Source Image**](#export-a-source-image) |

## Export a cropped image

Export the selected ROI either without min/max contrast remapping or with the [current contrast adjustment](adjust-images.md#contrast) applied.

### Before you start

1. [Open at least one original Marker or Blot image](open-images.md).
2. [Select an ROI](edit-roi-and-labels.md#roi-management). **Export Cropped Area** is unavailable when no ROI exists.

### Steps

1. Select **File > Export Cropped Area**.
2. Choose one output mode:

   - **Original Intensity** exports the current transformed crop without applying min/max contrast remapping.
   - **Contrast Adjusted** applies the current minimum and maximum contrast values.

3. Choose an output format:

   - **16-bit TIFF**
   - **8-bit TIFF**
   - **16-bit PNG**
   - **8-bit PNG**
   - **JPEG**

The 16-bit choices are available only when every original image in the export is 16-bit. See [Supported images](open-images.md#supported-images) for accepted bit depths.

**Output:** MyWB creates a folder beside the source image. Its name ends in `_cropped_area` or `_cropped_area_contrast_adjusted`; if that folder exists, MyWB adds a number instead of overwriting it.

The folder contains the available Marker and Blot crops and, when possible, an [editable `.gel.svg` snapshot](manage-mywb-files.md#common-mywb-file-operations) of the exported state.

## Export a source image

1. Choose **File > Export Source Image > Blot Image...** or **Marker Image...**.
2. If MyWB asks for a format, choose **PNG** or **TIFF**.
3. Choose a location and filename, then save.

Existing files are not overwritten. If the source image data is missing, open the original image file before exporting.

> [!NOTE]
> The export preserves the source pixel values stored in the document, together with the metadata MyWB can write to the output format. It may not be byte-for-byte identical to the original because its encoding or file structure may differ. Some metadata of the original image may be omitted when converting formats.

## Continue with

- [Adjust images and export again](adjust-images.md)
- [Find an original source file](manage-mywb-files.md#find-a-source-image)
- [Save the main editable MyWB file](manage-mywb-files.md#common-mywb-file-operations)
- [Quantify the same ROI](quantify-bands.md) <a href="premium-access.md"><img src="../assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
