# iOS & iPadOS 26.1 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 26.1 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 26.1. The SDK comes bundled with Xcode 26.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.1, see [`Xcode 26.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_1-release-notes).

##### Airdrop

###### Resolved Issues

- Fixed: The AirDrop icon in the iOS share sheet has some visual defects at the corners.  (158979986)

##### Background Assets

###### Resolved Issues

- Fixed: `AssetPackManager.url(for:)` unexpectedly throws an error when looking up the URL for a locally available asset file.  (157959878) (FB19512759)

##### Game Controller

###### Resolved Issues

- Fixed: The time returned by `GCPressedStateInput.lastPressedStateTimestamp` is not in the correct time domain.  (159124910)

##### Healthkit

###### New Features

- HealthKit authorization UI now displays a single Blood Pressure switch to control changes to Systolic and Diastolic Blood Pressure type authorizations. The API is unchanged and apps should request for both types in code.  (153579893)

###### Resolved Issues

- Fixed: `HKCorrelation` objects of type `.bloodPressure` fail to save with `errorInvalidArgument` HKError code if they don’t have exactly one systolic and one diastolic blood pressure quantity sample its set of objects.  (151889745)

##### Instruments

###### Resolved Issues

- Fixed: Processor Trace Instrument doesn’t allow for recording on iPhone 17 family of devices.  (161440613)

##### Keyboard

###### Resolved Issues

- Fixed: You are unable to select diacritical marks and character variants with keyboard. The base character is inserted instead of the intended variant.  (159398021)

##### Lock Screen

###### Resolved Issues

- Fixed: Devices might sleep unexpectedly while using certain apps on the Lock Screen (Calculator, Timer, Notes).  (162150524)

##### Nearbyinteraction

###### New Features

- `NINearbyAccessoryConfiguration` now supports additional UWB parameters such as hopping mode.  (157879907)

###### Known Issues

- Running an `NISession` with an `NIDLTDOAConfiguration` results in an error.  (151352056)

##### Siri

###### Resolved Issues

- Fixed: Questions related to News in Portuguese might fall back to Web search or ChatGPT.  (153935878)

###### Known Issues

- Siri Voice preview might default to legacy pt-BR voices, rather than new pt-PT options.  (155929981)  Select Voice 2 as your new Siri voice. Ask Siri a question, and you will hear the new pt-PT offering.
- The initial pt-PT Siri Voices have pronunciation and word stress issues. Your feedback is appreciated.  (160205691)

##### Swiftui

###### New Features

- `@Animatable` macro is now available starting with iOS 13, macOS 10.15, tvOS 13, and watchOS 6.  (158895616)

###### Resolved Issues

- Fixed: Buttons that do not specify an explicit label display text instead of a symbol in toolbars.  (157671221)
- Fixed: The `navigationLinkIndicatorVisibility` modifier crashes when run on iOS 17, iOS 18 and aligned releases. You must recompile your app against the 26.1 SDK to receive this fix.  (158236264) (FB19613386)

###### Known Issues

- On iOS and iPadOS, `@FocusState` doesn’t work in `safeAreaBar`.  (158720838)

##### Uikit

###### Resolved Issues

- UIDocument was incorrectly annotated to be main actor only. This has been corrected. As a result you might see new warnings or errors show up in your Swift code using UIDocument.  (149990945)

##### Webkit

###### Known Issues

- WebKit outputs a crash stacktrace to `stderr` when `decidePolicyFor navigationAction` returns `.cancel`.  (156957269)  This trace does not represent a bug in the application, and can be safely ignored.

## See Also

- [iOS & iPadOS 26.3 Beta Release Notes](ios-ipados-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26.2 Release Notes](ios-ipados-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26 Release Notes](ios-ipados-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_1-release-notes)*