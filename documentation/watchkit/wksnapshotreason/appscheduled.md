# WKSnapshotReason.appScheduled

**Framework**: WatchKit  
**Kind**: case

The app scheduled this snapshot.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case appScheduled
```

#### Discussion

You can schedule snapshots either by calling the [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](wkextension/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) method, or—when completing a background task—by calling the [`setTaskCompletedWithSnapshot(_:)`](wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:).md) method and passing [`true`](https://developer.apple.com/documentation/swift/true).

These snapshot refresh tasks are only triggered when the watchOS app is in the dock.

## See Also

- [WKSnapshotReason.appBackgrounded](wksnapshotreason/appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.complicationUpdate](wksnapshotreason/complicationupdate.md)
  The app updated the complication timeline.
- [WKSnapshotReason.prelaunch](wksnapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [WKSnapshotReason.returnToDefaultState](wksnapshotreason/returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appscheduled)*