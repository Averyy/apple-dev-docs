# delay

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delay (in seconds) after which the animations begin.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var delay: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval delay;
```

## Discussion

The default value of this property is `0`. When the value is greater than 0, the start of any animations is delayed by the specified amount of time.

To set a value for this property, use the [`startAnimation(afterDelay:)`](../uiviewanimating/startanimation%28afterdelay%29.md) method when starting your animations.

## See Also

### Accessing the animation parameters
- [var duration: TimeInterval](./duration.md)
  The total duration (in seconds) of the main animations.
- [var timingParameters: (any UITimingCurveProvider)?](./timingparameters.md)
  The information used to determine the timing curve for the animation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/delay)*