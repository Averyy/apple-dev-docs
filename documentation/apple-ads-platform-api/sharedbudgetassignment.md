# SharedBudgetAssignment

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Represents a single budget order assignment within a campaign’s `sharedBudgets` array.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetAssignment
```

#### Discussion

`SharedBudgetAssignment` is an embedded object returned as part of a [`Campaign`](campaign.md). On Campaign, the field is `sharedBudgets`, an array of assignment objects each containing a `budgetId`.

A campaign can carry multiple budget order assignments as long as their schedules do not overlap.

**Multiple budget orders per campaign:** A campaign can be assigned to multiple budget orders, subject to the non-overlap rule. Sort budget orders by `startTime`. Each budget order must have an `endTime` that is strictly before the next budget order’s `startTime`. An open-ended budget order (no `endTime`) cannot be combined with another budget order on the same campaign. The API rejects overlapping schedules with a `BUDGET_ORDER_OVERLAPPING` error.

**No standalone operations:** `SharedBudgetAssignment` is not independently addressable. There are no standalone create, read, update, delete, or query operations for it. The API only returns assignment objects as part of a Campaign response.

##### Example

```json
{
  "budgetId": 555666777
}
```

## Properties

- `budgetId` (int64): The identifier of the budget order this campaign is assigned to. Read-only.

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
- [object SharedBudgetAssignmentCreate](sharedbudgetassignmentcreate.md)
  Request payload for assigning a campaign to a budget order at campaign creation time.
- [object SharedBudgetAssignmentUpdate](sharedbudgetassignmentupdate.md)
  Request payload for changing or removing a campaign’s budget order assignment.
- [object InvoiceDetail](invoicedetail.md)
  Invoice billing details for accounts on the Line of Credit (LOC) payment model.
- [object InvoiceDetailUpdate](invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetassignment)*