# WKSnapshotReason.returnToDefaultState

**Framework**: WatchKit  
**Kind**: case

It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case returnToDefaultState
```

## See Also

- [WKSnapshotReason.appBackgrounded](appbackgrounded.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appbackgrounded))
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.appScheduled](appscheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appscheduled))
  The app scheduled this snapshot.
- [WKSnapshotReason.complicationUpdate](complicationupdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/complicationupdate))
  The app updated the complication timeline.
- [WKSnapshotReason.prelaunch](prelaunch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/prelaunch))
  The system needs a snapshot for the dock, but the app has not been launched yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/returntodefaultstate)*