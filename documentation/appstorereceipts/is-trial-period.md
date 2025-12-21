# is_trial_period

**Framework**: App Store Receipts  
**Kind**: typealias

An indicator of whether an auto-renewable subscription is in the free trial period.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
string is_trial_period
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info-data.dictionary.md) and [`responseBody.Receipt.In_app`](responsebody/receipt-data.dictionary/in_app-data.dictionary.md) arrays.

You can use this value to determine whether the specific record is in a subscription trial period. If a previous subscription period in the receipt has the value `"true"` for either the `is_trial_period` or [`is_in_intro_offer_period`](is_in_intro_offer_period.md) keys, the user is not eligible for a free trial or introductory price within that subscription group.

## See Also

- [type status](status.md)
  The status of the app receipt.
- [type auto_renew_status](auto_renew_status.md)
  The renewal status for the auto-renewable subscription.
- [type is_in_billing_retry_period](is_in_billing_retry_period.md)
  An indicator of whether an auto-renewable subscription is in the billing retry period.
- [type is_in_intro_offer_period](is_in_intro_offer_period.md)
  An indicator of whether an auto-renewable subscription is in the introductory price period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/is_trial_period)*