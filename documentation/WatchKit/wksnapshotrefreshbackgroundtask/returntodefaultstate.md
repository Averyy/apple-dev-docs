# returnToDefaultState

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating that the app should return to its default state.

**Availability**:
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`reasonForSnapshot`](./reasonforsnapshot.md) instead.

## Declaration

```swift
var returnToDefaultState: Bool { get }
```

```objc
@property (readonly) BOOL returnToDefaultState;
```

## See Also

### Instance properties
- [var reasonForSnapshot: WKSnapshotReason](./reasonforsnapshot.md)
  The reason for taking the upcoming snapshot.
- [enum WKSnapshotReason](../wksnapshotreason.md)
  The reason for a background snapshot task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/returntodefaultstate)*