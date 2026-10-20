# timingParameters

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The information used to determine the timing curve for the animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var timingParameters: (any UITimingCurveProvider)? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) id<UITimingCurveProvider> timingParameters;
```

#### Discussion

The timing curve defines the speed of the animation at different points during its execution. For a linear animation, the speed of the animation is constant over the total duration. For animations that follow a curve, the animation speeds up or slows down based on the slope of the curve. You specify the curve parameters at initialization time and can use this property to get those parameters later.

## See Also

### Accessing the animation parameters
- [var duration: TimeInterval](./duration.md)
  The total duration (in seconds) of the main animations.
- [var delay: TimeInterval](./delay.md)
  The delay (in seconds) after which the animations begin.
- [var isInterruptible: Bool](./isinterruptible.md)
  A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [var isUserInteractionEnabled: Bool](./isuserinteractionenabled.md)
  A Boolean value indicating whether views receive touch events while animations are running.
- [var isManualHitTestingEnabled: Bool](./ismanualhittestingenabled.md)
  A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [var scrubsLinearly: Bool](./scrubslinearly.md)
  A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [var pausesOnCompletion: Bool](./pausesoncompletion.md)
  A Boolean value that indicates whether a completed animation remains in the active state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/timingparameters)*