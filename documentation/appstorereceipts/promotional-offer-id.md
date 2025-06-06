# promotional_offer_id

**Framework**: App Store Receipts  
**Kind**: tdef

The identifier of the promotional offer for an auto-renewable subscription that the user redeems.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

## Declaration

```swift
string promotional_offer_id
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info.md) and [`responseBody.Receipt.In_app`](responsebody/receipt/in_app.md) arrays.

You provide this value in the Promotional Offer Identifier field when you create the promotional offer in App Store Connect. For more information, see [`Set up promotional offers for auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev16dfca448).

You can use the promotional offer ID value to:

- Confirm that the sale of the subscription was from a promotional offer.
- Confirm which promotional offer the user redeemed.
- Keep track of the promotional offers that a user has redeemed to limit discounts you offer, according to your business model.

For more information on promotional offers, see [`Implementing promotional offers in your app`](https://developer.apple.com/documentation/storekit/implementing-promotional-offers-in-your-app).

## See Also

- [type offer_code_ref_name](offer_code_ref_name.md)
  The offer-reference name of the subscription offer code that the customer redeems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/promotional_offer_id)*