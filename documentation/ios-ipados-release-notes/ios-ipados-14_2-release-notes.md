# iOS & iPadOS 14.2 Release Notes

**Framework**: iOS & iPadOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The iOS & iPadOS 14.2 SDK provides support to develop apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 14.2. The SDK comes bundled with Xcode 12.2. For information on the compatibility requirements for Xcode 12.2, see [Xcode 12.2 Release Notes](../Xcode-Release-Notes/xcode-12_2-release-notes.md).

### Core Media

#### New Features

- Support for multiple concurrent [`AVURLAsset`](../AVFoundation/avurlasset.md) instances on offline HLS filesystem URLs has been improved.
- You can now use multiple concurrent [`AVPlayerItem`](../AVFoundation/avplayeritem.md) objects and other [AVFoundation](../AVFoundation/AVFoundation.md) objects on offline HLS assets with completed [`AVMediaSelection`](../AVFoundation/avmediaselection.md) objects without triggering network reads.
- The progress indicator logic of [`AVMediaSelection`](../AVFoundation/avmediaselection.md) ordering for [`AVAggregateAssetDownloadTask`](../AVFoundation/avaggregateassetdownloadtask.md) has been improved. (64551736)

### Intercom

#### Resolved Issues

- You can now play and reply to Intercom notifications. (70470421)

### SKAdNetwork

#### Known Issues

- To receive a postback from devices running iOS 14 or later, generate signatures using signature version 2.0 or later. Version 1.0 signatures don’t result in a postback on iOS 14 and later, even if the advertised app is installed and launched. (71474331)

## See Also

### iOS & iPadOS 14
- [iOS & iPadOS 14.7 Release Notes](./ios-ipados-14_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.6 Release Notes](./ios-ipados-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5.1 Release Notes](./ios-ipados-14_5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5 Release Notes](./ios-ipados-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.4 Release Notes](./ios-ipados-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.3 Release Notes](./ios-ipados-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14 Release Notes](./ios-ipados-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-14_2-release-notes)*