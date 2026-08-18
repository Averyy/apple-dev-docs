# SharedBudgetAssignmentUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request payload for changing or removing a campaign’s budget order assignment.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudgetAssignmentUpdate
```

#### Discussion

The API embeds `SharedBudgetAssignmentUpdate` in [`CampaignUpdate`](campaignupdate.md) to modify a campaign’s budget order assignment.

##### Example

```json
{
  "budgetId": 555666777
}
```

## Properties

- `budgetId` (int64): The identifier of the budget order to assign this campaign to. Omit to leave the current assignment unchanged.

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
- [object InvoiceDetail](invoicedetail.md)
  Invoice billing details for accounts on the Line of Credit (LOC) payment model.
- [object InvoiceDetailUpdate](invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudgetassignmentupdate)*