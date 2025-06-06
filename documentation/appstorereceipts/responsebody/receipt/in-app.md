# responseBody.Receipt.In_app

**Framework**: App Store Receipts  
**Kind**: dict

An array that contains the in-app purchase receipt fields for all in-app purchase transactions.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

#### Discussion

The `in_app` array is not in chronological order. When parsing the array, iterate over all items to ensure all items are fulfilled. For example, you cannot assume that the last item in the array is the most recent.

For receipts containing auto-renewable subscriptions, check the value of the [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info.md) key of the response to get the status of the most recent renewal.

You can use this array to:

- Check for an empty array in a valid receipt, indicating that the App Store has made no in-app purchase charges. 
- Determine which products the user purchased. Purchases for non-consumable products, auto-renewable subscriptions, and non-renewing subscriptions remain in the receipt indefinitely. For consumable products, the transaction is added to the receipt when the purchase is made, and remains until your app finishes that transaction. It no longer appears in updated receipts after you call [`finishTransaction(_:)`](https://developer.apple.com/documentation/storekit/skpaymentqueue/finishtransaction(_:)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody/receipt/in_app)*