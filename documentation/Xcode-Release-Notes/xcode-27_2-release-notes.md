# Xcode 27.2 Release Notes

**Framework**: Xcode Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

Xcode 27.2 includes Swift 6.4 and SDKs for iOS 27.2, iPadOS 27.2, tvOS 27.2, watchOS 27.2, macOS 27.2, and visionOS 27.2. Xcode 27.2 supports on-device debugging in iOS 17 and later, tvOS 17 and later, watchOS 10 and later, and visionOS. Xcode 27.2 requires a Mac running macOS Tahoe 26.6 or later.

See [Xcode Support](https://developer.apple.com/support/xcode/) to learn more about compatible platforms and deployment targets.

### Device Hub

#### New Features

- When used via Sidecar or a MacBook with Touch, Device Hub now sends touches on the iPad screen to the remote device as touches. This allows you to use multi-finger gestures such as pinch and rotate to test your applications. (188634387)
- Device Hub in Xcode 27.2 contains multiple improvements:

  - Support for touch events through Sidecar
  - Support for Standby in iPhone Duo
  - Input support for iOS 17.x simulator runtimes
  - Slow Motion Animation (simulators only)
  - Simulate Shake (simulators only)
  - Simulate Fall (simulators only)
  - Simulate Memory Pressure (simulators only)
  - Context Menu for Screenshots
  - Improved Drag and Drop Compatibility for Screenshot Icon
  - Option to Hide Device Bezels
  - App Settings

    - Quit Behavior for Booted Simulators
    - Keyboard Shortcut Behavior
    - Secure Keyboard Entry
    - Hardware Keyboard Simulation
    - Screen Capture Save Location (189236369)

#### Resolved Issues

- Fixed: Modifier keys such as Shift, Control, Option, and Command were not sent to the correct device when more than one device window was open. (177181719)
- Fixed: Keyboard and mouse inputs to simulators for OS versions before iOS 18.0, tvOS 18.0, watchOS 11.0, and visionOS 2.0 were not accepted. (181945323)
- Fixed: After disconnecting a physical device from Device Hub when “Simulate Hardware Keyboard” was in use, the device might have remained in “hardware keyboard” mode for up to 2 minutes. This caused the software keyboard not to appear when selecting a text field. (182553164)
- Fixed: Device Hub stopped sending touch and button input to a connected device after a period of inactivity. (182695157) (FB23873443)
- Device Hub now supports input to iOS 17 simulator devices. (187484157)
- Fixed: Selecting a Vision Pro simulator in Device Hub might cause Device Hub to quit unexpectedly if a visionOS runtime is not available. (188313956)
- Fixed: The Device > Simulate Memory Warning menu item did not work. (188326513)
- Fixed: Device Hub might terminate unexpectedly when running on earlier macOS 27.2 betas. (190126101)

#### Known Issues

- When the “Secure keyboard entry” setting is on, it prevents any app on the system from intercepting keyboard events before Device Hub sends them to the controlled device. It cannot be used at the same time as the “Capture Keyboard” feature. (176305816)
- Device Hub support for CarPlay requires devices to be physically connected via USB cable (not over the network). iOS Simulator is not supported for CarPlay. (179494052) (FB23101450)
- Screenshots and recordings in iPhone Duo might be black for up to a few minutes after booting the device. (187146039)
- VoiceOver, the Accessibility Inspector, and other accessibility tools cannot convey screen content on an iPhone Duo within Device Hub. (187148389)
- Device Hub is unable to customize the text size for a device running iOS 18 or earlier. (189261485) (FB25077755)
- When switching between the inner and outer display of the iPhone Duo simulator, modifier keys such as Shift and Command might stop working. (189465196)

  **Workaround:** Click with the mouse on the currently visible screen.

### Instruments

#### Resolved Issues

- Fixed: Hovering over the top ruler in the timeline would sometimes not show all tooltips for the timestamp you hovered over. (168530263)

### Interface Builder

#### Resolved Issues

- Fixed: Interface Builder `toolchain` compilation mode incorrectly encoded standard/system `UIStackView.spacing` as `0`. (186354589) (FB24605403)
- Fixed: Interface Builder `toolchain` compilation mode failed to encode `UIButtonConfiguration.contentInsets`. (187747632) (FB24829108)

### Mac Catalyst

#### Known Issues

- Projects that use APIs specific to iOS 27.1 show compile errors when building for Mac Catalyst (“undeclared identifier”, “not found”, “has no member”, “cannot find”, and similar errors). (185924957)

  **Workaround:** Use build-time conditionals like `#if !targetEnvironment(macCatalyst)` (Swift) or `#if !TARGET_OS_MACCATALYST` (Objective-C) to isolate affected code.

### Memory Gauge

#### Resolved Issues

- Fixed: Memory usage needle rotated beyond the meter when swap is used. (187611943)

### Previews

#### Resolved Issues

- Fixed an occasional issue where selecting a preview from a preview group’s thumbnail grid on macOS would fail to 1-up the right preview. (183475595)
- A clearer error with recovery steps is now shown when previews fail because another user account on this Mac owns the Previews JIT directory. (184564292)
- A clearer error is now shown when the selected platform does not support a preview’s content. (185436582)
- Fixed: Previews could fail in source files that use Windows-style (CRLF) line endings. (186255376)
- The RenderPreview MCP tool now returns the list of available render destinations, and lets the caller specify which destination to use for rendering. (186442676)

### Project Format

#### New Features

- Xcode now supports a JSON-based project format (`.xcproj`) that’s more readable, merge-friendly, and easier for coding agents to edit. Enable it in the File inspector. Projects using `.xcproj` also open in earlier versions of Xcode 27. Learn more in [Updating your Xcode project configuration file format](../Xcode/updating-your-xcode-project-configuration-file-format.md). (184661114)

### SDK

#### Known Issues

- macOS, watchOS, tvOS, and visionOS SDKs in Xcode 27.2 incorrectly report 27.1 as a valid deployment target. Builds and other functionality might have unexpected behavior if this deployment target is used. Mac Catalyst builds with a 27.1 or 27.2 deployment target might be unable to use newly introduced API. (187160501)

### Simulator

#### Resolved Issues

- Fixed: Some simulator runtimes are not completely deleted when removed, reappearing after a reboot. (141290052) (FB16083602)
- Fixed: If a simulator runtime is reinstalled after being deleted, it might still show up as unavailable in Xcode. (187950199)
- Fixed: In the iPhone Duo simulator, an app using `CameraCaptureAccessory` could use both displays at the same time without an active camera capture session. (190155353)

#### Known Issues

- Cloning a simulator device running runtime 27.2 might fail due to incorrect file permissions. (188407822) (FB24939277)

  **Workaround:** `find ~/Library/Developer/CoreSimulator/Devices/<SOURCE_UDID>/data -name '*.sb-????????-??????' -delete`

### XCTest UI Automation

#### Resolved Issues

- Fixed: Tests using `.rotateDigitalCrown` might fail due to the device not registering the action. (188422137)

## See Also

### Xcode 27
- [Xcode 27.1 Release Notes](./xcode-27_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27 Release Notes](./xcode-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes)*