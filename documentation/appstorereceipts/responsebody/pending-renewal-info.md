# responseBody.Pending_renewal_info

**Framework**: App Store Receipts  
**Kind**: dict

An array of elements that refers to open or failed auto-renewable subscription renewals.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

#### Discussion

In the JSON file, `pending_renewal_info` is an array in which each element contains the pending renewal information for each auto-renewable subscription identified by the `product_id`. A pending renewal may refer to a renewal that the system scheduled in the future or a renewal that failed in the past for some reason.

Use this value to get critical information about any pending renewal transactions for an auto-renewable subscription.

The `pending_renewal_info` array is returned only for app receipts that contain auto-renewable subscriptions. If customers voluntarily cancel a subscription renewal while in the grace period, the App Store pauses billing retry, and removes the transaction from `pending_renewal_info`. The subscription is in the grace period if the key `grace_period_expires_date_ms` is present and the expiration date hasn't passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody/pending_renewal_info)*