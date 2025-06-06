# remainingComplicationUserInfoTransfers

**Framework**: Watchconnectivity  
**Kind**: property

The number of remaining times you can send complication data from the iOS app to the WatchKit extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var remainingComplicationUserInfoTransfers: Int { get }
```

#### Discussion

The number of remaining times that you can call [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) during the current day. If this property is set to 0, any additional calls to [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) use [`transferUserInfo(_:)`](wcsession/transferuserinfo(_:).md) instead.

If the complication is on the active watch face, you are given 50 transfers a day. If the complication is not active, this property defaults to 0.

## See Also

- [func transferCurrentComplicationUserInfo([String : Any]) -> WCSessionUserInfoTransfer](wcsession/transfercurrentcomplicationuserinfo(_:).md)
  Sends complication-related data from the iOS app to the WatchKit extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/remainingcomplicationuserinfotransfers)*