# iOS & iPadOS 14.2 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 14.2 SDK provides support to develop apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 14.2. The SDK comes bundled with Xcode 12.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 12.2, see [`Xcode 12.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-12_2-release-notes).

##### Core Media

###### New Features

- Support for multiple concurrent [`AVURLAsset`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset) instances on offline HLS filesystem URLs has been improved.
- You can now use multiple concurrent [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem) objects and other [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) objects on offline HLS assets with completed [`AVMediaSelection`](https://developer.apple.com/documentation/AVFoundation/AVMediaSelection) objects without triggering network reads.
- The progress indicator logic of [`AVMediaSelection`](https://developer.apple.com/documentation/AVFoundation/AVMediaSelection) ordering for [`AVAggregateAssetDownloadTask`](https://developer.apple.com/documentation/AVFoundation/AVAggregateAssetDownloadTask) has been improved. (64551736)

##### Intercom

###### Resolved Issues

- You can now play and reply to Intercom notifications. (70470421)

##### Skadnetwork

###### Known Issues

- To receive a postback from devices running iOS 14 or later, generate signatures using signature version 2.0 or later. Version 1.0 signatures don’t result in a postback on iOS 14 and later, even if the advertised app is installed and launched. (71474331)

## See Also

- [iOS & iPadOS 14.7 Release Notes](ios-ipados-14_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.6 Release Notes](ios-ipados-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5.1 Release Notes](ios-ipados-14_5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5 Release Notes](ios-ipados-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.4 Release Notes](ios-ipados-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.3 Release Notes](ios-ipados-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14 Release Notes](ios-ipados-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-14_2-release-notes)*