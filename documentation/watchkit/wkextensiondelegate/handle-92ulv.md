# handle(_:)

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the app has received one or more background tasks.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor optional func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>)
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

## Overview

The system calls this method after launching your app to handle a background task. Use this method to handle the specified tasks. Call each tasks’s [`setTaskCompletedWithSnapshot(_:)`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)) method as soon as the task is complete. For more information on background tasks, see [`Using background tasks`](https://developer.apple.com/documentation/watchkit/using-background-tasks).

## Parameters

- `backgroundTasks`: A set containing one or more background tasks.

## See Also

- func recoverActiveWorkoutSession(completion: (HKWorkoutSession?, (any Error)?) -> Void) ([Apple Docs](https://developer.apple.com/documentation/healthkit/hkhealthstore/2962889-recoveractiveworkoutsession))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-92ulv)*