# transaction_id

**Framework**: App Store Receipts  
**Kind**: tdef

A unique identifier for a transaction, such as a purchase, restore, or renewal.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

## Declaration

```swift
string transaction_id
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info.md) and [`responseBody.Receipt.In_app`](responsebody/receipt/in_app.md) arrays.

This value has the same format as the transaction’s [`transactionIdentifier`](https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactionidentifier) property; however, the values may not be the same. 

You can use this value to:

- Manage subscribers in your account database. Store the `transaction_id`, `original_transaction_id`, and `product_id` for each transaction, as a best practice to store transaction records for each customer. App Store generates a new value for `transaction_id` every time the subscription automatically renews or is restored on a new device.
- Differentiate a purchase transaction from a restore or a renewal transaction. In a purchase transaction, the `transaction_id` always matches the `original_transaction_id`. For subscriptions, it indicates the first subscription purchase. For a restore or renewal, the `transaction_id` does not match the `original_transaction_id`. If a user restores or renews the same purchase multiple times, each restore or renewal has a different `transaction_id`.

## See Also

- [type original_transaction_id](original_transaction_id.md)
  The transaction identifier of the original purchase.
- [type app_account_token](app_account_token.md)
  The UUID that an app optionally generates to map a customer’s in-app purchase with its resulting App Store transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/transaction_id)*