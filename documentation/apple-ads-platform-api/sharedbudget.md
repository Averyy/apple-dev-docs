# SharedBudget

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SharedBudget
```

#### Discussion

A SharedBudget creates a spending cap across a group of campaigns within an ad account. Campaigns participating in the same SharedBudget draw from a common spend limit. `startTime` and `endTime` define the active window.

`systemStatus` reflects whether the budget is currently usable. Common blocking reasons in `systemStatusReasons` include `EXHAUSTED` and `SCHEDULE_PENDING`.

##### Example

```json
{
  "id": 777890001,
  "name": "AwayFinder - Q3 2026 Budget",
  "startTime": "2026-07-01T00:00:00.000",
  "endTime": "2026-09-30T23:59:59.000",
  "value": {
    "amount": "20000.00",
    "currency": "USD"
  },
  "adAccountIds": [
    123456789
  ],
  "orgId": 555666777,
  "systemStatus": "ACTIVE",
  "systemStatusReasons": [],
  "invoiceDetail": {
    "name": "AwayFinder Q3 2026 Invoice",
    "primaryBuyerName": "Jane Smith",
    "primaryBuyerEmail": "jane.smith@awayfinder.com",
    "billingEmail": "billing@awayfinder.com"
  },
  "creationTime": "2026-06-06T10:00:00.000",
  "modificationTime": "2026-06-06T10:00:00.000",
  "deleted": false
}
```

## Topics

### Dictionaries
- [object SharedBudget.InvoiceDetail](sharedbudget/invoicedetail-data.dictionary.md)
  Invoice billing details for accounts on the Line of Credit (LOC) payment model.
### Type Aliases
- [type SharedBudget.SystemStatus](sharedbudget/systemstatus-data.typealias.md)
  The system-derived operational state of a budget order.
- [type SharedBudget.SystemStatusReasons](sharedbudget/systemstatusreasons-data.typealias.md)
  Reason codes explaining a budget order’s current system status.

## Properties

- `name` (string): Non-empty string label for the budget order. Mutable.
- `startTime` (date-time): The start date and time for this budget. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2026-06-07T00:00:00.000`). Must be tomorrow or later (midnight UTC). Today is rejected. Mutable.
- `endTime` (date-time): The end date and time for this budget. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC. Must be after `startTime`. Omit for an open-ended budget. Mutable.
- `value` (Money): The budget amount as a Money object with amount and ISO 4217 currency code. See [`Money`](money.md). Mutable.
- `adAccountIds` ([int64]): The ad account IDs this budget order applies to. Exactly one allowed at creation. Mutable.
- `orgId` (int64): The identifier of the organization that owns this budget order. Read-only.
- `systemStatus` (SharedBudget.SystemStatus): Current system status of this budget order. See [`BudgetSystemStatus`](budgetsystemstatus.md). Read-only.
- `systemStatusReasons` ([SharedBudget.SystemStatusReasons]): Status reasons applied based on system factors. Values: `CANCELED`, `CAMPAIGN_BUDGET_UNASSIGNED`, `DELETED_BY_USER`, `EXHAUSTED`, `PROCESSING`, `SCHEDULE_EXPIRED`, `SCHEDULE_PENDING`. Read-only.
- `invoiceDetail` (SharedBudget.InvoiceDetail): Invoice details required on create for Line of Credit accounts. Required fields: `name`, `primaryBuyerName`, `primaryBuyerEmail`, `billingEmail`. `clientName` and `orderNumber` are optional and nullable. See [`SharedBudget.InvoiceDetail`](sharedbudget/invoicedetail-data.dictionary.md). Mutable.
- `id` (int64): The unique budget identifier. Read-only.
- `creationTime` (date-time): Timestamp when the budget was created. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC. Read-only.
- `modificationTime` (date-time): Timestamp of the last modification. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC. Read-only.
- `deleted` (boolean): Indicates if the budget has been deleted. Read-only.

## See Also

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
- [object InvoiceDetailUpdate](invoicedetailupdate.md)
  The request body for updating the invoice details of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudget)*