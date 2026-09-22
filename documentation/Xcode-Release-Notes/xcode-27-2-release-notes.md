# Xcode 27.2 Beta Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 27.2 beta includes Swift 6.4 and SDKs for iOS 27.2, iPadOS 27.2, tvOS 27.2, watchOS 27.2, macOS 27.2, and visionOS 27.2. Xcode 27.2 beta supports on-device debugging in iOS 17 and later, tvOS 17 and later, watchOS 10 and later, and visionOS. Xcode 27.2 beta requires a Mac running macOS Tahoe 26.6 or later.

> ❗ **Important**: [`Download Xcode 27.1 beta`](https://developer.apple.comhttps://developer.apple.com/download/applications/) to get the iOS SDK and simulator support for iPhone Duo.

See [`Xcode Support`](https://developer.apple.comhttps://developer.apple.com/support/xcode/) to learn more about compatible platforms and deployment targets.

##### General

###### Known Issues

- Xcode may crash when using code completion on macOS 27.2 beta. (186939138) **Workaround:** Turn off enhanced code completion ranking with the following preference:
`defaults write com.apple.dt.Xcode CodeCompletionAssetsToLoad /dev/null`

##### Device Hub

###### Known Issues

- Keyboard and mouse inputs to simulators for OS versions before iOS 18.0, tvOS 18.0, watchOS 11.0, and visionOS 2.0 are not accepted. (181945323)
- After disconnecting a physical device from Device Hub when “Simulate Hardware Keyboard” was in use, the device may remain in “hardware keyboard” mode for up to 2 minutes. This will cause the software keyboard to not appear when selecting a text field. (182553164) **Workaround:** Wait 2 minutes for the condition to clear.

##### Previews

###### Resolved Issues

- Fixed an occasional issue where selecting a preview from a preview group’s thumbnail grid on macOS would fail to 1-up the right preview. (183475595)
- Fixed: A clearer error is now shown when the selected platform does not support a preview’s content. (185436582)
- Fixed: The RenderPreview MCP tool now returns the list of available render destinations, and lets the caller specify which destination to use for rendering. (186442676)

##### Previews Playgrounds

###### Resolved Issues

- Fixed: A clearer error with recovery steps is now shown when previews fail because another user account on this Mac owns the Previews JIT directory. (184564292)

##### Project Format

###### New Features

- Xcode now supports a JSON-based project format (.xcproj) that’s more readable, merge-friendly, and easier for coding agents to edit. Enable it in the file inspector. Projects using .xcproj also open in earlier versions of Xcode 27. Learn more in [`Updating your Xcode project configuration file format`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/updating-your-xcode-project-configuration-file-format). (184661114)

##### Sdk

###### Known Issues

- macOS, watchOS, tvOS, and visionOS SDKs in Xcode 27.2 incorrectly report 27.1 as a valid deployment target. Builds and other functionality may have unexpected behavior if this deployment target is used. Mac Catalyst builds with a 27.1 or 27.2 deployment target may be unable to use newly introduced API. (187160501)

##### Simulator

###### Known Issues

- Some simulator runtimes are not completely deleted when removed, re-appearing after a reboot. (141290052) (FB16083602)

## See Also

- [Xcode 27.1 Beta Release Notes](xcode-27_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27 Release Notes](xcode-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes)*