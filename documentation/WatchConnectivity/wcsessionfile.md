# WCSessionFile

**Framework**: Watch Connectivity  
**Kind**: class

Information about a file currently being transferred between an iOS app and WatchKit extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class WCSessionFile
```

#### Overview

You do not create instances of this class directly. When you initiate a file transfer using the [`transferFile(_:metadata:)`](wcsession/transferfile(_:metadata:).md)  method of your app’s [`WCSession`](wcsession.md) object, the session creates an instance when it queues the file for transfer. You can get a list of in-progress transfers initiated by your app from the session’s [`outstandingFileTransfers`](wcsession/outstandingfiletransfers.md) property. When a file is received by your app, the corresponding file object is delivered directly to your session’s delegate.

The file object includes the URL of the file on the local system and an optional dictionary of keys and values that accompany the file.

## Topics

### Getting the File Information
- [var fileURL: URL](wcsessionfile/fileurl.md)
  The URL of the file that was received.
- [var metadata: [String : Any]?](wcsessionfile/metadata.md)
  A dictionary of additional information that was sent with the file.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WCSessionFileTransfer](wcsessionfiletransfer.md)
  Information about in-progress file transfers.
- [class WCSessionUserInfoTransfer](wcsessionuserinfotransfer.md)
  Information about in-progress data transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile)*