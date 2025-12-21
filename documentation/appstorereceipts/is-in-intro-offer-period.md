# is_in_intro_offer_period

**Framework**: App Store Receipts  
**Kind**: typealias

An indicator of whether an auto-renewable subscription is in the introductory price period.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
string is_in_intro_offer_period
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info-data.dictionary.md) and [`responseBody.Receipt.In_app`](responsebody/receipt-data.dictionary/in_app-data.dictionary.md) arrays.

You can use this value to determine if the user is eligible for introductory pricing. If a previous subscription period in the receipt has the value `“true”` for either the [`is_trial_period`](is_trial_period.md) or `is_in_intro_offer_period` keys, the user is not eligible for a free trial or introductory price within that subscription group. For more information, see [`Implementing introductory offers in your app`](https://developer.apple.com/documentation/StoreKit/implementing-introductory-offers-in-your-app).

## See Also

- [type status](status.md)
  The status of the app receipt.
- [type auto_renew_status](auto_renew_status.md)
  The renewal status for the auto-renewable subscription.
- [type is_in_billing_retry_period](is_in_billing_retry_period.md)
  An indicator of whether an auto-renewable subscription is in the billing retry period.
- [type is_trial_period](is_trial_period.md)
  An indicator of whether an auto-renewable subscription is in the free trial period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/is_in_intro_offer_period)*