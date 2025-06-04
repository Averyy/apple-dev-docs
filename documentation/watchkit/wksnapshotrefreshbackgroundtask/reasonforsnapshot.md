# reasonForSnapshot

**Framework**: WatchKit  
**Kind**: property

The reason for taking the upcoming snapshot.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var reasonForSnapshot: WKSnapshotReason { get }
```

#### Discussion

You can use this property to change your application’s appearance before a snapshot is taken. For example, if the property contains an [`WKSnapshotReason.appBackgrounded`](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appbackgrounded) value, you’d probably want to capture the app’s current state, and no changes are necessary. However, if the property contains a [`WKSnapshotReason.returnToDefaultState`](https://developer.apple.com/documentation/watchkit/wksnapshotreason/returntodefaultstate) value, you may want to navigate back to the root view controller before taking the snapshot.

For a list of possible reasons for taking the snapshot, see [`WKSnapshotReason`](https://developer.apple.com/documentation/watchkit/wksnapshotreason).

## See Also

- [enum WKSnapshotReason](wksnapshotreason.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason))
  The reason for a background snapshot task.
- [var returnToDefaultState: Bool](returntodefaultstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/returntodefaultstate))
  A Boolean value indicating that the app should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/reasonforsnapshot)*