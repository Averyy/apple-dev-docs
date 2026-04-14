# macOS Tahoe 26.4 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 26.4 SDK provides support to develop apps for Mac computers running Tahoe 26.4. The SDK comes bundled with Xcode 26.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.4, see [`Xcode 26.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_4-release-notes).

##### Address Sanitizer

###### Known Issues

- Address Sanitizer and Thread Sanitizer might hang on macOS 26.4, iOS 26.4, tvOS 26.4, watchOS 26.4, and visionOS 26.4 when building with Xcode 26.3 or older.  (171762808) **Workaround:** Use Xcode 26.4 when testing applications with Address Sanitizer or Thread Sanitizer.

##### Appkit

###### Resolved Issues

- Fixed: Window resize pointer does not follow the window’s corner shape.  (149726089)

##### Background Assets

###### New Features

- You can now check the status of an asset pack while offline by calling `localStatus(ofAssetPackWithID:)` or `assetPackIsAvailableLocally(withID:)` on the shared asset pack manager. The former method returns all available status information. The latter returns only a Boolean value but can be called synchronously. Not all status information is available offline.  (164498466)
- You can make the latest version of an asset pack available locally by calling `ensureLocalAvailability(of:requireLatestVersion:)` on the shared asset pack manager and passing `true` to the `shouldUpdate` parameter.  (166237389)

###### Resolved Issues

- Fixed: Setting a URL override could break apps from the App Store that use Apple-Hosted Background Assets.  (169558509)
- Fixed: Apps might crash when downloading asset packs.  (169648111)

##### Coremidi

###### New Features

- Audio MIDI Setup now supports Network MIDI 2.0 sessions in the redesigned MIDI Network Setup panel. You can create MIDI 2.0 connections over your local network using UDP transport for Universal MIDI Packets, enabling both Legacy MIDI and MIDI 2.0 protocol communication. Network MIDI 2.0 sessions appear alongside existing RTP MIDI sessions and support automatic device discovery through mDNS and data integrity features for reliable wireless performance.  (118728162)

##### External Boot

###### Known Issues

- When installing an external disk, some configurations of M1 Apple Silicon Macs might panic at boot.   (170263142) **Workaround:** Install to a secondary volume in APFS container instead of external disk to validate secondary boot sequences.

##### External Media

###### Resolved Issues

- Fixed: HFS external media might fail to mount automatically.  (168672160)

##### Fskit

###### Known Issues

- The availability version for `FSVolume.MountOptions` and for the property `FSVolume.requestedMountOptions` is incorrect. These symbols are available starting in macOS 26.4.  (171914656)

##### Installation

###### Resolved Issues

- Fixed: Install macOS Tahoe Beta.app does not work on versions of macOS prior to 15.0.  (170997618)

##### Internet Accounts

###### Known Issues

- Exchange syncing for Calendar, Reminders and Notes might fail.  (168082477) **Workaround:** To continue syncing Calendar and Reminders, disable Notes syncing in Internet Accounts.

##### Login

###### Resolved Issues

- Fixed: Touch ID might not be available to unlock the screen of a standard user account after updating to this release. This occurs when FileVault is enabled and a standard user account is logged in prior to any administrator logging in following the update.  (169743642)

##### Macos Recovery

###### Known Issues

- When deleting a boot volume from the Activation Lock window in macOS Recovery, full erase functionality might not work.   (170280070) **Workaround:** Use the “Erase All Content and Settings” functionality from the booted OS instead of triggering from recovery.

##### Networking

###### Resolved Issues

- Fixed: Multiple processes leak `CFRunLoopSource` objects when Automatic proxy configuration (PAC) or Auto proxy discovery are configured. For clients of the `CFNetworkExecuteProxyAutoConfigurationURL` and `CFNetworkExecuteProxyAutoConfigurationScript` API, please check to make sure your process is not working around the leak by overreleasing the `CFRunLoopSourceRef` returned by those functions or the `CFArrayRef` and `CFErrorRef` passed to the completion.  (166839810) (FB21376045)

##### Printing

###### Known Issues

- Jobs and Printer Status might not be reflected in Print Center.  (171264258)

##### Resource Fork

###### Resolved Issues

- On macOS 26.4 and later, file systems that do not natively support extended attributes restrict partial writes to the first 286 bytes of the resource fork extended attribute (com.apple.ResourceFork). To modify the resource fork, replace the entire 286-byte range, or write beyond the 286-byte offset.  (156896699)

##### Rosetta

###### Deprecations

- As announced at WWDC in 2025, macOS Tahoe 26 is the last release to support Intel based Macs. Additionally, Rosetta support for apps will end after macOS 27. Starting in macOS Tahoe 26.4, users will be notified when they launch apps that use Rosetta of the upcoming incompatibility. During the beta period, the cadence of notifications will be accelerated, enabling Apple and developers to address any issues that might occur. There will continue to be support for older, unmaintained gaming titles leveraging Rosetta along with software running Intel binaries in Linux VMs. Organizations using a device management service can control the notification experience with the `allowRosettaUsageAwareness` key.  (169228455)

##### Storekit

###### New Features

- New fields [`revocationType`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property) and [`revocationPercentage`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationpercentage) have been added to [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction).  (148858551)

###### Resolved Issues

- Fixed: Purchase Intents might not be emitted from the intents sequence when the app is launched from the background.  (168958783) (FB21767675)

##### Swiftui

###### Resolved Issues

- Fixed: SwiftUI does not surface the latest `.userActivity` as the current user activity.  (163136831)
- Fixed: On macOS, a non-opaque window that hosts glass content will correctly update the backdrop content behind the glass even if the window is inactive.  (166828089) (FB21375029)

###### Known Issues

- Multiple implicit SwiftUI animations (triggered by `RealityViewContent.animate` or `Entity.animate`) that modify a RealityKit component’s properties, are combined only when the implicit animations target the same set of component properties. For example, if you initiate an implicit animation on Transform.scale and then initiate an implicit animation on Transform.scale and Transform.translation then the animations affecting the scale property will be independent of each other, and will not combine. In this case, the most recently initiated animation will overwrite the scale property.  (169723142) **Workaround:** Ensure the same component properties are animated by subsequent implicit animations when possible.

##### Virtualization

###### Resolved Issues

- Fixed: On certain hardware configurations, new macOS Tahoe virtual machine installations may boot to a black screen.  (169654019)

## See Also

- [macOS Tahoe 26.5 Beta 2 Release Notes](macos-26_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26.3 Release Notes](macos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26.2 Release Notes](macos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26.1 Release Notes](macos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26 Release Notes](macos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-26_4-release-notes)*