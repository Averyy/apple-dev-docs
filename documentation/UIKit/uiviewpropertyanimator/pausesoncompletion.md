# pausesOnCompletion

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a completed animation remains in the active state.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var pausesOnCompletion: Bool { get set }
```

```objc
@property (nonatomic) BOOL pausesOnCompletion;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the animator remains in the [`UIViewAnimatingState.active`](../uiviewanimatingstate/active.md) state when the animation finishes, and it does not execute its completion handler. Keeping the animator in the [`UIViewAnimatingState.active`](../uiviewanimatingstate/active.md) state allows you to reverse the animation even after it has finished. When the value of this property is [`false`](../../Swift/false.md), the animator automatically transitions to the [`UIViewAnimatingState.inactive`](../uiviewanimatingstate/inactive.md) state when the animation finishes, thereby concluding the animation. The default value of this property is [`false`](../../Swift/false.md).

Because the completion handler is not called when this property is [`true`](../../Swift/true.md), you cannot use the animator’s completion handler to determine when the animations have finished running. Instead, you determine when the animation has ended by observing the [`isRunning`](../uiviewanimating/isrunning.md) property.

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
- [var scrubsLinearly: Bool](./scrubslinearly.md)
  A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/pausesoncompletion)*