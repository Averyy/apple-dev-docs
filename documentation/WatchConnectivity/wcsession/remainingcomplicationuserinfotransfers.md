# remainingComplicationUserInfoTransfers

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSUInteger remainingComplicationUserInfoTransfers;
```

## Discussion

The number of remaining times that you can call [`transferCurrentComplicationUserInfo(_:)`](./transfercurrentcomplicationuserinfo%28_%29.md) during the current day. If this property is set to 0, any additional calls to [`transferCurrentComplicationUserInfo(_:)`](./transfercurrentcomplicationuserinfo%28_%29.md) use [`transferUserInfo(_:)`](./transferuserinfo%28_%29.md) instead.

If the complication is on the active watch face, you are given 50 transfers a day. If the complication is not active, this property defaults to 0.

## See Also

### Updating Complication Data
- [func transferCurrentComplicationUserInfo([String : Any]) -> WCSessionUserInfoTransfer](./transfercurrentcomplicationuserinfo%28_%29.md)
  Sends complication-related data from the iOS app to the WatchKit extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/remainingcomplicationuserinfotransfers)*