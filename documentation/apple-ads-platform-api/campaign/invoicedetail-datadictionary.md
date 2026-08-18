# Campaign.InvoiceDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Invoice details for the LOC payment model.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Campaign.InvoiceDetail
```

#### Discussion

Captures the billing contact and reference information required for Line of Credit (`LOC`) payment model accounts. `primaryBuyerEmail` and `billingEmail` must each be a valid email address.

See [`InvoiceDetailCreate`](invoicedetailcreate.md) for which fields are required when creating a new record, and [`InvoiceDetailUpdate`](invoicedetailupdate.md) for update behavior.

## Properties

- `clientName` (string): Identifies the advertiser or product. Nullable. Mutable.
- `primaryBuyerName` (string): Name of the primary buyer. Mutable.
- `primaryBuyerEmail` (string): Email address of the primary buyer. Must be a valid email address. Mutable.
- `orderNumber` (string): Purchase order number. Typically a PO number. Nullable. Mutable.
- `billingEmail` (string): Billing email address. Must be a valid email address. Mutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/invoicedetail-data.dictionary)*