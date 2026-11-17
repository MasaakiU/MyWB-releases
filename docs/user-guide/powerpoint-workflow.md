# Use MyWB with PowerPoint

[← How to use MyWB](../user-guide.md)

Copy MyWB figures to PowerPoint while retaining the data needed to reopen them later in MyWB. Recoverable MyWB figures can also be restored from a PowerPoint presentation.

## Before you start

See **[Create a figure from a blot](from-blot-to-figure.md)** for the complete figure workflow. A saved `.gel.svg` file is not required when you use **Copy SVG for PowerPoint** and paste the figure. Save the figure first only when you use the **File** method below to insert or drag the `.gel.svg` file into PowerPoint.

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
          <li><a href="manage-mywb-files.md#common-mywb-file-operations">Save the figure as a <code>.gel.svg</code> file</a>.</li>
          <li>In PowerPoint, use <b>Insert &gt; Pictures</b>, or drag the <code>.gel.svg</code> file onto a slide.</li>
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
      <td rowspan="3" valign="top"><b>Open the figures in a PowerPoint file</b><br><a href="premium-access.md"><img src="../assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle"></a></td>
      <td valign="top"><b>Files panel</b></td>
      <td>
        <ol>
          <li>In the <b>Files</b> panel on the right side of the window, click a <code>.pptx</code> file to list the MyWB figures in it.</li>
          <li>Click a figure, or a panel of a figure of several panels.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td valign="top"><b>Menu</b></td>
      <td>
        <ol>
          <li>Select <b>File &gt; Open MyWB File</b> (<kbd>Command+O</kbd> on macOS or <kbd>Ctrl+O</kbd> on Windows).</li>
          <li>Choose a <code>.pptx</code> file. MyWB shows its folder, lists its figures, and opens the first one.</li>
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


### Save figures opened from a PowerPoint file

The **Files** panel lists a `.pptx` file like a folder. Open it to see the MyWB figures it holds, named by slide. A figure of several panels lists its panels, and its assemblies, under it. Selecting one of its panels shows the whole figure in the Assembly View.

MyWB never changes the `.pptx` file. A figure you open and leave unedited needs no saving. A figure you edit is marked with `*`: use **Save As** to save it as a `.gel.svg` file, beside the presentation by default. To update the slide, copy the saved figure with **Copy SVG for PowerPoint** and paste it into PowerPoint again.

## Troubleshooting

### A figure cannot be restored

A figure can be restored only while PowerPoint keeps it as an SVG with its MyWB data intact. Clipboard behavior is controlled by PowerPoint, so compatibility with future PowerPoint versions cannot be guaranteed. The figure may no longer be recoverable if it has been:

- converted to another image format,
- converted to PowerPoint shapes or flattened with other slide content, or
- processed by software that removes embedded metadata.

See [Premium Access](premium-access.md) if MyWB detects a recoverable figure but the Premium operation is unavailable.

### A figure is too large to copy

**Copy SVG for PowerPoint** can copy up to 256 MiB. Every copy carries the figure's source images, so that it can be reopened in MyWB with its pixels. If a figure exceeds this limit, MyWB says it is too large and copies nothing. Reduce the output image size, or save it as a MyWB File instead.

### PowerPoint becomes slow after pasting a figure

Every copy carries the figure's source image data, so that the figure can always be reopened in MyWB with its pixels, and this data increases the PowerPoint file size. MyWB has no setting to leave it out.

## Continue with

- [Save a restored figure](manage-mywb-files.md#common-mywb-file-operations)
- [Adjust marker and blot images](adjust-images.md)
- [Adjust the figure layout and style](design-and-preview-figure.md)
