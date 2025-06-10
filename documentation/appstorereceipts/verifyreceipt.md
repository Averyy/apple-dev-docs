# verifyReceipt

**Framework**: App Store Receipts  
**Kind**: httpPost

Send a receipt to the App Store for verification.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

#### Discussion

Validating with the App Store requires a secure connection between your app and your server, as well as code on your server to validate the receipt with the App Store. Submit an HTTP POST request with the contents detailed in [`requestBody`](requestbody.md) using the `verifyReceipt` endpoint to verify receipts with the App Store. Use the receipt fields in the [`responseBody`](responsebody.md) to validate app and in-app purchases.

Your server must support the Transport Layer Security (TLS) protocol 1.2 or later to call this endpoint.

For more information about server-side receipt validation, see [`Validating receipts with the App Store`](https://developer.apple.com/documentation/storekit/validating-receipts-with-the-app-store).

##### 3179518

The sandbox URL for verifying receipts is:

```other
POST https://sandbox.itunes.apple.com/verifyReceipt
```

> ❗ **Important**: As a best practice, always call the production URL `https://buy.itunes.apple.com/verifyReceipt` first and proceed to verify with the sandbox URL if you receive a `21007` [`status`](status.md) code. Following this approach ensures that you don’t have to switch between URLs while your app is in testing, in review by App Review, or live in the App Store.

##### 4209023

The `verifyReceipt` endpoint is deprecated. The HTTP header includes the deprecation date, according to [`RFC 8594`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc8594.html).

## Request Body

The JSON contents you submit with the request.

## See Also

- [object requestBody](requestbody.md)
  The JSON contents you submit with the request to the App Store.
- [object responseBody](responsebody.md)
  The JSON data that returns in the response from the App Store.
- [object error](error.md)
  Error information that returns in the response body when a request isn’t successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/verifyreceipt)*