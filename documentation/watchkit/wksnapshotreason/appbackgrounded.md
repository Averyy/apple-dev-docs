# WKSnapshotReason.appBackgrounded

**Framework**: WatchKit  
**Kind**: case

The app transitioned from the foreground to the background.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case appBackgrounded
```

## See Also

- [WKSnapshotReason.appScheduled](wksnapshotreason/appscheduled.md)
  The app scheduled this snapshot.
- [WKSnapshotReason.complicationUpdate](wksnapshotreason/complicationupdate.md)
  The app updated the complication timeline.
- [WKSnapshotReason.prelaunch](wksnapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [WKSnapshotReason.returnToDefaultState](wksnapshotreason/returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appbackgrounded)*