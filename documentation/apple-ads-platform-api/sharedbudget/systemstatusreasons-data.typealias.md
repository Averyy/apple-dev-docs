# SharedBudget.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Reason codes explaining a budget order’s current system status.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string SharedBudget.SystemStatusReasons
```

## Possible Values

- `CANCELED`: The budget order was manually canceled and is no longer eligible to receive spend.
- `CAMPAIGN_BUDGET_UNASSIGNED`: No campaigns are currently assigned to draw against this budget order.
- `DELETED_BY_USER`: The budget order was soft-deleted by a user action.
- `EXHAUSTED`: The total monetary cap has been fully consumed. The budget order cannot accept further spend until it is increased or a new budget order is created.
- `PROCESSING`: The budget order was recently created or modified and is still being processed by the system. This state is transient.
- `SCHEDULE_EXPIRED`: The budget order’s `endTime` has passed.
- `SCHEDULE_PENDING`: The budget order’s `startTime` has not yet been reached.

#### Discussion

The `systemStatusReasons` is a read-only array populated by the system. It lists one or more reason codes that explain why a budget order has its current `systemStatus`. Use these codes to diagnose why a budget order is `INACTIVE` and determine what action, if any, is required.

See [`BudgetSystemStatusReason`](../budgetsystemstatusreason.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudget/systemstatusreasons-data.typealias)*