# SharedBudgetAssignmentCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request payload for assigning a campaign to a budget order at campaign creation time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetAssignmentCreate
```

#### Discussion

`SharedBudgetAssignmentCreate` is embedded in [`CampaignCreate`](campaigncreate.md) to link a campaign to one or more existing budget orders at creation time. The `sharedBudgets` field on `CampaignCreate` is an array. You can create a campaign with multiple budget order assignments, subject to the non-overlap rule: each budget order must have an `endTime` strictly before the next budget order’s `startTime`. You cannot combine an open-ended budget order with another.

Every campaign requires a `dailyBudget` regardless of whether it has shared budget assignments. Both controls function independently: `dailyBudget` caps daily spending while each shared budget caps spending over its flight period.

##### Example

```json
{
  "budgetId": 555666777
}
```

## Properties

- `budgetId` (int64): The identifier of the budget order to assign this campaign to.

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
- [object SharedBudgetAssignmentUpdate](sharedbudgetassignmentupdate.md)
  Request payload for changing or removing a campaign’s budget order assignment.
- [object InvoiceDetail](invoicedetail.md)
  Invoice billing details for accounts on the Line of Credit (LOC) payment model.
- [object InvoiceDetailUpdate](invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetassignmentcreate)*