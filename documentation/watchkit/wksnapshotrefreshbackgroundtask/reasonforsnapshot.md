# reasonForSnapshot

**Framework**: Watchkit  
**Kind**: property

The reason for taking the upcoming snapshot.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var reasonForSnapshot: WKSnapshotReason { get }
```

#### Discussion

You can use this property to change your application’s appearance before a snapshot is taken. For example, if the property contains an [`WKSnapshotReason.appBackgrounded`](wksnapshotreason/appbackgrounded.md) value, you’d probably want to capture the app’s current state, and no changes are necessary. However, if the property contains a [`WKSnapshotReason.returnToDefaultState`](wksnapshotreason/returntodefaultstate.md) value, you may want to navigate back to the root view controller before taking the snapshot.

For a list of possible reasons for taking the snapshot, see [`WKSnapshotReason`](wksnapshotreason.md).

## See Also

- [enum WKSnapshotReason](wksnapshotreason.md)
  The reason for a background snapshot task.
- [var returnToDefaultState: Bool](wksnapshotrefreshbackgroundtask/returntodefaultstate.md)
  A Boolean value indicating that the app should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/reasonforsnapshot)*