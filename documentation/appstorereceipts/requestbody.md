# requestBody

**Framework**: App Store Receipts  
**Kind**: dict

The JSON contents you submit with the request to the App Store.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

#### Discussion

To receive a decoded receipt for validation, send a request with the encoded receipt data and app password to the App Store. For receipts that contain auto-renewable subscriptions, optionally include an exclusion flag. Send this JSON data using the HTTP POST request method.

## See Also

- [verifyReceipt](verifyreceipt.md)
  Send a receipt to the App Store for verification.
- [object responseBody](responsebody.md)
  The JSON data that returns in the response from the App Store.
- [object error](error.md)
  Error information that returns in the response body when a request isn’t successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/requestbody)*