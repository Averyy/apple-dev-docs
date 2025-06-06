# transferCurrentComplicationUserInfo(_:)

**Framework**: Watchconnectivity  
**Kind**: method

Sends complication-related data from the iOS app to the WatchKit extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+

## Declaration

```swift
func transferCurrentComplicationUserInfo(_ userInfo: [String : Any] = [:]) -> WCSessionUserInfoTransfer
```

#### Return Value

A transfer object that you can use to monitor and cancel the operation.

#### Discussion

Call this method when you have new data to send to your complication. Your WatchKit extension can use the data to replace or extend its current timeline entries.

This method can only be called while the session is active (the [`activationState`](wcsession/activationstate.md) property is set to [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md)). Calling this method for an inactive or deactivated session is a programmer error.

> ⚠️ **Warning**:  Always test Watch Connectivity data transfers on paired devices. The Simulator app doesn’t support the [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) method.

 Always test Watch Connectivity data transfers on paired devices. The Simulator app doesn’t support the [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) method.

## Parameters

- `userInfo`: A dictionary of property list values that you want to send. You define the contents of the dictionary that your counterpart supports. This parameter must not be  .

## See Also

- [var remainingComplicationUserInfoTransfers: Int](wcsession/remainingcomplicationuserinfotransfers.md)
  The number of remaining times you can send complication data from the iOS app to the WatchKit extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/transfercurrentcomplicationuserinfo(_:))*