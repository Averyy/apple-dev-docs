# App Store Receipts

**Framework**: App Store Receipts

Validate app and In-App Purchase receipts with the App Store.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

#### Overview

> ❗ **Important**: The [`verifyReceipt`](verifyreceipt.md) endpoint is deprecated. To validate receipts on your server, follow the steps in [`Validating receipts on the device`](validating_receipts_on_the_device.md) on your server. 

The [`verifyReceipt`](verifyreceipt.md) endpoint is deprecated. To validate receipts on your server, follow the steps in [`Validating receipts on the device`](validating_receipts_on_the_device.md) on your server. 

Your server can access the [`verifyReceipt`](verifyreceipt.md) endpoint to validate app and in-app transaction receipts. Submit a receipt to the App Store with your [`shared secret`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts) to receive a JSON response containing the app information and in-app purchase details in the fields that make up the receipt. Each field or combination of fields provides insight you can use to deliver service and content to the user, as you define. 

In-app transactions that your app doesn’t mark as finished using [`finishTransaction(_:)`](https://developer.apple.com/documentation/storekit/skpaymentqueue/finishtransaction(_:)) or [`finish()`](https://developer.apple.com/documentation/storekit/transaction/finish()) remain in the App Store receipt. Auto-renewable subscriptions, non-renewing subscriptions, and non-consumables remain in the receipt indefinitely, and appear in the customer transaction history when you call the [`Get Transaction History V1`](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history-v1) endpoint.

The [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info.md) object for auto-renewable subscriptions can grow over time because the renewal transactions stay in the receipt indefinitely. To optimize performance, the App Store may truncate receipts in the sandbox environment to remove old transactions. 

You can test validating receipts in the sandbox environment. For more information, see [`Testing In-App Purchases with sandbox`](https://developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox) and [`Test in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases-main/test-in-app-purchases).

You can validate receipts from the App Store using server-side receipt validation or on-device validation. For more information about receipt validation options, see [`Choosing a receipt validation technique`](https://developer.apple.com/documentation/storekit/choosing-a-receipt-validation-technique).

> **Note**: Session 110404: [`Implement proactive in-app purchase restore`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/110404/).

Session 110404: [`Implement proactive in-app purchase restore`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/110404/).

## Topics

### Receipt data 
- [App Store receipt data types](app_store_receipt_data_types.md)
  Data types of objects that return in the receipt.
### Local receipt validation
- [Validating receipts on the device](validating_receipts_on_the_device.md)
  Verify the contents of app receipts by decoding and parsing the receipt on the device.
### Deprecated
- [verifyReceipt](verifyreceipt.md)
  Send a receipt to the App Store for verification.
- [object requestBody](requestbody.md)
  The JSON contents you submit with the request to the App Store.
- [object responseBody](responsebody.md)
  The JSON data that returns in the response from the App Store.
- [object error](error.md)
  Error information that returns in the response body when a request isn’t successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts)*