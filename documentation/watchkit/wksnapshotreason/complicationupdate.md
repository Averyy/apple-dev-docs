# WKSnapshotReason.complicationUpdate

**Framework**: WatchKit  
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

- [WKSnapshotReason.appBackgrounded](appbackgrounded.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appbackgrounded))
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.appScheduled](appscheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appscheduled))
  The app scheduled this snapshot.
- [WKSnapshotReason.prelaunch](prelaunch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/prelaunch))
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [WKSnapshotReason.returnToDefaultState](returntodefaultstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/returntodefaultstate))
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/complicationupdate)*