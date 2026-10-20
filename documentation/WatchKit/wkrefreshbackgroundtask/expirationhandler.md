# expirationHandler

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A block that the system calls when the available runtime for a background task is about to expire.

**Availability**:
- watchOS 8.0+

## Declaration

```swift
var expirationHandler: (() -> Void)? { get set }
```

```objc
@property (strong, nullable) void (^expirationHandler)();
```

## Mentions

- [Using background tasks](../using-background-tasks.md)

#### Discussion

To respond when your background task is about to expire, assign a block to this property. In this block, clean up any running background tasks, and prepare for the system to suspend your app.

## See Also

### Completing the background task
- [func setTaskCompletedWithSnapshot(Bool)](./settaskcompletedwithsnapshot%28_%29.md)
  Marks the task as complete and indicates whether the system should take a new snapshot of the app.
- [func setTaskCompleted()](./settaskcompleted%28%29.md)
  Marks the task as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/expirationhandler)*