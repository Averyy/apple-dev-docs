# BudgetSystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The system-derived operational state of a budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BudgetSystemStatus
```

#### Discussion

`BudgetSystemStatus` is a read-only, system-computed field on budget objects. It reflects whether campaigns can currently draw spend against the budget. Check `systemStatusReasons` on the parent object to determine the specific cause when the status is not `ACTIVE`.

## See Also

- [type PaymentModel](paymentmodel.md)
  Enumeration of billing models that determine payment method and budget availability for an ad account.
- [type BudgetSystemStatusReason](budgetsystemstatusreason.md)
  A reason code that explains why a budget or budget order has its current system status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/budgetsystemstatus)*