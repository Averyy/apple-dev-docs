# watchOS 26.1 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 26.1 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 26.1. The SDK comes bundled with Xcode 26.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.1, see [`Xcode 26.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_1-release-notes).

##### Healthkit

###### Resolved Issues

- Fixed: `HKCorrelation` objects of type `.bloodPressure` fail to save with `errorInvalidArgument` HKError code if they don’t have exactly one systolic and one diastolic blood pressure quantity sample its set of objects.  (151889745)
- Fixed: HealthKit authorization UI on watchOS shows separate switches for systolic and diastolic blood pressure, instead of a singular switch like iOS and visionOS.  (159711055)

##### Swiftui

###### Resolved Issues

- Fixed: The `navigationLinkIndicatorVisibility` modifier crashes when run on iOS 17, iOS 18 and aligned releases. You must recompile your app against the 26.1 SDK to receive this fix.  (158236264) (FB19613386)

## See Also

- [watchOS 26.3 Beta Release Notes](watchos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.2 Release Notes](watchos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26 Release Notes](watchos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-26_1-release-notes)*