# WKSnapshotReason.prelaunch

**Framework**: WatchKit  
**Kind**: case

The system needs a snapshot for the dock, but the app has not been launched yet.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case prelaunch
```

## See Also

- [WKSnapshotReason.appBackgrounded](appbackgrounded.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appbackgrounded))
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.appScheduled](appscheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appscheduled))
  The app scheduled this snapshot.
- [WKSnapshotReason.complicationUpdate](complicationupdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/complicationupdate))
  The app updated the complication timeline.
- [WKSnapshotReason.returnToDefaultState](returntodefaultstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/returntodefaultstate))
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/prelaunch)*