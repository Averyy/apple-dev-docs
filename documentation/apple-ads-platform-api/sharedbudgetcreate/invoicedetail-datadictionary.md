# SharedBudgetCreate.InvoiceDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Invoice billing contact details supplied when creating a budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetCreate.InvoiceDetail
```

#### Discussion

Required for accounts on the Line of Credit (`LOC`) payment model. For all accounts, `name`, `primaryBuyerName`, `primaryBuyerEmail`, and `billingEmail` are required.

See [`InvoiceDetailCreate`](invoicedetailcreate.md) for the full field reference.

## Properties

- `primaryBuyerName` (string) *(required)*: Name of the primary buyer.
- `primaryBuyerEmail` (string) *(required)*: Email address of the primary buyer. Must be a valid email address.
- `billingEmail` (string) *(required)*: Billing email address. Must be a valid email address.
- `clientName` (string): Identifies the advertiser or product.
- `orderNumber` (string): Purchase order number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetcreate/invoicedetail-data.dictionary)*