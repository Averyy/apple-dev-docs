# InvoiceDetailUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating the invoice details of a budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object InvoiceDetailUpdate
```

#### Discussion

All fields are optional, allowing partial updates to an existing invoice detail record. See [`InvoiceDetailCreate`](invoicedetailcreate.md) for required fields on create.

##### Example

```json
{
  "name": "AwayFinder Q3 Invoice",
  "orderNumber": "PO-555666777",
  "clientName": "AwayFinder",
  "primaryBuyerName": "Jordan Lee",
  "primaryBuyerEmail": "jordan.lee@awayfinder.com",
  "billingEmail": "billing@awayfinder.com"
}
```

## Properties

- `orderNumber` (string): Purchase order number.
- `clientName` (string): Identifies the advertiser or product.
- `primaryBuyerName` (string): Name of the primary buyer.
- `primaryBuyerEmail` (string): Email address of the primary buyer. Must be a valid email address.
- `billingEmail` (string): Billing email address. Must be a valid email address.

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
- [object InvoiceDetail](invoicedetail.md)
  Invoice billing details for accounts on the Line of Credit (LOC) payment model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/invoicedetailupdate)*