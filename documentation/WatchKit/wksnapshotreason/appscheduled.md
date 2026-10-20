# WKSnapshotReason.appScheduled

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The app scheduled this snapshot.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case appScheduled
```

```c
WKSnapshotReasonAppScheduled
```

#### Discussion

You can schedule snapshots either by calling the [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](../wkextension/schedulesnapshotrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md) method, or—when completing a background task—by calling the [`setTaskCompletedWithSnapshot(_:)`](../wkrefreshbackgroundtask/settaskcompletedwithsnapshot%28_%29.md) method and passing [`true`](../../Swift/true.md).

These snapshot refresh tasks are only triggered when the watchOS app is in the dock.

## See Also

### Enumeration Cases
- [WKSnapshotReason.appBackgrounded](./appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.complicationUpdate](./complicationupdate.md)
  The app updated the complication timeline.
- [WKSnapshotReason.prelaunch](./prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [WKSnapshotReason.returnToDefaultState](./returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appscheduled)*