# visionOS 2.2 Release Notes

**Framework**: Visionos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 2.2 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 2.2. The SDK comes bundled with Xcode 16.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.2, see [`Xcode 16.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_2-release-notes).

##### Compatible Apps

###### Known Issues

- In the visionOS Simulator, iOS apps running against the “Apple Vision Pro (Designed for iPad)” target will crash upon launch if they link `ImagePlayground.framework`.  (141228566) (FB16079366)  Apps behave correctly when running on-device. Test directly against Apple Vision Pro hardware.

##### Mac Virtual Display

###### Resolved Issues

- Fixed: Playing videos in Firefox does not work while using Mac Virtual Display with Vision Pro speakers.  (138642255)
- Fixed: If you are not using the default Mac display resolution, the Mac Virtual Display window might get stuck when changing its aspect ratio.  (139087505)

##### Siri

###### Resolved Issues

- Fixed: Siri does not work on the simulator.  (139096339)

##### Swiftui

###### Resolved Issues

- Fixed: Compiling in the Swift 6 language mode might cause an `@Entry` error due to “static property `defaultValue` is not concurrency-safe because non-‘Sendable’ type”.  (133885814)
- Fixed: Views won’t accept dropped directories if [`UTType.directory`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/directory) or [`UTType.fileURL`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/fileurl) are not in the list of accepted content types for drop.  (138158126)

##### Tabletopkit

###### New Features

- Direct manipulation allows a user to pick up equipment up close and move it in a way that naturally follows their hands.  (138592898)
- Local handoff allows a user to hand off equipment from one hand to the other without releasing the equipment.  (138854913)

###### Resolved Issues

- Fixed: The existing API `tabletopGame(_ game, parent, automaticUpdate, interaction)` is erroneously annotated as `@available(visionOS, introduced: 2.2)`, which causes an existing app that uses it to stop compiling, unless the deployment target is bumped to visionOS 2.2.  (139018795)

##### Unity Applications

###### Known Issues

- Some Unity applications might render incorrectly. The content might swim more than expected and appear stretched.  (139384386)  Rebuild with Unity release 1.2.3 or later.

## See Also

- [visionOS 2.5 Release Notes](visionos-2_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.4 Release Notes](visionos-2_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.3 Release Notes](visionos-2_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.1 Release Notes](visionos-2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2 Release Notes](visionos-2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_2-release-notes)*