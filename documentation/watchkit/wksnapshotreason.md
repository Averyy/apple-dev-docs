# WKSnapshotReason

**Framework**: WatchKit  
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
- [WKSnapshotReason.appBackgrounded](wksnapshotreason/appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [WKSnapshotReason.appScheduled](wksnapshotreason/appscheduled.md)
  The app scheduled this snapshot.
- [WKSnapshotReason.complicationUpdate](wksnapshotreason/complicationupdate.md)
  The app updated the complication timeline.
- [WKSnapshotReason.prelaunch](wksnapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [WKSnapshotReason.returnToDefaultState](wksnapshotreason/returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.
### Initializers
- [init?(rawValue: Int)](wksnapshotreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [RawRepresentable](https://developer.apple.com/documentation/Swift/RawRepresentable)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [var reasonForSnapshot: WKSnapshotReason](wksnapshotrefreshbackgroundtask/reasonforsnapshot.md)
  The reason for taking the upcoming snapshot.
- [var returnToDefaultState: Bool](wksnapshotrefreshbackgroundtask/returntodefaultstate.md)
  A Boolean value indicating that the app should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason)*