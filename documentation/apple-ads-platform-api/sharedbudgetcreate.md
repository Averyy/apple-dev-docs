# SharedBudgetCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for creating a new budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetCreate
```

#### Discussion

`SharedBudgetCreate` is the request payload for creating a new budget order.

Ensure the `currency` in the `Money` object matches the ad account’s currency. Once created, you can assign the budget order to one or more campaigns using `SharedBudgetAssignment` on each campaign.

##### Example

```json
{
  "name": "AwayFinder Q3 Budget Order",
  "startTime": "2026-08-01T00:00:00.000",
  "endTime": "2026-09-30T23:59:59.000",
  "value": {
    "amount": "50000.00",
    "currency": "USD"
  },
  "adAccountIds": [
    123456789
  ],
  "invoiceDetail": {
    "name": "AwayFinder Inc.",
    "orderNumber": "PO-987654321",
    "clientName": "AwayFinder Marketing",
    "primaryBuyerName": "Jordan Rivera",
    "primaryBuyerEmail": "jordan.rivera@awayfinder.com",
    "billingEmail": "billing@awayfinder.com"
  }
}
```

## Topics

### Dictionaries
- [object SharedBudgetCreate.InvoiceDetail](sharedbudgetcreate/invoicedetail-data.dictionary.md)
  Invoice billing contact details supplied when creating a budget order.

## Properties

- `name` (string) *(required)*: A descriptive label for the budget order. Must be non-empty.
- `startTime` (date-time) *(required)*: The date and time the budget becomes active. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2026-06-07T00:00:00.000`). Must be tomorrow or later (midnight UTC). Today is rejected.
- `endTime` (date-time): The date and time the budget expires. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC. Must be after `startTime`. Omit for an open-ended budget.
- `value` (Money) *(required)*: The total budget amount as a `Money` object with `amount` and ISO 4217 `currency` code. See [`Money`](money.md).
- `adAccountIds` ([int64]) *(required)*: The ad account IDs that can draw from this budget. Exactly one ID is allowed at creation. The API rejects requests that send more than one ID.
- `invoiceDetail` (SharedBudgetCreate.InvoiceDetail) *(required)*: Billing contact details. See [`SharedBudgetCreate.InvoiceDetail`](sharedbudgetcreate/invoicedetail-data.dictionary.md).

## See Also

- [object SharedBudget](sharedbudget.md)
  A budget order.
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
- [object InvoiceDetailUpdate](invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetcreate)*