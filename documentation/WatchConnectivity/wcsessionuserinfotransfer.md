# WCSessionUserInfoTransfer

**Framework**: Watch Connectivity  
**Kind**: class  
**Role**: Class

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

```objc
@interface WCSessionUserInfoTransfer : NSObject
```

#### Overview

You don’t create instances of this class yourself. When you begin a data transfer, the system creates a new instance of this class for you. Use the created object to monitor or cancel the transfer as needed.

To initiate a file transfer operation, call the [`transferUserInfo(_:)`](./wcsession/transferuserinfo%28_%29.md) or [`transferCurrentComplicationUserInfo(_:)`](./wcsession/transfercurrentcomplicationuserinfo%28_%29.md) method of your app’s [`WCSession`](./wcsession.md) object.

## Topics

### Getting the Transfer Information
- [var isCurrentComplicationInfo: Bool](./wcsessionuserinfotransfer/iscurrentcomplicationinfo.md)
  A Boolean indicating whether the data is related to the app’s complication.
- [var userInfo: [String : Any]](./wcsessionuserinfotransfer/userinfo.md)
  The data being transferred.
### Managing the Transfer Operation
- [var isTransferring: Bool](./wcsessionuserinfotransfer/istransferring.md)
  A Boolean value indicating whether the data is still being transferred.
- [func cancel()](./wcsessionuserinfotransfer/cancel%28%29.md)
  Cancels the data transfer.
### Initializers
- [init?(coder: NSCoder)](./wcsessionuserinfotransfer/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Data Objects
- [class WCSessionFile](./wcsessionfile.md)
  Information about a file currently being transferred between an iOS app and WatchKit extension.
- [class WCSessionFileTransfer](./wcsessionfiletransfer.md)
  Information about in-progress file transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer)*