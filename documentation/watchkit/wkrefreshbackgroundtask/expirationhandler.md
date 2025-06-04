# expirationHandler

**Framework**: Watchkit  
**Kind**: property

A block that the system calls when the available runtime for a background task is about to expire.

**Availability**:
- watchOS 8.0+

## Declaration

```swift
var expirationHandler: (() -> Void)? { get set }
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

## Overview

To respond when your background task is about to expire, assign a block to this property. In this block, clean up any running background tasks, and prepare for the system to suspend your app.

## See Also

- [func setTaskCompletedWithSnapshot(Bool)](settaskcompletedwithsnapshot(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)))
- [func setTaskCompleted()](settaskcompleted().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompleted()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/expirationhandler)*