# iOS & iPadOS 26.4 Beta Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 26.4 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 26.4 beta. The SDK comes bundled with Xcode 26.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.4, see [`Xcode 26.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_4-release-notes).

##### Background Assets

###### New Features

- You can now check the status of an asset pack while offline by calling `localStatus(ofAssetPackWithID:)` or `assetPackIsAvailableLocally(withID:)` on the shared asset pack manager. The former method returns all available status information. The latter returns only a Boolean value but can be called synchronously. Not all status information is available offline.  (164498466)
- You can make the latest version of an asset pack available locally by calling `ensureLocalAvailability(of:requireLatestVersion:)` on the shared asset pack manager and passing `true` to the `shouldUpdate` parameter.  (166237389)

###### Known Issues

- Apps might crash when downloading asset packs.  (169648111)  If an app crashes due to this issue, then relaunch it. The app should then have local access to the asset pack that it was downloading when it crashed.

##### External Media

###### Known Issues

- HFS external media might fail to mount automatically.  (168672160)  For macOS only, use CLI tool `diskutil mount` to attach the relevant disk device.

##### Feedback

###### Known Issues

- After submitting a crash/panic report, Feedback UI’s close button might become unresponsive.  (170091186)  Locking and unlocking the device helps get out of this state.

##### Memory Integrity Enforcement for Applications

###### New Features

- Applications can now opt in to the full protections of Memory Integrity Enforcement for enhanced memory safety protection. Previously applications were limited to Soft Mode.  (160719439)

##### Messages

###### New Features

- RCS end-to-end encryption is now available for testing in this beta. This feature is not shipping in this release and will be available to customers in a future software update for iOS, iPadOS, macOS, and watchOS. End-to-end encryption is in beta and is not available for all devices or carriers. Conversations labeled as encrypted are encrypted end-to-end, so messages can’t be read while they’re sent between devices. In this beta, RCS encryption is available for testing between Apple devices and is not yet testable with other platforms.  (170160585)

##### Networking

###### Resolved Issues

- Fixed: Multiple processes leak `CFRunLoopSource` objects when Automatic proxy configuration (PAC) or Auto proxy discovery are configured. For clients of the `CFNetworkExecuteProxyAutoConfigurationURL` and `CFNetworkExecuteProxyAutoConfigurationScript` API, please check to make sure your process is not working around the leak by overreleasing the `CFRunLoopSourceRef` returned by those functions or the `CFArrayRef` and `CFErrorRef` passed to the completion.  (166839810) (FB21376045)

##### Reality Composer

###### Known Issues

- Reality Composer iOS can no longer export projects as `.reality` or USDZ. Opening export menu results in an empty panel.  (170091896)

##### Storekit

###### New Features

- New fields [`revocationType`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property) and [`revocationPercentage`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationpercentage) have been added to [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction).  (148858551)

##### Swiftui

###### Resolved Issues

- Fixed: SwiftUI does not surface the latest `.userActivity` as the current user activity.  (163136831)

###### Known Issues

- Multiple implicit SwiftUI animations (triggered by `RealityViewContent.animate` or `Entity.animate`) that modify a RealityKit component’s properties, are combined only when the implicit animations target the same set of component properties. For example, if you initiate an implicit animation on Transform.scale and then initiate an implicit animation on Transform.scale and Transform.translation then the animations affecting the scale property will be independent of each other, and will not combine. In this case, the most recently initiated animation will overwrite the scale property.  (169723142)  Ensure the same component properties are animated by subsequent implicit animations when possible.

##### Uikit

###### Resolved Issues

- Fixed: KeyboardNotification might not send.  (165479264)

## See Also

- [iOS & iPadOS 26.3 Release Notes](ios-ipados-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26.2 Release Notes](ios-ipados-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26.1 Release Notes](ios-ipados-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26 Release Notes](ios-ipados-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_4-release-notes)*