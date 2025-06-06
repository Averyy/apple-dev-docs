# iOS & iPadOS 17.6 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 17.5 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 17.6. The SDK comes bundled with Xcode 15.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.4, see [`Xcode 15.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_4-release-notes).

##### Audio

###### Resolved Issues

- Fixed: Some bluetooth headphones might not be usable as an audio output route with certain AVAudioSession configurations.  (129624040)

##### Camera and Avfoundation Capture

###### Resolved Issues

- Fixed: `AVCaptureDeviceRotationCoordinator` returns incorrect values for `videoRotationAngleForHorizonLevelCapture` and `videoRotationAngleForHorizonLevelPreview` when using the Front Camera on iPad Air (6th generation) and iPad Pro (7th generation).  (126887983)

##### Marketplacekit

###### Resolved Issues

- Fixed an issue where user notification fails to display when an app, with an expired license and installed from a marketplace, fails to launch.  (129306666)
- Fixed an issue where reinstalling an offloaded app from a marketplace might get stuck with a disabled home screen icon.  (130278683)

##### Notes

###### Known Issues

- For devices running iOS 17.6 betas 2 or 3, the Notes folder widget might display “No Folder Available”, and tapping on this widget might cause Notes to crash.  (131921810)  Remove the Notes folder widget and re-add it, or update device to iOS 17.6 beta 4.

## See Also

- [iOS & iPadOS 17.5 Release Notes](ios-ipados-17_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.4 Release Notes](ios-ipados-17_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.3 Release Notes](ios-ipados-17_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.2 Release Notes](ios-ipados-17_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.1 Release Notes](ios-ipados-17_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17 Release Notes](ios-ipados-17-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-17_6-release-notes)*