# Xcode 27.2 Beta 2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 27.2 beta 2 includes Swift 6.4 and SDKs for iOS 27.2, iPadOS 27.2, tvOS 27.2, watchOS 27.2, macOS 27.2, and visionOS 27.2. Xcode 27.2 beta 2 supports on-device debugging in iOS 17 and later, tvOS 17 and later, watchOS 10 and later, and visionOS. Xcode 27.2 beta 2 requires a Mac running macOS Tahoe 26.6 or later.

> ❗ **Important**: [`Download Xcode 27.1 beta`](https://developer.apple.comhttps://developer.apple.com/download/applications/) to get the iOS SDK and simulator support for iPhone Duo.

See [`Xcode Support`](https://developer.apple.comhttps://developer.apple.com/support/xcode/) to learn more about compatible platforms and deployment targets.

##### General

###### Known Issues

- Screenshots and recordings in iPhone Duo may be black for up to a few minutes after booting the device. (187146039)
- Cloning a 27.2 simulator device may encounter an issue due to incorrect file permissions. (188407822) (FB24939277)

##### Coding Assistant

###### New Features

- Added a GetCodeCoverage MCP tool that reports code coverage from the most recent test result, optionally filtered by target or file. (181141715)

##### Device Hub

###### Resolved Issues

- Fixed: Keyboard and mouse inputs to simulators for OS versions before iOS 18.0, tvOS 18.0, watchOS 11.0, and visionOS 2.0 are not accepted. (181945323)
- Fixed: After disconnecting a physical device from Device Hub when “Simulate Hardware Keyboard” was in use, the device may remain in “hardware keyboard” mode for up to 2 minutes. This will cause the software keyboard to not appear when selecting a text field. (182553164)
- Fixed an issue where Device Hub stopped sending touch and button input to a connected device after a period of inactivity. (182695157) (FB23873443)
- Fixed: Device Hub now supports input to iOS 17 Simulator Devices. (187484157)

###### Known Issues

- Fixed an issue where modifier keys such as Shift, Control, Option, and Command were not sent to the correct device when more than one device window was open. (177181719)
- VoiceOver, the Accessibility Inspector, and other accessibility tools cannot convey screen content on an iPhone Duo within Device Hub. (187148389)
- Selecting a Vision Pro Simulator in Device Hub may cause Device Hub to quit unexpectedly if a visionOS runtime is not available. (188313956) **Workaround:** Install the corresponding visionOS runtime from within Xcode or delete the simulator device.
- The Device->Simulate Memory Warning menu item does not work. (188326513)

##### Devices

###### Resolved Issues

- Fixed: Holding Escape does not dismiss keyboard capture mode. (187880316)

##### Mac Catalyst

###### Known Issues

- Projects that use APIs specific to iOS 27.1 show compile errors when building for Mac Catalyst (“undeclared identifier”, “not found”, “has no member”, “cannot find”, etc). (185924957) **Workaround:** Use build-time conditionals like `#if !targetEnvironment(macCatalyst)` (Swift) or `#if !TARGET_OS_MACCATALYST` (ObjC) to isolate affected code.

##### Previews

###### New Features

- The canvas overrides picker now includes a Display group for previewing content on a device’s alternative display. (182598534)

###### Resolved Issues

- Fixed: A clearer error with recovery steps is now shown when previews fail because another user account on this Mac owns the Previews JIT directory. (184564292)
- Fixed an issue where previews could fail in source files that use Windows-style (CRLF) line endings. (186255376)
- Fixed: The RenderPreview MCP tool now returns the list of available render destinations, and lets the caller specify which destination to use for rendering. (186442676)

##### Project Format

###### New Features

- Xcode now supports a JSON-based project format (.xcproj) that’s more readable, merge-friendly, and easier for coding agents to edit. Enable it in the File inspector. Projects using .xcproj also open in earlier versions of Xcode 27. Learn more in [`Updating your Xcode project configuration file format`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/updating-your-xcode-project-configuration-file-format). (184661114)

##### Sdk

###### Known Issues

- macOS, watchOS, tvOS, and visionOS SDKs in Xcode 27.2 incorrectly report 27.1 as a valid deployment target. Builds and other functionality may have unexpected behavior if this deployment target is used. Mac Catalyst builds with a 27.1 or 27.2 deployment target may be unable to use newly introduced API. (187160501)

##### Simulator

###### Resolved Issues

- Fixed: Some simulator runtimes are not completely deleted when removed, re-appearing after a reboot. (141290052) (FB16083602)

###### Known Issues

- Device Hub support for CarPlay requires devices to be physically connected via USB cable (not over the network).  iOS Simulator is not supported for CarPlay. (179494052) (FB23101450)
- If a simulator runtime is re-installed after being deleted, it may still show up as unavailable in Xcode (187950199) **Workaround:** `killall -9 com.apple.CoreSimulator.CoreSimulatorService`

#### Updates in Xcode 272 Beta

##### Previews

###### Resolved Issues in Xcode 272 Beta

- Fixed an occasional issue where selecting a preview from a preview group’s thumbnail grid on macOS would fail to 1-up the right preview. (183475595)
- Fixed: A clearer error is now shown when the selected platform does not support a preview’s content. (185436582)

## See Also

- [Xcode 27.1 RC Release Notes](xcode-27_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27 Release Notes](xcode-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes)*