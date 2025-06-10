# WCSessionUserInfoTransfer

**Framework**: Watch Connectivity  
**Kind**: class

Information about in-progress data transfers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class WCSessionUserInfoTransfer
```

#### Overview

You don’t create instances of this class yourself. When you begin a data transfer, the system creates a new instance of this class for you. Use the created object to monitor or cancel the transfer as needed.

To initiate a file transfer operation, call the [`transferUserInfo(_:)`](wcsession/transferuserinfo(_:).md) or [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) method of your app’s [`WCSession`](wcsession.md) object.

## Topics

### Getting the Transfer Information
- [var isCurrentComplicationInfo: Bool](wcsessionuserinfotransfer/iscurrentcomplicationinfo.md)
  A Boolean indicating whether the data is related to the app’s complication.
- [var userInfo: [String : Any]](wcsessionuserinfotransfer/userinfo.md)
  The data being transferred.
### Managing the Transfer Operation
- [var isTransferring: Bool](wcsessionuserinfotransfer/istransferring.md)
  A Boolean value indicating whether the data is still being transferred.
- [func cancel()](wcsessionuserinfotransfer/cancel.md)
  Cancels the data transfer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class WCSessionFile](wcsessionfile.md)
  Information about a file currently being transferred between an iOS app and WatchKit extension.
- [class WCSessionFileTransfer](wcsessionfiletransfer.md)
  Information about in-progress file transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer)*