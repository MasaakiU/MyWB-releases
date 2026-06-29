# MyWB Standalone App

MyWB is a desktop app for western blot image alignment, labeling, SVG export, and quantification.

## How to Start

### macOS

Open `MyWB.app`.

If macOS blocks the app the first time you open it:

1. Right-click `MyWB.app`.
2. Choose `Open`.
3. Confirm that you want to open the app.

If the app is still blocked:

1. Open `System Settings`.
2. Go to `Privacy & Security`.
3. Scroll down to the `Security` section.
4. Look for a message saying that `MyWB.app` was blocked.
5. Click `Open Anyway`.
6. Enter your Mac password or use Touch ID if asked.
7. Try opening `MyWB.app` again.

## Basic Workflow

1. Open a blot image and, if needed, a marker image.
2. Adjust contrast, inversion, flipping, rotation, and the ROI.
3. Add marker and sample labels.
4. Save the session as a MyWB SVG file.
   - The MyWB SVG file can be placed into PowerPoint or edited in tools such as Inkscape.
   - Open the MyWB SVG file again in MyWB to resume the session.
5. Export cropped images or run quantification when needed.

## Files Created by MyWB

- `.mywb.svg`: Main MyWB save file. It stores image data, labels, ROI, display settings, and metadata.
- Cropped image exports: ROI image exports, either original-intensity or contrast-adjusted.
- Quantification outputs: Result files and snapshot SVGs created from the quantification dialog.

## Notes

- MyWB preserves 8-bit and 16-bit image handling where possible.
- The output bit depth setting affects image data embedded in MyWB SVG files.
- Crop export follows the format selected in the export menu.
- Table-style sample labels should be edited from the `Label: table` button.
- Editing table-label text directly will convert table labels back to basic labels.

## License

See `LICENSE.txt` for the MyWB license.
See `THIRD_PARTY_NOTICES.txt` for third-party software notices.

## Troubleshooting

### The app does not open

On macOS, try right-click > `Open` for the first launch.
If needed, check `System Settings` > `Privacy & Security`.

### The app cannot access files

Make sure the app has permission to access the folder containing your images or output files.
On macOS, folder access can be managed in `System Settings` > `Privacy & Security`.
