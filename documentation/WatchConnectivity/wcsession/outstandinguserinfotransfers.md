# outstandingUserInfoTransfers

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

An array of in-progress data transfers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outstandingUserInfoTransfers: [WCSessionUserInfoTransfer] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<WCSessionUserInfoTransfer *> * outstandingUserInfoTransfers;
```

#### Discussion

This property contains the [`WCSessionUserInfoTransfer`](../wcsessionuserinfotransfer.md) objects representing the data that you queued using the [`transferUserInfo(_:)`](./transferuserinfo%28_%29.md) or [`transferCurrentComplicationUserInfo(_:)`](./transfercurrentcomplicationuserinfo%28_%29.md) methods. Use the objects in this array to cancel specific data transfers.

## See Also

### Transferring Data in the Background
- [func transferUserInfo([String : Any]) -> WCSessionUserInfoTransfer](./transferuserinfo%28_%29.md)
  Sends the specified data dictionary to the counterpart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/outstandinguserinfotransfers)*