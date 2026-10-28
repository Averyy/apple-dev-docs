# BudgetSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

A reason code that explains why a budget or budget order has its current system status.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BudgetSystemStatusReason
```

## Possible Values

- `CANCELED`: The budget was manually canceled and is no longer eligible to receive spend.
- `CAMPAIGN_BUDGET_UNASSIGNED`: No campaigns are currently assigned to draw against this budget.
- `DELETED_BY_USER`: The budget was soft-deleted by a user action.
- `EXHAUSTED`: The total monetary cap has been fully consumed. The budget cannot accept further spend until it is increased or a new budget is created.
- `PROCESSING`: The budget was recently created or modified and is still being processed by the system. This state is transient.
- `SCHEDULE_EXPIRED`: The budget’s `endTime` has passed.
- `SCHEDULE_PENDING`: The budget’s `startTime` has not yet been reached.

## Discussion

One or more `BudgetSystemStatusReason` values appear in the `systemStatusReasons` array on a budget or budget order. These codes are read-only and system-applied. They update automatically as conditions change. Use them to diagnose why a budget is `INACTIVE` and determine what action, if any, is required.

## See Also

- [type PaymentModel](./paymentmodel.md)
  Enumeration of billing models that determine payment method and budget availability for an ad account.
- [type BudgetSystemStatus](./budgetsystemstatus.md)
  The system-derived operational state of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/budgetsystemstatusreason)*