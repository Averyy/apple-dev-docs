# WKHapticType.click

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

Indicates a simple click type of feedback.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
case click
```

```c
WKHapticTypeClick
```

#### Discussion

Use this haptic to mark fixed points along a path. Space out the intervals at which you play the haptic rather than playing it several times in quick succession.

## See Also

### Constants
- [WKHapticType.notification](./notification.md)
  Alerts the user to an arrived notification when the Watch app is not running in the foreground.
- [WKHapticType.directionUp](./directionup.md)
  Indicates an increase in a specific value or when a value has gone above a certain threshold.
- [WKHapticType.directionDown](./directiondown.md)
  Indicates a decrease in a specific value or when a value has gone below a certain threshold.
- [WKHapticType.success](./success.md)
  Indicates the successful completion of a task or the answering of a question.
- [WKHapticType.failure](./failure.md)
  Indicates the failed completion of a task or answering of a question.
- [WKHapticType.retry](./retry.md)
  Indicates that the user should retry a task that temporarily failed.
- [WKHapticType.start](./start.md)
  Indicates the beginning of an action.
- [WKHapticType.stop](./stop.md)
  Indicates the end of an action.
- [WKHapticType.navigationGenericManeuver](./navigationgenericmaneuver.md)
  Indicates a new navigation step.
- [WKHapticType.navigationLeftTurn](./navigationleftturn.md)
  Indicates that the user should turn left.
- [WKHapticType.navigationRightTurn](./navigationrightturn.md)
  Indicates that the user should turn right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkhaptictype/click)*