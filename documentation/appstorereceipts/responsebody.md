# responseBody

**Framework**: App Store Receipts  
**Kind**: dict

The JSON data that returns in the response from the App Store.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

#### Discussion

The [`verifyReceipt`](verifyreceipt.md) endpoint returns this response.

## Topics

### Objects
- [object responseBody.Pending_renewal_info](responsebody/pending_renewal_info.md)
  An array of elements that refers to open or failed auto-renewable subscription renewals.
- [object responseBody.Latest_receipt_info](responsebody/latest_receipt_info.md)
  An array that contains all in-app purchase transactions.
- [object responseBody.Receipt](responsebody/receipt.md)
  The decoded version of the encoded receipt data that you send with the request to the App Store.

## See Also

- [verifyReceipt](verifyreceipt.md)
  Send a receipt to the App Store for verification.
- [object requestBody](requestbody.md)
  The JSON contents you submit with the request to the App Store.
- [object error](error.md)
  Error information that returns in the response body when a request isn’t successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody)*