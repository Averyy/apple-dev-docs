# WCSessionFileTransfer

**Framework**: Watchconnectivity  
**Kind**: class

Information about in-progress file transfers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class WCSessionFileTransfer
```

#### Overview

You do not create instances of this class yourself. When you initiate a file transfer, the system creates a new file transfer object to represent the transferred file. Use that object to get the file information or to cancel the transfer as needed.

To initiate a file transfer operation, call the [`transferFile(_:metadata:)`](wcsession/transferfile(_:metadata:).md) method of your app’s [`WCSession`](wcsession.md) object.

## Topics

### Getting the File Information
- [var file: WCSessionFile](wcsessionfiletransfer/file.md)
  The file being transferred.
### Managing the File Transfer
- [var isTransferring: Bool](wcsessionfiletransfer/istransferring.md)
  A Boolean value indicating whether the file is still being transferred.
- [var progress: Progress](wcsessionfiletransfer/progress.md)
  An object that tracks the progress of the file transfer.
- [func cancel()](wcsessionfiletransfer/cancel.md)
  Cancels the file transfer.

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

- [class WCSessionFile](wcsessionfile.md)
  Information about a file currently being transferred between an iOS app and WatchKit extension.
- [class WCSessionUserInfoTransfer](wcsessionuserinfotransfer.md)
  Information about in-progress data transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer)*