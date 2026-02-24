# setTaskCompleted(restoredDefaultState:estimatedSnapshotExpiration:userInfo:)

**Framework**: WatchKit  
**Kind**: method

Marks the task as complete.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setTaskCompleted(restoredDefaultState: Bool, estimatedSnapshotExpiration: Date?, userInfo: (any NSSecureCoding & NSObjectProtocol)?)
```

#### Discussion

Call this method as soon as your app finishes updating its user interface. The system provides your extension with a limited amount of time (on the order of seconds) to finish the background snapshot refresh task. If you do not call [`setTaskCompleted(restoredDefaultState:estimatedSnapshotExpiration:userInfo:)`](wksnapshotrefreshbackgroundtask/settaskcompleted(restoreddefaultstate:estimatedsnapshotexpiration:userinfo:).md) on the task, the system uses all available time, wasting battery power. The system then suspends the extension as soon as the allotted time has expired.

The system automatically takes a snapshot of your app’s user interface as soon as this task is complete. The system also suspends the extension as soon as all background tasks are complete.

## Parameters

- `restoredDefaultState`: Pass [`true`](https://developer.apple.com/documentation/Swift/true) if your app has navigated back to its default launch scene.
- `estimatedSnapshotExpiration`: The preferred date and time for the next background snapshot refresh task.  Use [`distantFuture`](https://developer.apple.com/documentation/Foundation/NSDate/distantFuture) if you do not want to schedule the next refresh.
- `userInfo`: Custom data to be associated with the next background snapshot refresh task. This value is assigned to the next [`WKSnapshotRefreshBackgroundTask`](wksnapshotrefreshbackgroundtask.md) object’s [`userInfo`](wkrefreshbackgroundtask/userinfo.md) property. Pass `nil` if you don’t want to associate any data with the next task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/settaskcompleted(restoreddefaultstate:estimatedsnapshotexpiration:userinfo:))*