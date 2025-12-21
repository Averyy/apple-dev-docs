# Xcode 26.1.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.1.1 includes Swift 6.2.1 and SDKs for iOS 26.1, iPadOS 26.1, tvOS 26.1, macOS 26.1, and visionOS 26.1. Xcode 26.1.1 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.1.1 requires a Mac running macOS Sequoia 15.6 or later.

##### General

###### Resolved Issues

- Fixed an issue causing background indexing not to complete for some projects.  (160820381) (FB20286513)

###### Known Issues

- Simulators may fail to boot during the first build after upgrading macOS.  (152328794)  Execute `xcrun simctl runtime dyld_shared_cache update --all` prior to booting the simulator to ensure dyld shared cache generation has completed.

##### Address Sanitizer

###### Known Issues

- Address Sanitizer is currently incompatible with hardware memory tagging.  (161649378)  Disable hardware memory tagging when running with Address Sanitizer by un-checking the “Enable Hardware Memory Tagging” box in the “Enhanced Security” capability section of your Xcode project settings.

##### Callkit

###### Resolved Issues

- Fixed: visionOS 3rd-party apps using LiveLookup may hit a compilation failure if referencing `LiveLookupDBExtensionCoreDataPropertiesSet`.   (162615774)

##### Coding Intelligence

###### Resolved Issues

- Fixed: Improved the memory usage of the Coding Assistant in projects with large git repositories.  (155382239)
- Fixed: Coding tools may become unavailable in the source editor, and may fail when used in menus.  (160972804)
- Fixed: The Coding Assistant’s “find text in file” tool may return incorrect line numbers, causing failed text replacements.  (161690692)
- Fixed: Users interacting with ChatGPT in Xcode might experience performance issues when the assistant is applying code changes.  (163507099)

###### Known Issues

- Users interacting with ChatGPT in Xcode may not receive previews of sample code.  (164573607)  Clicking the copy button allows you to access the contents of the sample code.

##### Devices

###### New Features

- The `devicectl` command line tool now supports gathering a sysdiagnose from a connected device. To use this functionality, run `xcrun devicectl device sysdiagnose`.  (160492448)

##### Enhanced Security

###### New Features

- When enabling Hardware Memory Tagging under Enhanced Security (Capabilities editor -> Enhanced Security -> Memory Safety -> Enable Hardware Memory Tagging), all applications will currently run under Soft Mode irrespective of the Soft Mode for Memory Tagging option.  (160806045)

##### Instruments

###### New Features

- View body and view representable updates that were skipped are labeled as “Skipped Update” instead of “Update” in summaries and the cause graph.  (157571061)

###### Resolved Issues

- Fixed: When using detail filter in the aggregation views, Instruments wouldn’t recalculate aggregation function results based on the filtered output.  (147846388)
- Fixed an issue where Instruments detail filter would reset in the Call Tree view when timeline selection is changed.  (157571541)
- Fixed an issue where `xctrace list instruments` wouldn’t list some of the available instruments to record.  (157695053)
- Fixed: a.out files could not be selected for launch using the file browser.  (158295042) (FB19629820)
- Fixed: Foundation Models Instrument shows incorrect input and output token counts.  (159793146)
- Fixed: Instruments could crash when processing a SwiftUI trace of an app that was already running.  (160881881)
- Fixed: ‘Set Inspection Range and Zoom’ context menu button on an events table view wouldn’t cause timeline to zoom into the selected range.  (161122705)
- Fixed: Processor Trace Instrument doesn’t allow for recording on iPhone 17 family of devices.  (161440613)

##### Interface Builder

###### Resolved Issues

- Fixed: In the Components settings, the Add Platforms view may have two identical items that appear with different sizes. The larger one has Intel support.  (160642378)

##### Localization

###### Resolved Issues

- Fixed: The String Catalog editor now has improved persistence of column sizes.  (138817529) (FB15620865)
- Fixed an issue where Xcode and `xcstringstool` may not extract strings from localization macros that contain empty arguments. For example: `NSLocalizedString(@“key1”, )`  (144548519) (FB16477769)
- Fixed a potential crash when editing a translation in a String Catalog while filtering.  (160557189) (FB20245249)

##### Previews

###### Resolved Issues

- Fixed: Previews should now work in projects using mergeable libraries.  (156593454) (FB19043520)
- Fixed: When switching between visionOS previews, it is possible to get a momentary “Resource Invalidation” error. This can be worked around by just resuming the preview by clicking the resume button or pressing Command-Option-P.  (158613019)

##### Simulator

###### Resolved Issues

- Fixed: `simctl list devices --json` should now list all devices when multiple simulator runtimes with the same identifier are present on the system.  (106564770)

##### Swift Packages

###### Resolved Issues

- Fixed: Packages resolved from a package registry are now cached locally with a 1 hour expiry to reduce unnecessary fetches. (https://github.com/swiftlang/swift-package-manager/pull/9144)  (160953355)

##### Testing

###### Resolved Issues

- Fixed: If an issue is recorded during a Swift Testing test via an API such as `#expect` or `Issue.record()` in a context which is unassociated with the test, such as via `Task.detached { … }` or a `DispatchQueue`, the test process no longer unexpectedly terminates and Xcode shows the issue.  (156631722)

##### Xcode Cloud

###### Resolved Issues

- Fixed: The Xcode Cloud logo failed to display in the Report Navigator’s Cloud Reports tab. If you’re upgrading from the prior beta release (17B5025f) and continue to experience this issue, uninstall the previous version and restart your system.  (160716132)

## See Also

- [Xcode 26.2 Release Notes](xcode-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.0.1 Release Notes](xcode-26_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26 Release Notes](xcode-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_1-release-notes)*