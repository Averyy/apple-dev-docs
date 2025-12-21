# original_transaction_id

**Framework**: App Store Receipts  
**Kind**: typealias

The transaction identifier of the original purchase.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
string original_transaction_id
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Pending_renewal_info`](responsebody/pending_renewal_info-data.dictionary.md), [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info-data.dictionary.md), and [`responseBody.Receipt.In_app`](responsebody/receipt-data.dictionary/in_app-data.dictionary.md) arrays.

This value is identical to the [`transaction_id`](transaction_id.md) except when the user restores a purchase or renews a subscription. This value has the same format as the transaction’s `transactionIdentifier` property; however, the values may not be the same. For auto-renewable subscription transactions, this value also appears in the `pending_renewal_info` key of the JSON response.

You can use this value to:

- Match a transaction found in the receipt to a server-to-server notification event. For more information, see [`Enabling App Store Server Notifications`](https://developer.apple.com/documentation/StoreKit/enabling-app-store-server-notifications).
- Manage auto-renewable subscriptions. Store this value, `product_id`, `expires_date_ms`, and `purchase_date_ms` for each transaction for each customer, as a best practice.
- Identify a subscription with the `product_id` in the `pending_renewal_info` section. Do not rely on the `original_transaction_id` value on its own. Treat this purchase as a new subscription when you see a new `original_transaction_id` value for a `product_id`.
- Differentiate a purchase transaction from a restore or a renewal transaction. In a purchase transaction, the `transaction_id` always matches the `original_transaction_id`. For subscriptions, it indicates the first subscription purchase. For a restore or renewal, the `transaction_id` does not match the `original_transaction_id`.
- Identify one or more renewals for the same subscription.

## See Also

- [type transaction_id](transaction_id.md)
  A unique identifier for a transaction, such as a purchase, restore, or renewal.
- [type app_account_token](app_account_token.md)
  The UUID that an app optionally generates to map a customer’s in-app purchase with its resulting App Store transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/original_transaction_id)*