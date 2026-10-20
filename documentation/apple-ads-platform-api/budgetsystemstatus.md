# BudgetSystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The system-derived operational state of a budget order.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BudgetSystemStatus
```

## Possible Values

- `ACTIVE`: The budget is active. Campaigns assigned to this budget can draw spend against it.
- `INACTIVE`: The budget is not currently active. No spend will be drawn until the underlying condition is resolved.

#### Discussion

The `BudgetSystemStatus` is a read-only, system-computed field on budget objects. It reflects whether campaigns can currently draw spend against the budget. Check `systemStatusReasons` on the parent object to determine the specific cause when the status is not `ACTIVE`.

## See Also

- [type PaymentModel](./paymentmodel.md)
  Enumeration of billing models that determine payment method and budget availability for an ad account.
- [type BudgetSystemStatusReason](./budgetsystemstatusreason.md)
  A reason code that explains why a budget or budget order has its current system status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/budgetsystemstatus)*