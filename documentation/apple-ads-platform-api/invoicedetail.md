# InvoiceDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Invoice billing details for accounts on the Line of Credit (LOC) payment model.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object InvoiceDetail
```

#### Discussion

`InvoiceDetail` captures the billing contact information required for campaign or budget Line of Credit (`LOC`) payment model accounts. The API embeds it in `Campaign` and `SharedBudget` objects.

See [`InvoiceDetailCreate`](invoicedetailcreate.md) for which fields are required when creating a new record, and [`InvoiceDetailUpdate`](invoicedetailupdate.md) for update behavior.

##### Example

```json
{
  "name": "AwayFinder Q1 Invoice",
  "clientName": "AwayFinder",
  "primaryBuyerName": "Jordan Blake",
  "primaryBuyerEmail": "jordan.blake@awayfinder.com",
  "orderNumber": "PO-556677",
  "billingEmail": "billing@awayfinder.com"
}
```

## Properties

- `clientName` (string): Identifies the advertiser or product. Nullable. Mutable.
- `primaryBuyerName` (string): Name of the primary buyer. Mutable.
- `primaryBuyerEmail` (string): Email address of the primary buyer. Must be a valid email address. Mutable.
- `orderNumber` (string): Purchase order number. Typically a PO number. Nullable. Mutable.
- `billingEmail` (string): Billing email address. Must be a valid email address. Mutable.

## See Also

- [object SharedBudget](sharedbudget.md)
  A budget order.
- [object SharedBudgetCreate](sharedbudgetcreate.md)
  The request body for creating a new budget order.
- [object SharedBudgetUpdate](sharedbudgetupdate.md)
  Request body for updating an existing budget order.
- [object SharedBudgetResponse](sharedbudgetresponse.md)
  The response object for a single budget order operation.
- [object SharedBudgetQueryResponse](sharedbudgetqueryresponse.md)
  The response object for a budget order query.
- [object SharedBudgetAssignment](sharedbudgetassignment.md)
  Represents a single budget order assignment within a campaign’s `sharedBudgets` array.
- [object SharedBudgetAssignmentCreate](sharedbudgetassignmentcreate.md)
  Request payload for assigning a campaign to a budget order at campaign creation time.
- [object SharedBudgetAssignmentUpdate](sharedbudgetassignmentupdate.md)
  Request payload for changing or removing a campaign’s budget order assignment.
- [object InvoiceDetailUpdate](invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/invoicedetail)*