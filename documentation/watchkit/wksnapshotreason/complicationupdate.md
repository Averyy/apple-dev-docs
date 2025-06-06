# WKSnapshotReason.complicationUpdate

**Framework**: Watchkit  
**Kind**: case

The app updated the complication timeline.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case complicationUpdate
```

#### Discussion

These snapshot refresh tasks are only triggered when the WatchKit extension has a complication on the current watch face.

## See Also

- [WKSnapshotReason.appBackgrounded](wksnapshotreason/appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.appScheduled](wksnapshotreason/appscheduled.md)
  The app scheduled this snapshot.
- [WKSnapshotReason.prelaunch](wksnapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [WKSnapshotReason.returnToDefaultState](wksnapshotreason/returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/complicationupdate)*