# WKSnapshotReason

**Framework**: Watchkit  
**Kind**: enum

The reason for a background snapshot task.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
enum WKSnapshotReason
```

## Topics

### Enumeration Cases
- [WKSnapshotReason.appBackgrounded](appbackgrounded.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appbackgrounded))
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.appScheduled](appscheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appscheduled))
  The app scheduled this snapshot.
- [WKSnapshotReason.complicationUpdate](complicationupdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/complicationupdate))
  The app updated the complication timeline.
- [WKSnapshotReason.prelaunch](prelaunch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/prelaunch))
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [WKSnapshotReason.returnToDefaultState](returntodefaultstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/returntodefaultstate))
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [var reasonForSnapshot: WKSnapshotReason](reasonforsnapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/reasonforsnapshot))
- [var returnToDefaultState: Bool](returntodefaultstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/returntodefaultstate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason)*