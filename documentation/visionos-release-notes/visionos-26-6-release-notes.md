# visionOS 26.6 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 26.6 SDK provides support to develop apps for Apple Vision Pro devices running visionOS 26.6. The SDK comes bundled with Xcode 26.6, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.6, see [`Xcode 26.6 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_6-release-notes).

##### Healthkit

###### Resolved Issues

- Fixed: Authorization screen not displaying when requesting `HKQuantityTypeIdentifierBloodPressureDiastolic` or `HKQuantityTypeIdentifierBloodPressureSystolic`.  (177652061)
- Fixed: Temporally-weighted average statistics queries for discrete quantity types such as Resting Heart Rate may return erroneously high values when samples overlap in time.  (178157672)

##### Storekit

###### Resolved Issues

- Fixed: `SKTestSessions` does not properly connect to the test environment when using Simulator, causing test actions to fail.  (174738526) (FB22500243)

## See Also

- [visionOS 26.5 Release Notes](visionos-26_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.4 Release Notes](visionos-26_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.3 Release Notes](visionos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.2 Release Notes](visionos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.1 Release Notes](visionos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26 Release Notes](visionos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_6-release-notes)*