# setTaskCompleted()

**Framework**: Watchkit  
**Kind**: method

Marks the task as complete.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setTaskCompleted()
```

## Overview

Call this method as soon as you have finished the background task. The system provides your extension with a limited amount of time to finish the task (on the order of seconds). If you do not call [`setTaskCompleted()`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompleted()) on the task, the system continues to run in the background until all the available time is consumed, wasting battery power.

The system suspends the extension as soon as all background tasks are complete.

## See Also

- [var expirationHandler: (() -> Void)?](expirationhandler.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/expirationhandler))
- [func setTaskCompletedWithSnapshot(Bool)](settaskcompletedwithsnapshot(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompleted())*