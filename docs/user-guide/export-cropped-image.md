# Export a cropped image

[← How to use MyWB](../user-guide.md)

Export the selected ROI either without min/max contrast remapping or with the [current contrast adjustment](adjust-images.md#contrast) applied.

## Before you start

1. [Open at least one original Marker or Blot image](open-images.md).
2. [Select an ROI](edit-roi-and-labels.md#roi-management). **Export Cropped Area** is unavailable when no ROI exists.

## Steps

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

The folder contains the available Marker and Blot crops and, when possible, an [editable `.mywb.svg` snapshot](manage-mywb-files.md#common-mywb-file-operations) of the exported state.

## Continue with

- [Adjust images and export again](adjust-images.md)
- [Save the main editable MyWB file](manage-mywb-files.md#common-mywb-file-operations)
- [Quantify the same ROI](quantify-bands.md) <a href="premium-access.md"><img src="../assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a>
