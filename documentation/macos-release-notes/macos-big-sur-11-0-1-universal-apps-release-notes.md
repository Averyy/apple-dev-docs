# macOS Big Sur 11.0.1 Universal Apps Release Notes

**Framework**: macOS Release Notes

Update your apps to support Macs with Apple silicon.

#### Overview

The macOS 11 Universal Apps beta SDK aids in the creation of Universal Mac apps that run on both Apple silicon and Intel-based Mac computers running macOS Big Sur 11. The SDK comes bundled with Xcode 12.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 12.2, see [`Xcode 12.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-12_2-release-notes).

This page is specific to the Developer Transition Kit. For additional macOS 11 changes, see [`macOS Big Sur 11.0.1 Release Notes`](macos-big-sur-11_0_1-release-notes.md).

##### General

###### Known Issues

> ❗ **Important**: If you need to restore your Developer Transition Kit to macOS Big Sur 11.0.1, you must use another Mac running macOS Big Sur 11.0.1 to perform the restore. (69589918)

If you need to restore your Developer Transition Kit to macOS Big Sur 11.0.1, you must use another Mac running macOS Big Sur 11.0.1 to perform the restore. (69589918)

##### Auto Unlock

###### Known Issues

- Auto Unlock is unsupported. (63733266)

##### Code Signing

###### New Features

- New in macOS 11 on Macs with Apple silicon, and starting in macOS Big Sur 11 beta 6, the operating system enforces that any executable must be signed before it’s allowed to run. There isn’t a specific identity requirement for this signature: a simple ad-hoc signature is sufficient. This new behavior doesn’t change the long-established policy that our users and developers can run arbitrary code on their Macs, and is designed to simplify the execution policies on Macs with Apple silicon and enable the system to better detect code modifications. This new policy doesn’t apply to translated x86 binaries running under Rosetta 2, nor does it apply to macOS 11 running on Intel-based platforms. To reduce the impact on existing development workflows, starting with Xcode 12 beta 4, the toolchain will now automatically sign your executables whenever you build from Xcode, or use command-line utilities such as `clang(1)` or `ld(1)`. Since this signing mechanism generates signatures directly at link time, and doesn’t cover any resource other than the executable, it is expected to be faster than a traditional `codesign(1)` invocation. If you use a custom workflow involving tools that modify a binary after linking (e.g. `strip` or `install_name_tool`) you might need to manually call `codesign(1)` as an additional build phase to properly ad-hoc sign your binary. These new signatures are not bound to the specific machine that was used to build the executable, they can be verified on any other system and will be sufficient to comply with the new default code signing requirement on Macs with Apple silicon. However, given that these signatures do not bear any valid identity, binaries signed this way cannot pass through Gatekeeper. Xcode toolchains have been updated in the latest Xcode beta to automatically apply ad-hoc signatures at link time to support projects that might not already be configured for signing. Install the most current Xcode beta to ensure you have up-to-date tooling support. Software previously built on your Developer Transition Kit might need to be either re-built with new tools, or re-signed with `codesign -s - —preserve-metadata=identifier,entitlements,flags,runtime -f <path to mach-O>`, to resolve issues from using earlier releases of the toolchain, or correct executables that have incorrect or missing code signatures. To check the validity of a signature, run `codesign -v -vvvv —ignore-resources <path to mach-O>`. If the command indicates “valid on disk (not all contents verified)” and “satisfies its Designated Requirement”, the code is valid under this policy. (51911409)

##### Device Management

###### Known Issues

- Using MDM to [`clear the bypass code for Activation Lock`](https://developer.apple.comhttps://developer.apple.com/documentation/devicemanagement/clear_the_bypass_code_for_activation_lock) isn’t supported on the Developer Transition Kit. (66019394)

##### Disk Utility

###### Known Issues

- Formatting an external disk as APFS (encrypted) isn’t currently supported. (63209956)
- You might encounter a kernel panic when attempting to create a new APFS container. (67701824)

##### Displays

###### Known Issues

- HDR displays might show unexpected graphical artifacts. (64372135)

##### Fairplay

###### Known Issues

- FairPlay and FairPlay Streaming support is unavailable, including playback in both native apps and via Rosetta 2. (51825430, 57564513, 63559609, 64439476)

##### Kernel

###### Known Issues

- To generate a Non-Maskable Interrupt, refer to [`Generating a Non-Maskable Interrupt`](https://developer.apple.com/documentation/kernel/generating_a_non-maskable_interrupt). (64048855)

##### Printing

###### Known Issues

- You might experience difficulty adding a printer. (64512490)  Open `/System/Library/CoreServices/` in Finder and select the AddPrinter app. Choose Get Info from the File menu, then enable the “Open using Rosetta” option. Restart your Mac and try adding the printer again.

##### Pro Display Xdr

###### Known Issues

- The Developer Transition Kit is intended for use primarily with the Apple Display (P3-500 nits) preset on Pro Display XDR, as it doesn’t support any Pro Display XDR reference presets. Select the Apple Display (P3-500 nits) preset using a supported Mac before connecting the Pro Display XDR to the Developer Transition Kit, otherwise you might encounter the following: If the Pro Display XDR is configured to use a HDR preset, a “High Dynamic Range” checkbox  appears in Displays Preferences even though the checkbox has no effect. If the Pro Display XDR is configured to use one of the Reference Modes, the brightness control and the “Automatically adjust brightness” checkbox might appear enabled in Displays Preferences, even though they have no effect while in a Reference Mode. (63837010, 63837824)

##### Software Update

###### Known Issues

- You might receive a Download failed error when attempting to use Software Update. (65198213)  Download the full installer or the restore image instead of using Software Update.
- A full installer update is required to update from macOS 11 Big Sur beta 5 to beta 7. Installing via Software Update is supported if your Developer Transition Kit is running beta 3, 4, or 6. (67997566)

###### New Features

- In addition to the existing Apple Configurator 2 “restore” (erase) mode, “revive” (update) mode is now supported for Developer Transition Kit restore images. (63168698)

##### Virtualization

###### Known Issues

- Virtualization isn’t supported on the Developer Transition Kit. Support can be tested using the `kern.hv_support sysctl`.

###### New Features

- New Hypervisor APIs supporting arm64 virtualization on Macs with Apple silicon are available.

## See Also

- [macOS Big Sur 11.5 Release Notes](macos-big-sur-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.4 Release Notes](macos-big-sur-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.3 Release Notes](macos-big-sur-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.2 Release Notes](macos-big-sur-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.1 Release Notes](macos-big-sur-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Release Notes](macos-big-sur-11_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 iOS & iPadOS Apps on Mac Release Notes](macos-big-sur-11_0_1-ios-ipados-apps-on-mac-release-notes.md)
  Considerations for running iPhone and iPad apps on Macs with Apple silicon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-big-sur-11_0_1-universal-apps-release-notes)*