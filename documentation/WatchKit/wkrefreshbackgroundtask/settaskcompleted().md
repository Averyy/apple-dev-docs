# setTaskCompleted()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Marks the task as complete.

**Availability**:
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`setTaskCompletedWithSnapshot(_:)`](./settaskcompletedwithsnapshot%28_%29.md) instead.

## Declaration

```swift
func setTaskCompleted()
```

```objc
- (void) setTaskCompleted;
```

## Discussion

Call this method as soon as you have finished the background task. The system provides your extension with a limited amount of time to finish the task (on the order of seconds). If you do not call [`setTaskCompleted()`](./settaskcompleted%28%29.md) on the task, the system continues to run in the background until all the available time is consumed, wasting battery power.

The system suspends the extension as soon as all background tasks are complete.

## See Also

### Completing the background task
- [var expirationHandler: (() -> Void)?](./expirationhandler.md)
  A block that the system calls when the available runtime for a background task is about to expire.
- [func setTaskCompletedWithSnapshot(Bool)](./settaskcompletedwithsnapshot%28_%29.md)
  Marks the task as complete and indicates whether the system should take a new snapshot of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompleted())*