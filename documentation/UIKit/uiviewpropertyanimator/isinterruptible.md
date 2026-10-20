# isInterruptible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the animator is interruptible and can be paused or stopped.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isInterruptible: Bool { get set }
```

```objc
@property (nonatomic, getter=isInterruptible) BOOL interruptible;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), you can use the [`pauseAnimation()`](../uiviewanimating/pauseanimation%28%29.md) and [`stopAnimation(_:)`](../uiviewanimating/stopanimation%28_%29.md) methods to interrupt the animations and make changes. When the value of this property is [`false`](../../Swift/false.md), the animations run to completion (and without interruption) after you call the [`startAnimation()`](../uiviewanimating/startanimation%28%29.md) method. If you use a view property animator object to implement an interruptible view controller transition, this property must be [`true`](../../Swift/true.md).

It is a programmer error to change this property if the animator’s [`state`](../uiviewanimating/state.md) property is not set to [`UIViewAnimatingState.inactive`](../uiviewanimatingstate/inactive.md).

## See Also

### Accessing the animation parameters
- [var duration: TimeInterval](./duration.md)
  The total duration (in seconds) of the main animations.
- [var delay: TimeInterval](./delay.md)
  The delay (in seconds) after which the animations begin.
- [var timingParameters: (any UITimingCurveProvider)?](./timingparameters.md)
  The information used to determine the timing curve for the animation.
- [var isUserInteractionEnabled: Bool](./isuserinteractionenabled.md)
  A Boolean value indicating whether views receive touch events while animations are running.
- [var isManualHitTestingEnabled: Bool](./ismanualhittestingenabled.md)
  A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [var scrubsLinearly: Bool](./scrubslinearly.md)
  A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [var pausesOnCompletion: Bool](./pausesoncompletion.md)
  A Boolean value that indicates whether a completed animation remains in the active state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/isinterruptible)*