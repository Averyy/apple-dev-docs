# scrubsLinearly

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var scrubsLinearly: Bool { get set }
```

```objc
@property (nonatomic) BOOL scrubsLinearly;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md), which causes the animator to use a linear timing function during scrubbing. Setting the property to [`false`](../../Swift/false.md) causes the animator to use its specified timing curve.

## See Also

### Accessing the animation parameters
- [var duration: TimeInterval](./duration.md)
  The total duration (in seconds) of the main animations.
- [var delay: TimeInterval](./delay.md)
  The delay (in seconds) after which the animations begin.
- [var timingParameters: (any UITimingCurveProvider)?](./timingparameters.md)
  The information used to determine the timing curve for the animation.
- [var isInterruptible: Bool](./isinterruptible.md)
  A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [var isUserInteractionEnabled: Bool](./isuserinteractionenabled.md)
  A Boolean value indicating whether views receive touch events while animations are running.
- [var isManualHitTestingEnabled: Bool](./ismanualhittestingenabled.md)
  A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [var pausesOnCompletion: Bool](./pausesoncompletion.md)
  A Boolean value that indicates whether a completed animation remains in the active state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/scrubslinearly)*