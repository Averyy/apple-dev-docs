# handle(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app has received one or more background tasks.

**Availability**:
- watchOS 3.0+ - Deprecated in 9.2

## Declaration

```swift
optional func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>)
```

```objc
- (void) handleBackgroundTasks:(NSSet<WKRefreshBackgroundTask *> *) backgroundTasks;
```

## Mentions

- [Using background tasks](../using-background-tasks.md)

#### Discussion

The system calls this method after launching your app to handle a background task. Use this method to handle the specified tasks. Call each tasks’s [`setTaskCompletedWithSnapshot(_:)`](../wkrefreshbackgroundtask/settaskcompletedwithsnapshot%28_%29.md) method as soon as the task is complete. For more information on background tasks, see [Using background tasks](../using-background-tasks.md).

## Parameters

- `backgroundTasks`: A set containing one or more background tasks.

## See Also

### Related Documentation
- [func recoverActiveWorkoutSession(completion: (HKWorkoutSession?, (any Error)?) -> Void)](../../HealthKit/hkhealthstore/recoveractiveworkoutsession%28completion%29.md)
  Recovers an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-92ulv)*