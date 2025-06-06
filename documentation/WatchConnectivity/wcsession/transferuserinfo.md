# transferUserInfo(_:)

**Framework**: Watchconnectivity  
**Kind**: method

Sends the specified data dictionary to the counterpart.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func transferUserInfo(_ userInfo: [String : Any] = [:]) -> WCSessionUserInfoTransfer
```

#### Return Value

A transfer object that you can use to monitor and cancel the operation.

#### Discussion

Call this method when you want to send a dictionary of data to the counterpart and ensure that it’s delivered. Dictionaries sent using this method are queued on the other device and delivered in the order in which they were sent. After a transfer begins, the transfer operation continues even if the app is suspended.

This method can only be called while the session is active (the [`activationState`](wcsession/activationstate.md) property is set to [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md)). Calling this method for an inactive or deactivated session is a programmer error.

> ⚠️ **Warning**:  Always test Watch Connectivity data transfers on paired devices. The Simulator app doesn’t support the  [`transferUserInfo(_:)`](wcsession/transferuserinfo(_:).md) method.

 Always test Watch Connectivity data transfers on paired devices. The Simulator app doesn’t support the  [`transferUserInfo(_:)`](wcsession/transferuserinfo(_:).md) method.

## Parameters

- `userInfo`: A dictionary of property list values that you want to send. You define the contents of the dictionary that your counterpart supports. This parameter must not be  .

## See Also

- [var outstandingUserInfoTransfers: [WCSessionUserInfoTransfer]](wcsession/outstandinguserinfotransfers.md)
  An array of in-progress data transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/transferuserinfo(_:))*