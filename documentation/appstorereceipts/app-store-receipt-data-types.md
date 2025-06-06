# App Store receipt data types

**Framework**: App Store Receipts

Data types of objects that return in the receipt.

## Topics

### Transaction identifiers
- [type original_transaction_id](original_transaction_id.md)
  The transaction identifier of the original purchase.
- [type transaction_id](transaction_id.md)
  A unique identifier for a transaction, such as a purchase, restore, or renewal.
- [type app_account_token](app_account_token.md)
  The UUID that an app optionally generates to map a customer’s in-app purchase with its resulting App Store transaction.
### Receipt and subscription status
- [type status](status.md)
  The status of the app receipt.
- [type auto_renew_status](auto_renew_status.md)
  The renewal status for the auto-renewable subscription.
- [type is_in_billing_retry_period](is_in_billing_retry_period.md)
  An indicator of whether an auto-renewable subscription is in the billing retry period.
- [type is_in_intro_offer_period](is_in_intro_offer_period.md)
  An indicator of whether an auto-renewable subscription is in the introductory price period.
- [type is_trial_period](is_trial_period.md)
  An indicator of whether an auto-renewable subscription is in the free trial period.
### Dates and intent
- [type expiration_intent](expiration_intent.md)
  The reason a subscription expires.
- [type cancellation_date_ms](cancellation_date_ms.md)
  The time and date that the App Store refunds a transaction or revokes it from Family Sharing.
- [type expires_date_ms](expires_date_ms.md)
  The time, in milliseconds, a subscription expires or renews.
### Promotions and offers
- [type promotional_offer_id](promotional_offer_id.md)
  The identifier of the promotional offer for an auto-renewable subscription that the user redeems.
- [type offer_code_ref_name](offer_code_ref_name.md)
  The offer-reference name of the subscription offer code that the customer redeems.
### Family Sharing
- [type in_app_ownership_type](in_app_ownership_type.md)
  The relationship of the user with the family-shared purchase to which they have access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/app_store_receipt_data_types)*