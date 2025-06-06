# continueAnimation(withTimingParameters:durationFactor:)

**Framework**: UIKit  
**Kind**: method

Adjusts the timing and duration of a paused animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func continueAnimation(withTimingParameters parameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)
```

#### Discussion

This method overrides the timing and duration parameters for the current animations. When calling this method, the animator must be active and currently paused. It’s a programmer error to call this method when the animator is inactive, running, or its [`isInterruptible`](uiviewpropertyanimator/isinterruptible.md) property is set to [`false`](https://developer.apple.com/documentation/swift/false).

This method overrides the original timing and duration values only until the current animations finish. The original timing and duration values are restored when the animator transitions back to the inactive state.

## Parameters

- `parameters`: The new timing information to apply to the animation. The animator may transition from the previous timing curve to the new timing curve over time to keep the transition from becoming too jarring. For example, if the previous timing curve used a spring animation, the animator may add some of spring behavior to the new animation.
- `durationFactor`: A multiplying factor to apply to the animation’s original duration. The value of this parameter is multiplied by the original   value to obtain the new duration for the animations.

## See Also

- [func pauseAnimation()](uiviewanimating/pauseanimation.md)
  Pauses a running animation at its current position.
- [func addAnimations(() -> Void)](uiviewpropertyanimator/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addAnimations(() -> Void, delayFactor: CGFloat)](uiviewpropertyanimator/addanimations(_:delayfactor:).md)
  Adds the specified animation block with a delay.
- [func addCompletion((UIViewAnimatingPosition) -> Void)](uiviewpropertyanimator/addcompletion(_:).md)
  Adds the specified completion block to the animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/continueanimation(withtimingparameters:durationfactor:))*