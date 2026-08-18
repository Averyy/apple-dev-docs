# SharedBudget.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Reason codes explaining a budget order’s current system status.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string SharedBudget.SystemStatusReasons
```

#### Discussion

`systemStatusReasons` is a read-only array populated by the system. It lists one or more reason codes that explain why a budget order has its current `systemStatus`. Use these codes to diagnose why a budget order is `INACTIVE` and determine what action, if any, is required.

See [`BudgetSystemStatusReason`](budgetsystemstatusreason.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudget/systemstatusreasons-data.typealias)*