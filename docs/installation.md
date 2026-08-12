# Installation

[← Back to README](../README.md)

## System requirements

| Platform | Required operating system and architecture |
| --- | --- |
| macOS | macOS 15 (Sequoia) or later; Apple silicon (`arm64`) or Intel (`x86_64`) |
| Windows | 64-bit Windows 10 version 1809 or later, or Windows 11 (`x86_64`) |

Linux and native Windows Arm builds are not currently available. Windows 11
on Arm can run the Windows `x86_64` build through the operating system's x64
emulation.

## macOS

Download the latest version for your Mac. To check which type of Mac you have, open the Apple menu and select `About This Mac`.

- **[Apple silicon (`arm64`)](https://download.mybioapps.com/mywb/download/latest/macos/arm64)** — for Macs with an Apple M-series chip. The downloaded file ends in `-macos-arm64.dmg`.
- **[Intel (`x86_64`)](https://download.mybioapps.com/mywb/download/latest/macos/x86_64)** — for Macs with an Intel processor. The downloaded file ends in `-macos-x86_64.dmg`.

Once you have downloaded the appropriate version:

1. Quit MyWB if it is currently running.
2. Open the downloaded `.dmg` file.
3. Drag `MyWB.app` into the `Applications` folder.
4. If Finder asks whether to replace an existing `MyWB.app`, click **Replace**.

### First launch

The current MyWB release is not signed with a Developer ID certificate and has not been notarized by Apple, so macOS will normally block it on first launch. To allow MyWB to run:

1. Double-click `MyWB.app` in the `Applications` folder once, then dismiss the warning that says the developer cannot be verified or Apple cannot check the app for malicious software.
2. Open `System Settings` and go to `Privacy & Security`.
3. Scroll down to the `Security` section and click `Open Anyway` next to the message about `MyWB.app`.
4. Enter your Mac password or use Touch ID if asked.
5. When the warning appears again, click `Open`.

`Open Anyway` is available for about one hour after the first launch attempt. Only override the warning if you downloaded MyWB using the official links above. Do not override an alert saying that the app will damage your computer or is damaged; download the DMG again and report the problem if it continues.

For more information, see [Apple's instructions for opening an app from an unidentified developer](https://support.apple.com/102445).

## Windows (x86_64)

**[Download the latest Windows x86_64 Setup](https://download.mybioapps.com/mywb/download/latest/windows/x86_64)**. The downloaded file ends in `-windows-x86_64.exe`. Windows 11 on Arm devices can run the x86_64 version through Windows' built-in
emulation. A native Arm build is not currently available.

1. Open the downloaded Setup file.
2. If Windows displays a Microsoft Defender SmartScreen warning, select **More info**, then select **Run anyway** only when you downloaded the file from the official link above.
3. Follow the Setup prompts. MyWB installs for your current user and does not require administrator access.
4. Start MyWB from the Start menu or the optional desktop shortcut.
