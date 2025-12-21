# isUserInteractionEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether views receive touch events while animations are running.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isUserInteractionEnabled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), touch events are delivered to views normally. Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) causes touch events to be ignored in animated views for the duration of the animations. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var duration: TimeInterval](uiviewpropertyanimator/duration.md)
  The total duration (in seconds) of the main animations.
- [var delay: TimeInterval](uiviewpropertyanimator/delay.md)
  The delay (in seconds) after which the animations begin.
- [var timingParameters: (any UITimingCurveProvider)?](uiviewpropertyanimator/timingparameters.md)
  The information used to determine the timing curve for the animation.
- [var isInterruptible: Bool](uiviewpropertyanimator/isinterruptible.md)
  A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [var isManualHitTestingEnabled: Bool](uiviewpropertyanimator/ismanualhittestingenabled.md)
  A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [var scrubsLinearly: Bool](uiviewpropertyanimator/scrubslinearly.md)
  A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [var pausesOnCompletion: Bool](uiviewpropertyanimator/pausesoncompletion.md)
  A Boolean value that indicates whether a completed animation remains in the active state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/isuserinteractionenabled)*