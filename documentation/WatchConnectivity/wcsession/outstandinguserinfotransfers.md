# outstandingUserInfoTransfers

**Framework**: Watchconnectivity  
**Kind**: property

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

#### Discussion

This property contains the [`WCSessionUserInfoTransfer`](wcsessionuserinfotransfer.md) objects representing the data that you queued using the [`transferUserInfo(_:)`](wcsession/transferuserinfo(_:).md) or [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) methods. Use the objects in this array to cancel specific data transfers.

## See Also

- [func transferUserInfo([String : Any]) -> WCSessionUserInfoTransfer](wcsession/transferuserinfo(_:).md)
  Sends the specified data dictionary to the counterpart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/outstandinguserinfotransfers)*