# isInterruptible

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the animator is interruptible and can be paused or stopped.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isInterruptible: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), you can use the [`pauseAnimation()`](uiviewanimating/pauseanimation().md) and [`stopAnimation(_:)`](uiviewanimating/stopanimation(_:).md) methods to interrupt the animations and make changes. When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the animations run to completion (and without interruption) after you call the [`startAnimation()`](uiviewanimating/startanimation().md) method. If you use a view property animator object to implement an interruptible view controller transition, this property must be [`true`](https://developer.apple.com/documentation/Swift/true).

It is a programmer error to change this property if the animator’s [`state`](uiviewanimating/state.md) property is not set to [`UIViewAnimatingState.inactive`](uiviewanimatingstate/inactive.md).

## See Also

- [var duration: TimeInterval](uiviewpropertyanimator/duration.md)
  The total duration (in seconds) of the main animations.
- [var delay: TimeInterval](uiviewpropertyanimator/delay.md)
  The delay (in seconds) after which the animations begin.
- [var timingParameters: (any UITimingCurveProvider)?](uiviewpropertyanimator/timingparameters.md)
  The information used to determine the timing curve for the animation.
- [var isUserInteractionEnabled: Bool](uiviewpropertyanimator/isuserinteractionenabled.md)
  A Boolean value indicating whether views receive touch events while animations are running.
- [var isManualHitTestingEnabled: Bool](uiviewpropertyanimator/ismanualhittestingenabled.md)
  A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [var scrubsLinearly: Bool](uiviewpropertyanimator/scrubslinearly.md)
  A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [var pausesOnCompletion: Bool](uiviewpropertyanimator/pausesoncompletion.md)
  A Boolean value that indicates whether a completed animation remains in the active state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/isinterruptible)*