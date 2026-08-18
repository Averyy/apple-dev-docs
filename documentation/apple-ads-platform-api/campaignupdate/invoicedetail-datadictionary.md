# CampaignUpdate.InvoiceDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating the invoice details of a budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignUpdate.InvoiceDetail
```

#### Discussion

To change the billing contact details on an existing Line of Credit invoice record, use this object. Omit a field to leave its current value unchanged.

See [`InvoiceDetailUpdate`](invoicedetailupdate.md) for the full field reference.

## Properties

- `orderNumber` (string): Purchase order number.
- `clientName` (string): Identifies the advertiser or product.
- `primaryBuyerName` (string): Name of the primary buyer.
- `primaryBuyerEmail` (string): Email address of the primary buyer. Must be a valid email address.
- `billingEmail` (string): Billing email address. Must be a valid email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate/invoicedetail-data.dictionary)*