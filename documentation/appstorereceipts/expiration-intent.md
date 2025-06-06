# expiration_intent

**Framework**: App Store Receipts  
**Kind**: tdef

The reason a subscription expires.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

## Declaration

```swift
string expiration_intent
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Pending_renewal_info`](responsebody/pending_renewal_info.md) array.

You can use this value to do the following:

- If the value is `"1"`, decide whether to survey the subscribers who have opted in to an account on your system or show alternative subscription products within the same group. Decide whether to present a subscription offer to win back the user.
- If the value is `"2"`, decide whether to show the same or alternative subscription products because the user didn't actively make the choice to unsubscribe. 

For more information, see [`Engineering Subscriptions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/705/) from WWDC 2018 and [`Implementing promotional offers in your app`](https://developer.apple.com/documentation/storekit/implementing-promotional-offers-in-your-app).

## See Also

- [type cancellation_date_ms](cancellation_date_ms.md)
  The time and date that the App Store refunds a transaction or revokes it from Family Sharing.
- [type expires_date_ms](expires_date_ms.md)
  The time, in milliseconds, a subscription expires or renews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/expiration_intent)*