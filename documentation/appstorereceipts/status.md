# status

**Framework**: App Store Receipts  
**Kind**: typealias

The status of the app receipt.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
int status
```

#### Discussion

The [`verifyReceipt`](verify-receipt.md) endpoint returns this field in the JSON response, [`responseBody`](responsebody.md).

The value for `status` is `0` if the receipt is valid, or a status code if there’s an error. The status code reflects the status of the app receipt as a whole. For example, if you send a valid app receipt that contains an expired subscription, the response is `0` because the receipt is valid.

Status codes `21100–21199` are various internal data access errors.

## See Also

- [type auto_renew_status](auto_renew_status.md)
  The renewal status for the auto-renewable subscription.
- [type is_in_billing_retry_period](is_in_billing_retry_period.md)
  An indicator of whether an auto-renewable subscription is in the billing retry period.
- [type is_in_intro_offer_period](is_in_intro_offer_period.md)
  An indicator of whether an auto-renewable subscription is in the introductory price period.
- [type is_trial_period](is_trial_period.md)
  An indicator of whether an auto-renewable subscription is in the free trial period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/status)*