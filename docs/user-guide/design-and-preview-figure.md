# Preview, layout, and style of the figure

[← How to use MyWB](../user-guide.md)

Use the live SVG Preview to arrange labels and adjust the figure's appearance.

## Before you start

1. Click <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/table-columns-solid_gray20.svg"><img src="../assets/table-columns-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Marker/blot view** in the left sidebar.
2. [Open a blot image](open-images.md).
3. [Open a marker image](open-images.md) if you want to compare or transform both images.
4. [Adjust marker and blot images](adjust-images.md) if necessary.
5. Add [marker positions](edit-roi-and-labels.md#add-marker-positions) and [sample positions](edit-roi-and-labels.md#add-sample-positions).

## Preview of the figure

Click <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/eye-solid_gray20.svg"><img src="../assets/eye-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **SVG Preview** in the left sidebar to check the live figure preview. It uses the ROI when one exists and the full blot otherwise.

- Sample-label layout and content can be edited on the **Sample Label** tab.
- Figure appearance can be edited on the **SVG Style** tab under **Global**, **Image**, **Markers**, **Labels**, **Details**, and **Annotation**.

<p align="center"><img src="../assets/svg_style_guide_Overview.svg" alt="Generated figure areas for the annotation, sample labels, blot image, molecular-weight markers, and sample details" width="550"></p>

## Edit sample labels

You can select a **Layout** in the **Sample Label** tab when at least one applicable [Sample position](edit-roi-and-labels.md#add-sample-positions) is available. With an ROI, only Sample positions within the ROI's horizontal range are used; without an ROI, all Sample positions are used with the full blot.

<table>
  <tr>
    <td valign="top" width="50%">
      <p align="center"><img src="../assets/sample_label_layout_basic.svg" alt="Basic sample-label layout" width="383"></p>
      <p align="center"><img src="../assets/sample_label_layout_rotated.svg" alt="Rotated sample-label layout" width="383"></p>
    </td>
    <td valign="top" width="50%">
      <p align="center"><img src="../assets/sample_label_layout_table_per_lane.svg" alt="Table sample-label layout with per-lane labels" width="383"></p>
      <p align="center"><img src="../assets/sample_label_layout_table_line_span.svg" alt="Table sample-label layout with line spans" width="383"></p>
      <p align="center"><img src="../assets/sample_label_layout_table_bracket_span.svg" alt="Table sample-label layout with bracket spans" width="383"></p>
    </td>
  </tr>
</table>

### Edit table layout

When you select a table-based layout, the table editing area appears.

- Use the <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/plus-solid_gray20.svg"><img src="../assets/plus-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Add**, <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/arrow-up-solid_gray20.svg"><img src="../assets/arrow-up-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Up**, <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/arrow-down-solid_gray20.svg"><img src="../assets/arrow-down-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Down**, and <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/trash-can-regular_gray20.svg"><img src="../assets/trash-can-regular.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Trash** buttons to add, move, or delete rows.
- Use the <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/align-right-solid_gray20.svg"><img src="../assets/align-right-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Row header alignment** button to cycle row headers through right, center, and left alignment. The icon indicates the current alignment.
- For the **Table (per lane)** layout, the text entered in each table cell is used directly as the label.
- For the **Table (line span)** and **Table (bracket span)** layouts, adjacent cells containing the same text are merged and displayed as a single label.
- Move the **Separator** up or down to place table rows above and below the blot.
- Click the <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/gear-solid_gray20.svg"><img src="../assets/gear-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Settings** button to configure row-specific settings.
- Additional style settings are available as shown below.

<p align="center"><img src="../assets/screen_shots/table-layout_guide.svg" alt="Table layout diagram showing header gap, line inset, line offset, row gap, and row-specific settings" width="450"></p>

Below are several examples of table layouts.

<p align="center"><img src="../assets/screen_shots/table-layout-examples.svg" alt="Sample Label editor examples for per-lane, line-span, and split table layouts" width="917"></p>

### Edit rotated layout

- Enter a value in **Angle** to set the label rotation angle (−90° ≤ Angle ≤ 90°).
- Select **Anchor** to set the reference point for label rotation. The **automatic** option works well in most cases.
- By default, the rotated label uses the same text as **Sample Details**.
- To use a label different from **Sample Details**, enter custom text in the **Rotated label** field.
- Click the <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/link-solid_gray20.svg"><img src="../assets/link-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Link** button to restore the label from **Sample Details**.

<p align="center"><img src="../assets/screen_shots/angle-layout.svg" alt="Rotated sample label" width="700"></p>

### Settings by layout

The table below shows which settings are available for each layout.

| Setting       | Basic         | Rotated       | Table<br />(per lane) | Table<br />(line span) | Table<br />(bracket span) |
| ------------- | ------------- | ------------- | --------------------- | ---------------------- | ------------------------- |
| Position      | ✅️<sup>†</sup> | ✅️<sup>†</sup> | ✅️<sup>‡</sup>         | ✅️<sup>‡</sup>          | ✅️<sup>‡</sup>             |
| Angle         | ❌️             | ✅️             | ✅️<sup>§</sup>         | ✅️<sup>§</sup>          | ✅️<sup>§</sup>             |
| Anchor        | ❌️             | ✅️             | ❌️                     | ❌️                      | ❌️                         |
| Row gap       | ❌️             | ❌️             | ✅️<sup>¶</sup>         | ✅️<sup>¶</sup>          | ✅️<sup>¶</sup>             |
| Header gap    | ❌️             | ❌️             | ✅️                     | ✅️                      | ✅️                         |
| Header side   | ❌️             | ❌️             | ✅️                     | ✅️                      | ✅️                         |
| Header offset | ❌️             | ❌️             | ✅️<sup>§</sup>         | ✅️<sup>§</sup>          | ✅️<sup>§</sup>             |
| Line width    | ❌️             | ❌️             | ❌️                     | ✅️                      | ✅️                         |
| Line inset    | ❌️             | ❌️             | ❌️                     | ✅️                      | ✅️                         |
| Line offset   | ❌️             | ❌️             | ❌️                     | ✅️                      | ❌️                         |
| Hide lines    | ❌️             | ❌️             | ❌️                     | ✅️<sup>§</sup>          | ✅️<sup>§</sup>             |
| Text offset   | ❌️             | ❌️             | ❌️                     | ❌️                      | ✅️                         |

† With **Position** set to **Auto**, sample labels are placed above or below the blot based on the sample positions within the selected figure area.<br>
‡ With **Position** set to **Auto**, table rows can be placed both above and below the blot. See [Edit table layout](#edit-table-layout) for details.<br>
§ These settings appear when you click the gear icon for a row.<br>
¶ This setting is unavailable when there is only one row, or when two rows are split between the top and bottom of the blot.

## Edit SVG style

The following settings can be edited:

- **Global:** margins and font family
- **Image<sup>†</sup>:** pixel width, pixel height, scale (%), and border width
- **Markers<sup>‡</sup>:** position, gap, font size, baseline offset, tick width, and tick length
- **Labels<sup>§</sup>:** position, font size, and gap
- **Details:** visibility, font size, and gap
- **Annotation<sup>¶</sup>:** text, position, font size, gap, and text alignment

† **Pixel width**, **Pixel height**, and **Scale (%)** are linked to one another.<br>
‡ **Position** is linked to **Annotation > Position** and uses the opposite side.<br>
§ **Position** is linked to **Sample Label > Position**.<br>
¶ **Position** is linked to **Markers > Position** and uses the opposite side.

<p align="center"><img src="../assets/screen_shots/svg-style.svg" alt="SVG Style panel showing Global margin and font settings and Image size, scale, and border settings" width="300"></p>

On the **SVG Style** tab, use the **...** menu to select **Load System Default**, **Toggle Previous Style**, or **Save Current Style As...**.

<p align="center"><img src="../assets/svg_style_guide_Global-Image.svg" alt="Figure diagram showing the global margins and image border width" width="550"></p>

<p align="center"><img src="../assets/svg_style_guide_Markers-Labels-Details-Annotation.svg" alt="Figure diagram showing gaps for the annotation, sample labels, markers, and details, plus marker tick and baseline settings" width="550"></p>

## Continue with

- [Save the editable MyWB file](manage-mywb-files.md#common-mywb-file-operations)
- [Copy the figure to PowerPoint](powerpoint-workflow.md#powerpoint-workflow)
- [Adjust marker and blot images](adjust-images.md)
