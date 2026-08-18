# SharedBudget.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The system-derived operational state of a budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string SharedBudget.SystemStatus
```

#### Discussion

`systemStatus` is a read-only, system-computed field. It reflects whether campaigns can currently draw spend against the budget order. Check `systemStatusReasons` to determine the specific cause when the status is not `ACTIVE`.

See [`BudgetSystemStatus`](budgetsystemstatus.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudget/systemstatus-data.typealias)*