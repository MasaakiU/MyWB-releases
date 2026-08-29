# Use MyWB with PowerPoint

[← How to use MyWB](../user-guide.md)

Copy MyWB figures to PowerPoint while retaining the data needed to reopen them later in MyWB. Recoverable MyWB figures can also be restored from a PowerPoint presentation.

## Before you start

See **[Create a figure from a blot](from-blot-to-figure.md)** for the complete figure workflow. A saved `.mywb.svg` file is not required when you use **Copy SVG for PowerPoint** and paste the figure. Save the figure first only when you use the **File** method below to insert or drag the `.mywb.svg` file into PowerPoint.

## PowerPoint workflow

<table>
  <thead>
    <tr>
      <th>Task</th>
      <th>Type</th>
      <th>Method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4" valign="top"><b>Send a figure to PowerPoint</b></td>
      <td valign="top"><b>Click</b></td>
      <td>
        <ol>
          <li>Click <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/copy_to_powerpoint_gray20.svg"><img src="../assets/copy_to_powerpoint.svg" alt="" width="18" height="18" align="absmiddle"></picture> <b>Copy SVG for PowerPoint</b> at the bottom of the left sidebar.</li>
          <li>When MyWB displays <code>Copied. Paste it into PowerPoint.</code>, switch to PowerPoint.</li>
          <li>Paste the figure onto the slide.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>Menu</b></td>
      <td>
        <ol>
          <li>Select <b>Edit &gt; Copy SVG for PowerPoint</b>.</li>
          <li>In PowerPoint, paste the figure onto the slide.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>Keyboard</b></td>
      <td>
        <ol>
          <li>Press <kbd>Command+Shift+C</kbd> on macOS or <kbd>Ctrl+Shift+C</kbd> on Windows.</li>
          <li>In PowerPoint, paste the figure onto the slide.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>File</b></td>
      <td>
        <ol>
          <li><a href="manage-mywb-files.md#common-mywb-file-operations">Save the figure as a <code>.mywb.svg</code> file</a>.</li>
          <li>In PowerPoint, use <b>Insert &gt; Pictures</b>, or drag the <code>.mywb.svg</code> file onto a slide.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td rowspan="2" valign="top"><b>Restore one figure from PowerPoint</b><br><a href="premium-access.md"><img src="../assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a></td>
      <td valign="top"><b>Menu</b></td>
      <td>
        <ol>
          <li>In PowerPoint, select a MyWB SVG figure and copy it.</li>
          <li>In MyWB, select <b>Edit &gt; Paste MyWB from PowerPoint</b>.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>Keyboard</b></td>
      <td>
        <ol>
          <li>In PowerPoint, select a MyWB SVG figure and copy it.</li>
          <li>In MyWB, press <kbd>Command+Shift+V</kbd> on macOS or <kbd>Ctrl+Shift+V</kbd> on Windows.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td rowspan="3" valign="top"><b>Import all recoverable figures from a PowerPoint file</b><br><a href="premium-access.md"><img src="../assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a></td>
      <td valign="top"><b>Menu</b></td>
      <td>
        <ol>
          <li>Select <b>File &gt; Import MyWB from PowerPoint File...</b>.</li>
          <li>Choose a <code>.pptx</code> file.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>Keyboard</b></td>
      <td>
        <ol>
          <li>Press <kbd>Command+I</kbd> on macOS or <kbd>Ctrl+I</kbd> on Windows.</li>
          <li>Choose a <code>.pptx</code> file.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>Drag and drop</b></td>
      <td>
        <ol>
          <li>Drag a <code>.pptx</code> file onto the MyWB window.</li>
        </ol>
      </td>
    </tr>
  </tbody>
</table>


### Save figures imported from a PowerPoint file

When you import a `.pptx` file, MyWB lists each recoverable figure as an editable, unsaved document in the **MyWB Files** panel. The presentation is used only as the source of the recovered figures; editing or saving them does not modify the original `.pptx` file.

When you select **Save**, **Save As**, or **Save All**, MyWB opens the **Save Imported MyWB Files** dialog. Select the figures to save and the destination folder. Each selected figure is saved as a separate `.mywb.svg` file.

> [!CAUTION]
> After saving, MyWB leaves the PowerPoint workspace and opens the folder containing the saved `.mywb.svg` files. Unchecked figures are not saved, and edits to them are discarded. MyWB asks for confirmation before discarding edited unchecked figures.

## Troubleshooting

### A figure cannot be restored

A figure can be restored only while PowerPoint keeps it as an SVG with its MyWB data intact. Clipboard behavior is controlled by PowerPoint, so compatibility with future PowerPoint versions cannot be guaranteed. The figure may no longer be recoverable if it has been:

- converted to another image format,
- converted to PowerPoint shapes or flattened with other slide content, or
- processed by software that removes embedded metadata.

See [Premium Access](premium-access.md) if MyWB detects a recoverable figure but the Premium operation is unavailable.

### A figure is too large to copy

**Copy SVG for PowerPoint** can copy up to 256 MiB. If a figure exceeds this limit, MyWB offers **Copy Without Source Images**, which applies only to that copy. See [PowerPoint Copy settings](settings.md#powerpoint-copy-settings) for details and editing limitations.

### PowerPoint becomes slow after pasting a figure

Source image data can increase the PowerPoint file size. If PowerPoint becomes slow after pasting a figure, go to **Settings > PowerPoint > Copy** and turn off **Include source image data in PowerPoint copies**. See [PowerPoint Copy settings](settings.md#powerpoint-copy-settings) for details and editing limitations.

## Continue with

- [Save a restored figure](manage-mywb-files.md#common-mywb-file-operations)
- [Adjust marker and blot images](adjust-images.md)
- [Adjust the figure layout and style](design-and-preview-figure.md)
