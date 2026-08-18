# CampaignCreate.InvoiceDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Invoice billing contact details supplied when creating a campaign or budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignCreate.InvoiceDetail
```

#### Discussion

Supply these contact and reference details when creating a campaign or budget order on a Line of Credit account. Line of Credit accounts require this object. Pay As You Go accounts can omit it.

`clientName` and `orderNumber` are required for agency-type accounts.

See [`InvoiceDetailCreate`](invoicedetailcreate.md) for the full field reference.

## Properties

- `primaryBuyerName` (string) *(required)*: Name of the primary buyer.
- `primaryBuyerEmail` (string) *(required)*: Email address of the primary buyer. Must be a valid email address.
- `billingEmail` (string) *(required)*: Billing email address. Must be a valid email address.
- `clientName` (string): Identifies the advertiser or product.
- `orderNumber` (string): Purchase order number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/invoicedetail-data.dictionary)*