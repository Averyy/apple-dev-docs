# auto_renew_status

**Framework**: App Store Receipts  
**Kind**: typealias

The renewal status for the auto-renewable subscription.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
string auto_renew_status
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Pending_renewal_info`](responsebody/pending_renewal_info-data.dictionary.md) array.

The value for this field should not be interpreted as the customer’s subscription status. You can use this value to display an alternative subscription product in your app, such as a lower-level subscription plan to which the user can downgrade from their current plan.

Consider presenting an attractive upgrade or downgrade offer in the same subscription group, if the [`auto_renew_status`](auto_renew_status.md) value is `“0”`. See [`Engineering Subscriptions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/705/) from WWDC 2018 for more information.

## See Also

- [type status](status.md)
  The status of the app receipt.
- [type is_in_billing_retry_period](is_in_billing_retry_period.md)
  An indicator of whether an auto-renewable subscription is in the billing retry period.
- [type is_in_intro_offer_period](is_in_intro_offer_period.md)
  An indicator of whether an auto-renewable subscription is in the introductory price period.
- [type is_trial_period](is_trial_period.md)
  An indicator of whether an auto-renewable subscription is in the free trial period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/auto_renew_status)*