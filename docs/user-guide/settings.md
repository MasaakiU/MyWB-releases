# Settings

[← How to use MyWB](../user-guide.md)

Manage reusable presets, how much memory undo history may use, and whether an AI assistant may work in the window.

## Open Settings

- **macOS:** **MyWB > Settings...**
- **Windows:** **Edit > Settings...**

You can also open the relevant settings directly from:

- The <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/gear-solid_gray20.svg"><img src="../assets/gear-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Settings** button beside **Auto Fill** in the marker or sample label batch editor
- **SVG Preview > SVG Style > ... > Settings...**

## Settings pages

<table>
  <thead>
    <tr>
      <th scope="col">Category</th>
      <th scope="col">Page</th>
      <th scope="col">What it controls</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="rowgroup" rowspan="2">Label Presets</th>
      <td><a href="#auto-fill-presets"><strong>Marker Auto Fill</strong></a></td>
      <td>A complete list of molecular-weight marker labels</td>
    </tr>
    <tr>
      <td><a href="#auto-fill-presets"><strong>Sample Prefix Auto Fill</strong></a></td>
      <td>A prefix for sequential sample labels such as <code>sample 1</code>, <code>sample 2</code>, ...</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th scope="rowgroup">SVG</th>
      <td><a href="#svg-style-presets"><strong>Style Presets</strong></a></td>
      <td>Figure appearance, including margins, fonts, image size, and label positions</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th scope="rowgroup">Memory</th>
      <td><a href="#undo-history-settings"><strong>Undo History</strong></a></td>
      <td>How much memory retained undo steps may use</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th scope="rowgroup" rowspan="3">Integration</th>
      <td><a href="#ai-assistant-access-settings"><strong>AI Assistant Access</strong></a></td>
      <td>Whether an AI assistant may work in this window, and what it may do without asking</td>
    </tr>
    <tr>
      <td><a href="#assistant-notes"><strong>Assistant Notes</strong></a></td>
      <td>A note in your own words about how you work, handed to an assistant when it connects</td>
    </tr>
    <tr>
      <td><a href="#advanced-integration-settings"><strong>Advanced</strong></a></td>
      <td>The connection details for a client with no MyWB plugin</td>
    </tr>
  </tbody>
</table>

## Auto Fill presets

Auto Fill presets store reusable marker labels or sample label prefixes.

| Preset                      | Stores                                                       |
| --------------------------- | ------------------------------------------------------------ |
| **Marker Auto Fill**        | A complete list of molecular-weight marker labels            |
| **Sample Prefix Auto Fill** | A prefix for sequential sample labels such as `sample 1`, `sample 2`, ... |

### Use a preset

Click the <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/pen-solid_gray20.svg"><img src="../assets/pen-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Edit all marker labels...** button in the **Markers** panel or the <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/pen-solid_gray20.svg"><img src="../assets/pen-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Edit All...** button in the **Sample Lane Details** panel to open the label batch editor, then select <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/wand-magic-sparkles-solid_gray20.svg"><img src="../assets/wand-magic-sparkles-solid.svg" alt="" width="18" height="18" align="absmiddle"></picture> **Auto Fill > Fill with "[preset name]"**.

The number of lines cannot exceed the number of existing positions in the corresponding **Markers** or **Sample Lane Details** panel.

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

## Undo History settings

Undo history is kept per document and is bounded by one memory limit shared across every open document. A step that swaps an image for another exposure keeps a full-resolution image, so a few such steps cost far more than a few label edits.

1. Open **Settings > Memory > Undo History**.
2. Set the limit. The default is 512 MB, and the range is 64 MB to 8192 MB.
3. Click **Save Settings**.

Lowering the limit takes effect immediately: MyWB gives up the steps it can spare — redo steps first, then the oldest undo steps of whichever document holds the most — until the retained history fits. Every open document always keeps at least one undo step, whatever the limit says, so <kbd>Ctrl+Z</kbd> works once on each of them.

## AI Assistant Access settings

These pages control whether an AI assistant running on the same computer may work in the window you have open. Access is a Premium feature and is off by default. Installing MyWB in an assistant, switching access on, and what an assistant can and cannot do are described in [Use MyWB with an AI assistant](ai-assistant.md).

**Settings > Integration > AI Assistant Access** shows what is actually running, can switch access on or off, and lists the operations that cannot be undone — **Overwrite a file**, **Move a file to Trash** and **Discard unsaved work** — so you can answer them in advance with **Never allow**, **Ask each time** or **Allow without asking**. Those answers apply to that one window and are forgotten when MyWB closes or AI assistant access is switched off. See [What the assistant can see and do](ai-assistant.md#what-the-assistant-can-see-and-do).

> The <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/ai_gray20.svg"><img src="../assets/ai.svg" alt="" width="18" height="18" align="absmiddle"></picture> **AI assistant access** button beside **Copy SVG for PowerPoint** switches access at once, and so does the checkbox on this page; **Cancel** puts it back the way it was when Settings opened. The status line here always reports what is actually running.

## Assistant Notes

Save the instructions you would otherwise give an assistant in every conversation: the order you work in, what your exported folders are called, which settings you quantify with.

1. Open **Settings > Integration > Assistant Notes**.
2. Type the note, up to 2,000 characters. The count below the box shows what you have used.
3. Click **Save Settings**.

Manage notes the same way as the other presets: **... > Add Preset...**, **... > Rename Preset...**, **... > Delete Preset...**, and **... > Load System Default** to empty the box. The note selected in the drop-down list is the one an assistant is given.

A saved note reaches an assistant the next time the Claude or ChatGPT desktop app connects to MyWB; there is no need to restart MyWB or switch access off and on. Saving a note does not update a conversation that is already connected. In the Claude desktop app, quit and reopen the app, then start a new conversation. In the ChatGPT desktop app, start a new conversation. A note is also a preference and not a permission — the operations that ask for your answer still ask. See [Save your usual instructions](ai-assistant.md#save-your-usual-instructions).

## Advanced integration settings

**Settings > Integration > Advanced** holds nothing to save. It is for registering MyWB with an MCP client by hand: a one-line command each for Claude Code and Codex, and the launcher path for another MCP client. You do not need it if you installed the MyWB extension or plugin. See [Other MCP clients](ai-assistant.md#other-mcp-clients).

## Continue with

- [Add, change, or remove molecular-weight marker labels](edit-roi-and-labels.md#add-marker-and-sample-positions)
- [Add, change, or remove sample labels](edit-roi-and-labels.md#add-marker-and-sample-positions)
- [Adjust fonts, spacing, margins, and image size](design-and-preview-figure.md#edit-svg-style)
- [Use MyWB with an AI assistant](ai-assistant.md)
