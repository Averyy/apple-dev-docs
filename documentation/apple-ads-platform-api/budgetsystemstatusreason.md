# BudgetSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias

A reason code that explains why a budget or budget order has its current system status.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BudgetSystemStatusReason
```

#### Discussion

One or more `BudgetSystemStatusReason` values appear in the `systemStatusReasons` array on a budget or budget order. These codes are read-only and system-applied. They update automatically as conditions change. Use them to diagnose why a budget is `INACTIVE` and determine what action, if any, is required.

## See Also

- [type PaymentModel](paymentmodel.md)
  Enumeration of billing models that determine payment method and budget availability for an ad account.
- [type BudgetSystemStatus](budgetsystemstatus.md)
  The system-derived operational state of a budget order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/budgetsystemstatusreason)*