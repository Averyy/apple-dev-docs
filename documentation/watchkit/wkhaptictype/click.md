# WKHapticType.click

**Framework**: Watchkit  
**Kind**: case

Indicates a simple click type of feedback.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
case click
```

#### Discussion

Use this haptic to mark fixed points along a path. Space out the intervals at which you play the haptic rather than playing it several times in quick succession.

## See Also

- [WKHapticType.notification](wkhaptictype/notification.md)
  Alerts the user to an arrived notification when the Watch app is not running in the foreground.
- [WKHapticType.directionUp](wkhaptictype/directionup.md)
  Indicates an increase in a specific value or when a value has gone above a certain threshold.
- [WKHapticType.directionDown](wkhaptictype/directiondown.md)
  Indicates a decrease in a specific value or when a value has gone below a certain threshold.
- [WKHapticType.success](wkhaptictype/success.md)
  Indicates the successful completion of a task or the answering of a question.
- [WKHapticType.failure](wkhaptictype/failure.md)
  Indicates the failed completion of a task or answering of a question.
- [WKHapticType.retry](wkhaptictype/retry.md)
  Indicates that the user should retry a task that temporarily failed.
- [WKHapticType.start](wkhaptictype/start.md)
  Indicates the beginning of an action.
- [WKHapticType.stop](wkhaptictype/stop.md)
  Indicates the end of an action.
- [WKHapticType.navigationGenericManeuver](wkhaptictype/navigationgenericmaneuver.md)
  Indicates a new navigation step.
- [WKHapticType.navigationLeftTurn](wkhaptictype/navigationleftturn.md)
  Indicates that the user should turn left.
- [WKHapticType.navigationRightTurn](wkhaptictype/navigationrightturn.md)
  Indicates that the user should turn right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkhaptictype/click)*