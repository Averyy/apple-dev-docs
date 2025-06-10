# visionOS 1.2 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 1.2 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 1.2. The SDK comes bundled with Xcode 15.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.4, see [`Xcode 15.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_4-release-notes).

##### Facetime

###### Resolved Issues

- Fixed: Recent calls from an iPhone, iPad, or Apple Watch will not sync to Vision Pro and vice versa.  (125375528)

##### Keyboards

###### Resolved Issues

- Fixed: Trying to access the emoji keyplane from the mini keyboard redirects the user to a letter keyplane with extra platter space.  (125951731)

##### Notifications

###### Known Issues

- Developers might see session interruption notifications that are not relevant to their app.  (125360716)  Developers should filter notifications against their audio session of choice like so: `NotificationCenter.default.addObserver(forName: AVAudioSession.interruptionNotification, object: AVAudioSession.sharedInstance(), queue: nil) { ... }`

##### Storekit

###### Resolved Issues

- Fixed: When testing a compatible iOS or iPadOS app on visionOS, the UI presented from the App Store review request APIs will now render correctly.  (125912511)

## See Also

- [visionOS 1.3 Release Notes](visionos-1_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 1.1 Release Notes](visionos-1_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS Release Notes](visionos-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-1_2-release-notes)*