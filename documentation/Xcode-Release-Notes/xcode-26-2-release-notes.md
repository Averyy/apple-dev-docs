# Xcode 26.2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.2 includes Swift 6.2.3 and SDKs for iOS 26.2, iPadOS 26.2, tvOS 26.2, macOS 26.2, and visionOS 26.2. Xcode 26.2 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.2 requires a Mac running macOS Sequoia 15.6 or later.

##### Address Sanitizer

###### Resolved Issues

- Fixed: Address Sanitizer is currently incompatible with hardware memory tagging.  (161649378)

##### Coding Intelligence

###### Resolved Issues

- Fixed: Users interacting with ChatGPT in Xcode might experience performance issues when the assistant is applying code changes.  (163507099)
- Fixed: Users interacting with ChatGPT in Xcode may not receive previews of sample code.  (164573607)

##### Instruments

###### Resolved Issues

- Fixed: Instruments would sometimes fail to automatically find a dSYM for a profiled binary, resulting in lack of symbols in the trace.  (126836231)
- Fixed: Environment updates would show up in the cause and effect graph as multiple nodes instead of being logically grouped  (161448568)
- Fixed: Resolved an issue that would result in longer than expected load times for deferred mode recordings of all processes on an attached device.  (162242393)
- Fixed: The Allocations instrument sometimes fails to report reference counting operations for native Swift types.  (163080666)
- Fixed: After focusing on a subtree, the Call Tree/Flame Graph toggle may not be clickable  (163147572)
- Fixed a crash that would occur when sorting specific columns in the Foundation Models instrument  (164113337)

##### Localization

###### Resolved Issues

- Fixed: Resolved an issue where the wrong string could be annotated in a screenshot in Localization Catalog Editor.  (162370185) (FB20608107)

##### Metal

###### New Features

- GPU Profiling in Metal Debugger is now available for Metal 4. This also requires macOS/iOS/visionOS 26.2 beta 2 or newer.  (136244517)

##### Source Editor

###### Resolved Issues

- Fixed: New installations of Xcode will no longer make themselves the default editor for JSON, YAML, or Markdown files.  (164323314)

##### Storekit

###### Resolved Issues

- Fixed: `SubscriptionStatus.all` returning old `SubscriptionStatus` after a subscription change.  (163505178)

##### Swift Interoperability with Cc++

###### New Features

- You can now annotate C types with the `SWIFT_SHARED_REFERENCE` attribute.  (156056071)
- Retain and release operations for `SWIFT_SHARED_REFERENCE` types can now return an integer type.  (157853183)
- Retain and release operations for `SWIFT_SHARED_REFERENCE` types can now be methods of the type. You can now annotate a C/C++ type with `SWIFT_SHARED_REFERENCE(.doRetain, .doRelease)` to use methods `doRetain` and `doRelease` as the lifetime operations for the type.  (160696723)

##### Testing

###### Resolved Issues

- Fixed: Swift Testing exit tests run correctly when the Swift upcoming “nonisolated(nonsending) By Default” feature (`NonisolatedNonsendingByDefault`) is enabled.  (164424869)

## See Also

- [Xcode 26.1.1 Release Notes](xcode-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.0.1 Release Notes](xcode-26_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26 Release Notes](xcode-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_2-release-notes)*