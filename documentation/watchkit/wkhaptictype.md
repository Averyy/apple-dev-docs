# WKHapticType

**Framework**: Watchkit  
**Kind**: enum

Constant indicating the style of feedback to deliver using haptics.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKHapticType
```

## Topics

### Constants
- [WKHapticType.notification](notification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/notification))
  Alerts the user to an arrived notification when the Watch app is not running in the foreground.
- [WKHapticType.directionUp](directionup.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/directionup))
  Indicates an increase in a specific value or when a value has gone above a certain threshold.
- [WKHapticType.directionDown](directiondown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/directiondown))
  Indicates a decrease in a specific value or when a value has gone below a certain threshold.
- [WKHapticType.success](success.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/success))
  Indicates the successful completion of a task or the answering of a question.
- [WKHapticType.failure](failure.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/failure))
  Indicates the failed completion of a task or answering of a question.
- [WKHapticType.retry](retry.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/retry))
  Indicates that the user should retry a task that temporarily failed.
- [WKHapticType.start](start.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/start))
  Indicates the beginning of an action.
- [WKHapticType.stop](stop.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/stop))
  Indicates the end of an action.
- [WKHapticType.click](click.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/click))
  Indicates a simple click type of feedback.
- [WKHapticType.navigationGenericManeuver](navigationgenericmaneuver.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/navigationgenericmaneuver))
  Indicates a new navigation step.
- [WKHapticType.navigationLeftTurn](navigationleftturn.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/navigationleftturn))
  Indicates that the user should turn left.
- [WKHapticType.navigationRightTurn](navigationrightturn.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/navigationrightturn))
  Indicates that the user should turn right.
### Enumeration Cases
- [WKHapticType.underwaterDepthCriticalPrompt](underwaterdepthcriticalprompt.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/underwaterdepthcriticalprompt))
- [WKHapticType.underwaterDepthPrompt](underwaterdepthprompt.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/underwaterdepthprompt))
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [func play(WKHapticType)](play(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/play(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkhaptictype)*