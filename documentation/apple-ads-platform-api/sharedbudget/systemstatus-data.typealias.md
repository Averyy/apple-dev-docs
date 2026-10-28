# SharedBudget.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The system-derived operational state of a budget order.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string SharedBudget.SystemStatus
```

## Possible Values

- `ACTIVE`: The budget order is active. Campaigns assigned to it can draw spend against it.
- `INACTIVE`: The budget order is not currently active. No spend will be drawn until the underlying condition is resolved.

## Discussion

The `systemStatus` is a read-only, system-computed field. It reflects whether campaigns can currently draw spend against the budget order. Check `systemStatusReasons` to determine the specific cause when the status is not `ACTIVE`.

See [`BudgetSystemStatus`](../budgetsystemstatus.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/sharedbudget/systemstatus-data.typealias)*