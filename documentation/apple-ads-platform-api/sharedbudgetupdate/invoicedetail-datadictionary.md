# SharedBudgetUpdate.InvoiceDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Invoice billing contact details supplied when updating a budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetUpdate.InvoiceDetail
```

#### Discussion

All fields are optional, allowing partial updates to an existing invoice detail record. Only include the fields you want to change.

See [`InvoiceDetailUpdate`](invoicedetailupdate.md) for the full field reference.

## Properties

- `orderNumber` (string): Purchase order number.
- `clientName` (string): Identifies the advertiser or product.
- `primaryBuyerName` (string): Name of the primary buyer.
- `primaryBuyerEmail` (string): Email address of the primary buyer. Must be a valid email address.
- `billingEmail` (string): Billing email address. Must be a valid email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetupdate/invoicedetail-data.dictionary)*