# Use MyWB with an AI assistant

[← How to use MyWB](../user-guide.md)

Let an AI assistant read and adjust the document you have. It works with the Claude or ChatGPT desktop app on the same computer as MyWB; Claude Code, Codex and other MCP clients work too. [Premium Access](premium-access.md) must be verified on MyWB side. <img src="../assets/premium-badge.svg" alt="Premium" height="18" align="absmiddle">

> [!CAUTION]
> Most AI assistants run their model on a remote service, such as servers of Anthropic or OpenAI, so what AI assistants read from MyWB may be sent to that service. Read [What the assistant can see and do](#what-the-assistant-can-see-and-do) before you switch access on.

**On this page**

- [Install extension or plugin](#install-extension-or-plugin)
- [Turn AI assistant access on](#turn-ai-assistant-access-on)
- [Start working with an assistant](#start-working-with-an-assistant)
- [Save your usual instructions](#save-your-usual-instructions)
- [While an assistant is working](#while-an-assistant-is-working)
- [Updating MyWB](#updating-mywb)
- [What the assistant can see and do](#what-the-assistant-can-see-and-do)
- [Troubleshooting](#troubleshooting)

## Install extension or plugin

An extension or a plugin is the bridge between MyWB app and an AI desktop app, such as Claude desktop app and ChatGPT desktop app. It tells the assistant what MyWB can do, and passes the assistant's requests on to the MyWB window you have open.

### Claude

There are three ways to install MyWB in Claude. They differ in where in Claude you can use it.

| | Extension | Plugin from a file | Plugin from the marketplace |
| --- | :---: | :---: | :---: |
| Chat in Claude desktop app | ✅ | ❌ | ❌ |
| Cowork in Claude desktop app | ✅ | ✅ | ✅ |
| Code in Claude desktop app | ✅ | ✅ | ✅ |
| Claude Code in a terminal or an IDE | ❌ | ✅ | ✅ |
| Claude on the web or a smartphone | ❌ | ❌ | ❌ |

**Not sure which? Install the extension.** It is the only one that works in chat. The extension, the plugin, and the marketplace routes give you the same MyWB tools.

> **Your organization may limit the choice.** On a Team or Enterprise plan, an organization can turn extensions off or allow only the ones it lists, and can stop members from uploading plugins or adding marketplaces. If one way is refused, try another, or ask your organization's administrator.

#### Extension

<p align="center">
  <a href="https://github.com/MasaakiU/MyWB-releases/raw/master/integrations/claude-desktop/mywb.mcpb"><img src="../assets/download-claude-extension.svg" alt="Download the MyWB extension for Claude (mywb.mcpb)" height="68"></a>
</p>

1. Download `mywb.mcpb` with the button above.
2. Open the downloaded file. Claude Desktop shows MyWB with an **Install** button.
   - If opening the file does not start Claude Desktop, open **Settings > Customize > Connectors** in Claude Desktop, choose **Add custom connector**, and select the downloaded `mywb.mcpb`.
3. Click **Install**. MyWB then appears in **Settings > Customize > Connectors**, with the type **Desktop**.

The same file works on macOS and Windows. It contains no program of its own: it points at the copy of MyWB already installed on your computer.

#### Plugin from a file

<p align="center">
  <a href="https://github.com/MasaakiU/MyWB-releases/raw/master/integrations/claude-desktop/mywb-plugin.zip"><img src="../assets/download-claude-plugin.svg" alt="Download the MyWB plugin for Claude (mywb-plugin.zip)" height="68"></a>
</p>

1. Download `mywb-plugin.zip` with the button above. Leave it zipped.
2. In Claude, open **Settings > Customize > Plugins**, then **Add > Upload plugin**, and choose the downloaded `mywb-plugin.zip`.

The plugin simply wraps the [extension](#extension) described in the previous section, so it gives you exactly the same MyWB tools. The only difference is where in Claude you can use it; see the table above.

#### Plugin from the marketplace

1. In Claude, open **Settings > Customize > Plugins**, then **Add > Add marketplace**.
2. In the **URL** field, enter `MasaakiU/MyWB-releases`.
3. Leave **Sync automatically** on, so the plugin is kept up to date when it changes, and click **Sync**.
4. Find **MyWB** among the plugins and add it.

Either way, a plugin is added to your Claude account. Claude Code on your computer picks it up the next time it starts, as long as it is signed in to the same account (Claude Code 2.1.273 or later). Claude Code can also install it on its own, from a terminal:

```bash
claude plugin marketplace add MasaakiU/MyWB-releases
claude plugin install mywb@mywb
```

### ChatGPT desktop app and Codex

In ChatGPT, MyWB is installed as a plugin, and the plugin works in Work and Codex but not in chat.

| | Plugin |
| --- | :---: |
| Chat in the ChatGPT desktop app | ❌ |
| Work in the ChatGPT desktop app | ✅ |
| Codex in the ChatGPT desktop app | ✅ |
| Codex in a terminal or an IDE | ✅ |
| ChatGPT on the web or a smartphone | ❌ |

There is nothing to download. Just follow the instructions below:

1. In the ChatGPT desktop app, open **Settings > Plugins**, then **Add > Add a marketplace**.
2. In the **Source** field, enter `MasaakiU/MyWB-releases`, and click **Add marketplace**.
3. Select the **Personal** tab. If you added the marketplace earlier, open **Settings > Plugins > Browse directory > Personal** instead.
4. Click **+** next to **MyWB (macOS)** or **MyWB (Windows)**, whichever matches your computer. Install only the one for the computer you are on.

Codex in a terminal or an IDE uses what the desktop app installed, so there is no need to install MyWB there again. If you use Codex without the desktop app, install it from a terminal instead:

```bash
codex plugin marketplace add MasaakiU/MyWB-releases
codex plugin install mywb-macos   # or mywb-windows
```

### Other MCP clients

Any client that speaks [MCP](https://modelcontextprotocol.io) over standard input and output can be pointed at MyWB directly, without a plugin. Turn AI assistant access on, then open **Settings > Integration > Advanced** and copy the command for your client:

- for Claude Code, a one-line command to run once in a terminal (PowerShell on Windows);
- for Codex, its own one-line command to run once in the same shell;
- for another MCP client, the path of the MyWB launcher, to enter where the client asks for a command to run.

Registering is a one-off either way. The address and the token change every time MyWB starts, and the client finds the new ones by itself.

## Turn AI assistant access on

Access is **off by default**. Switch it on in the MyWB window the first time you use an assistant.

1. Click <picture><source media="(prefers-color-scheme: dark)" srcset="../assets/ai_gray20.svg"><img src="../assets/ai.svg" alt="" width="18" height="18" align="absmiddle"></picture> **AI assistant access** at the bottom of the left sidebar.
2. The button is highlighted only while access is actually on. If access could not start, it is not highlighted, even though you clicked it.

**Settings > Integration > AI Assistant Access** also shows the current state and can switch access on or off as well. **Allow an AI assistant to use this window** checkbox switches access at once, as the button does; **Cancel** puts it back the way it was when Settings opened. The status line on that page always shows whether access is on right now. Your choice is remembered: if you leave access on, it starts again after MyWB opens and Premium Access is verified. It also returns automatically if Premium Access lapses and is later verified again, provided the setting is still on.

> [!CAUTION]
> **Turn it off when you are not using an assistant.** While it is on, any program on your computer that has the access token can do what an assistant can: read the document you have open, and change it.

## Start working with an assistant

1. Open MyWB and check that the AI button is highlighted.
2. In Claude desktop app or the ChatGPT desktop app, start a new conversation where MyWB works: see the tables in [Install extension or plugin](#install-extension-or-plugin). There is no need to restart the app after installing. If new tools are missing after a MyWB update, see [Updating MyWB](#updating-mywb).
3. Ask the assistant to use MyWB, and say what you want done.

Example:

> Create a Western blot figure using MyWB. The raw data are located in `path/to/datafolder`.
>
> There are three membranes: the top one is the FLAG blot, the bottom-left one is the V5 blot, and the bottom-right one is the HA blot. For each blot, the left three lanes are WT and the right three lanes are KO, with replicates 1, 2, and 3 arranged from left to right within each group.
>
> Use placeholder values for the molecular weight markers for now. I'll edit them later.
>
> Finally, assemble the three blots into a single figure, arranged vertically from top to bottom in the order HA, FLAG, and V5.

**With several MyWB windows open**, each window with access on takes a letter — `A`, `B`, and so on — shown at the end of its title bar and on the Settings page. Tell the assistant which letter to work in. Asked to act with several windows open and no letter given, it lists them and asks rather than guessing.

## Save your usual instructions

You may find yourself giving the same instructions in every conversation. Instead of writing them into every prompt, save them once:

1. Open **Settings > Integration > Assistant Notes**.
2. Type the note in your own words. The box holds up to 2,000 characters and counts what you have used. For example:
   ```
   Set ROI padding to 10%, for more room above and below the bands.
   Name export folders figures_YYYYMMDD_<2-3 word summary>, e.g. figures_20261113_WT-vs-KO.
   Always uses a BG percentile 5 for quantification.
   ```
3. Click **Save Settings**.

You can keep several notes and switch between them with the drop-down list, the same way as the other presets: [Marker Auto Fill, Sample Prefix Auto Fill](settings.md#auto-fill-presets) and [SVG Style](settings.md#svg-style-presets). Two things are worth knowing:

- **A changed note reaches the assistant the next time the Claude or ChatGPT desktop app connects to MyWB.** There is no need to restart MyWB or switch AI assistant access off and on. Saving a note does not update a conversation that is already connected.
  - **Claude desktop app:** To apply a new note, quit and reopen the app, then start a new conversation. Starting a new conversation without reopening the app is not enough.
  - **ChatGPT desktop app:** To apply a new note, start a new conversation; there is no need to reopen the app.
- **A note is a preference, not a permission.** Writing over a file, moving one to the Trash, and throwing away unsaved changes are still asked in MyWB's own window, whatever a note says. See [What the assistant can see and do](#what-the-assistant-can-see-and-do).

## While an assistant is working

Before it changes anything, an assistant tells MyWB what it is about to do, and MyWB lends it that one window. The window greys over and a card names the job, with how long it has been going and a **Stop and Take This Window Back** button. Only that window is lent out: your other MyWB windows are untouched, and you can carry on working in them.

- **You do not have to wait for it to finish.** Press the button and the window is yours again at once. What the assistant already did stays, each change as its own step in the Edit menu, so you can take back as much of it as you want. What it had not got to will not happen, and it is told it was stopped, so it should tell you where it got to rather than starting the job again.
- **You do not have to press anything either.** If nothing is asked of the window for two minutes the session lapses by itself, and it never lasts more than half an hour, so an assistant that crashed cannot leave a window locked.

## Updating MyWB

MyWB can notify a connected assistant when its tools change after an update. Assistants that support this notification can refresh their tool list without restarting the assistant's app. The first request after the update may still use the old tool list and fail.

**If new tools are missing or requests keep failing after an update, quit and reopen the Claude or ChatGPT desktop app**, or Claude Code or Codex if you use them in a terminal. Reconnecting lets the assistant read the current tool list. There is no need to reinstall the extension or plugin; if Claude desktop app offers to update the extension, you can accept or ignore it.

## What the assistant can see and do

With AI assistant access on, an assistant can read and edit the document in that MyWB window. You control whether it may overwrite files, move them to the Trash, or discard unsaved work.

### What it can see

When requested, MyWB can provide:

- **Document contents:** ROIs, marker and sample labels, the band table, image adjustments, figure style, output settings, and quantification results.
- **File information:** names and paths of the files open in the window and those listed under **File > Open Recent**.
- **Settings and instructions:** MyWB settings and your [Assistant Notes](#save-your-usual-instructions).
- **Visual results:** a picture of the MyWB window and results from Auto Detect when the assistant runs it.
- **Measurements:** intensity profiles and the positions of lanes, bands and membranes measured from an image pane, when the assistant asks for them.
- **A folder you name:** the names and paths of the images, subfolders and MyWB files in it, what each image records about how it was taken (such as the instrument, exposure time and date), and reduced pictures of the images, including ones not opened in MyWB. When it compares exposures, the number of saturated pixels in a region of each image and a picture of that region.

The [MyWB Privacy Policy](../legal/privacy-policy.md#ai-assistant-access) gives the full list.

### Where that information goes

MyWB passes information to the assistant's app on your computer, such as Claude Desktop or the ChatGPT desktop app. It does not send it to MyWB's developer or a MyWB service. The connection accepts requests only from the computer MyWB runs on (`127.0.0.1`), with an access token that changes each time MyWB starts.

**The assistant may then send that information to its provider's servers (e.g., Anthropic or OpenAI).** Most assistants run their model on a remote service, under that provider's terms and privacy policy. MyWB cannot control what happens to information after handing it to the assistant. Before switching access on, decide whether the images, labels, and measurements in your document may be shared with that provider, especially if they are unpublished or confidential.

### What it can do

- **Edit the figure:** change ROIs, marker and sample labels, the band table, image adjustments, figure style, and output settings.
- **Work with files:** open and close images and documents, save, rename, duplicate, and export. The permissions below control overwriting, moving files to the Trash, and discarding unsaved work.
- **Analyze bands:** run [quantification](quantify-bands.md) and Auto Detect.
- **Undo and redo edits:** use **Edit > Undo** and **Edit > Redo**, including edits you made yourself. It is instructed to tell you what it undid.

Document edits appear as individual steps in the Edit menu. Use <kbd>Ctrl+Z</kbd> to undo one assistant action at a time.

**Auto Detect shows a preview before applying results.** Nothing is added to the document until **Place** is pressed. You can press **Place** or **Cancel** yourself; the assistant is instructed to ask before replacing existing marks. If Auto Detect fits several ROIs, each ROI after the first is saved in a new MyWB file beside the document.

### Which actions need your permission

Saving under a new name, renaming to an unused name, duplicating, and exporting can proceed without a MyWB confirmation. Each export goes into a new folder beside the source image, so it does not overwrite an earlier export; a rebuilt source image goes beside the original as `<name>_restored.<ext>`, and is refused a name that is already taken.

Files the assistant made itself in this window — saved under a new name, written by its own **Place** for further ROIs, or made by combining files into an assembly or moving panels out — it can save over, and Combine can move them to the Trash, without asking, as long as nothing else has written to them since; **Never allow** still blocks it. A copy made with **Duplicate** is not one of them. Switching AI assistant access off forgets which files these are.

**By default, MyWB asks before the assistant:**

- Overwrites an existing file.
- Moves a document's file to the Trash.
- Discards unsaved changes, including when switching to another document.

The question appears in the MyWB window with **Don't Allow**, **Allow Once**, and **Allow for This Session**. The assistant cannot answer for you, and an unanswered request does not proceed. If another window or program has changed a file since MyWB read it, the question names that file and explains the conflict.

You can set these permissions in advance under **Settings > Integration > AI Assistant Access**. Choose a setting separately for **Overwrite a file**, **Move a file to Trash**, and **Discard unsaved work**:

| Setting | What happens |
| --- | --- |
| Never allow | MyWB blocks the action without showing a question. The assistant is told not to ask again. |
| Ask each time | The default. MyWB asks you in its window. |
| Allow without asking | MyWB allows the action without a confirmation. |

These settings take effect when you click **Save Settings**. They apply only to that window, are not saved to disk, and reset when MyWB closes or you switch AI assistant access off and on again.

**Unsaved work has a separate permission.** Allowing a file to be moved to the Trash does not also allow its unsaved changes to be discarded. Moving a file with unsaved changes to the Trash always requires confirmation; MyWB blocks it if **Discard unsaved work** is set to **Never allow**.

Claude or ChatGPT may ask for permission to use MyWB tools. Those prompts are separate from MyWB's confirmations, and changing MyWB settings does not change them.

## Troubleshooting

**The assistant says it cannot reach MyWB.** The assistant's app (i.e., the Claude desktop app or the ChatGPT desktop app) can be opened before MyWB: ask the assistant to open MyWB, or open it yourself, and ask again. If MyWB is open, check that the AI button shows access is on. A remembered on setting takes effect once Premium Access is verified; otherwise, switch access on yourself.

**Claude does not offer MyWB in chat, but it works in Cowork or Claude Code.** Only the plugin is installed, and chat does not run a plugin's connection to programs on your computer. Install the [extension](#extension) for chat.

**ChatGPT does not offer MyWB in chat, but it works in Work or Codex.** That is expected: chat does not run a plugin's connection to programs on your computer. Use Work or Codex; see [ChatGPT desktop app and Codex](#chatgpt-desktop-app-and-codex).

**Claude asks before every MyWB step.** In Claude, choose **Always allow** if you want it to use MyWB tools without repeated prompts. With the extension, you can allow all MyWB tools under **Settings > Customize > Connectors > MyWB**. MyWB still applies the [permissions described above](#which-actions-need-your-permission).

**The assistant does not know a tool the release notes mention.** It may still have the tool list from before MyWB was updated. If it has not refreshed automatically, quit and reopen the assistant's app; see [Updating MyWB](#updating-mywb).

**The assistant reports that a change was refused.** It is reading a document that has moved on since it last looked — usually because you edited the window while it was working. Ask it to read the document again and repeat the change. Announcing work, which locks the window, is what normally prevents this.

**A window is greyed over and you want it back.** Press **Stop and Take This Window Back** on the card. See [While an assistant is working](#while-an-assistant-is-working).

**Premium Access has lapsed.** AI assistant access stops with it, and MyWB clears the button. See [If Premium features are unavailable](premium-access.md#if-premium-features-are-unavailable).

**Report a bug or ask a question.** See [Troubleshooting](../troubleshooting.md#report-a-bug-or-ask-a-question).
