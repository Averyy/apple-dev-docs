# Xcode 27.3 Beta Release Notes

**Framework**: Xcode Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

Xcode 27.3 beta includes Swift 6.4 and SDKs for iOS 27.3, iPadOS 27.3, tvOS 27.3, watchOS 27.3, macOS 27.3, and visionOS 27.3. Xcode 27.3 beta supports on-device debugging in iOS 17 and later, tvOS 17 and later, watchOS 10 and later, and visionOS. Xcode 27.3 beta requires a Mac running macOS Tahoe 26.6 or later.

See [Xcode Support](https://developer.apple.com/support/xcode/) to learn more about compatible platforms and deployment targets.

### Coding Intelligence

#### New Features

- GitHub Copilot is now available in the coding assistant. (185837709)

### Device Hub

#### New Features

- You can now drag items onto a device in Device Hub. Drop an app (`.app` or `.ipa`) to install it, or drop a link to open it on the device. On iOS simulators, drop any other file to save it with the Files app. (179246120) (FB23037189)

#### Resolved Issues

- Device Hub now supports using option-drag to simulate two-finger touch gestures for iPhones and iPads. (169537162)
- Device Hub now accepts keyboard and mouse input for OS simulators earlier than iOS 18.0, tvOS 18.0, watchOS 11.0, and visionOS 2.0. (190652440)

#### Known Issues

- Device Hub support for CarPlay requires devices to be physically connected via USB cable (not over the network). iOS Simulator is not supported for CarPlay. (179494052) (FB23101450)
- When using Device Hub via Sidecar or a Mac with Touch, only two touches can be sent to the target device. Three or more touches are interpreted by macOS as a system gesture. (185140491)

  **Workaround:** Turn off touch gestures in Settings under Touch Display.

### Previews

#### New Features

- RenderPreview MCP tool snapshot filenames and metadata now include the applied overrides. (176531615)
- RenderPreview MCP tool now supports interactive delayed snapshots for macOS previews. (181244878)

#### Resolved Issues

- A clearer error is now shown when the sandbox blocks a library from loading in a preview. (147269145)
- macOS widget previews now fail with a clear error. (178635433)
- Fixed a crash that could occur when building a preview after the workspace closes. (183679367)
- Fixed excessive processing time for source files that contain long operator chains. (184132564)
- Fixed an issue where previews refreshed unnecessarily when an Xcode project or workspace had not changed. (187278576) (FB24753484)
- Previews now refresh when asset catalog contents change on disk. (187456273) (FB24785391)
- Fixed an issue where the RenderPreview MCP tool could report no previews before they finished loading. (188424749)
- Fixed an issue where the RenderPreview MCP tool could render a different preview than the one requested. (188817121)
- Fixed a crash that could occur when changing code while in the Resizable Canvas mode. (189463909)

### Simulator

#### Resolved Issues

- Fixed: Simulator runtimes might be inaccessible to users who are in the `daemon` group. (User accounts should not be added to the `daemon` group.) (190649396)

### Swift Testing

#### New Features

- Xcode now supports writing UI tests with Swift Testing and `XCUIAutomation`. (95593221)

### UI Automation

#### New Features

- `XCUIAutomation` supports setting the hinge angle on iPhone Duo with a new `XCUIHinge` class. (187479559)

### Xcode AEA

#### New Features

- Xcode is now available as an Apple Encrypted Archive (`.aea`).  If you’re installing Xcode from the command line, use `archiveutil extractXcodeAEA` to extract the Xcode archive.

  Xcode 27.3 is the final release supporting the `.xip` format. (111337953)

## See Also

### Xcode 27
- [Xcode 27.2 Release Notes](./xcode-27_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27.1 Release Notes](./xcode-27_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27 Release Notes](./xcode-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes)*