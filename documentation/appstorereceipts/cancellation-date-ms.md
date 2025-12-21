# cancellation_date_ms

**Framework**: App Store Receipts  
**Kind**: typealias

The time and date that the App Store refunds a transaction or revokes it from Family Sharing.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
string cancellation_date_ms
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info-data.dictionary.md) and [`responseBody.Receipt.In_app`](responsebody/receipt-data.dictionary/in_app-data.dictionary.md) arrays.

This field represents the time and date the App Store refunded a transaction or revoked it from family sharing, in UNIX epoch time format, in milliseconds. This field is only present for purchases that Apple refunded or revoked. Use this time format for processing dates.

A canceled in-app purchase remains in the receipt indefinitely. This value is present only if the refund or revocation was for a non-consumable product, an auto-renewable subscription, or a non-renewing subscription.

Use this value to determine whether to stop providing the content associated with the purchase.

## See Also

- [type expiration_intent](expiration_intent.md)
  The reason a subscription expires.
- [type expires_date_ms](expires_date_ms.md)
  The time, in milliseconds, a subscription expires or renews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/cancellation_date_ms)*