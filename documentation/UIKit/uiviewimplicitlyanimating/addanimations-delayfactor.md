# addAnimations(_:delayFactor:)

**Framework**: UIKit  
**Kind**: method

Adds the specified animation block to the animator with a delay.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func addAnimations(_ animation: @escaping () -> Void, delayFactor: CGFloat)
```

#### Discussion

Use this method to add new animation blocks to your custom animator object. The animations in the new block should run alongside any previously configured animations, starting after the specified delay and finishing at the same time as any original animations. Your implementation must be able to handle multiple calls to this method.

## Parameters

- `animation`: A block containing the animations to add to the animator object. This block has no return value and takes no parameters.
- `delayFactor`: The factor to use for delaying the start of the animations. The value must be between   and  . Multiply this value by the animator’s remaining duration to determine the actual delay in seconds. For example, if the value   and the animator’s duration is  , delay the start of the animations by one second.

## See Also

- [func addAnimations(() -> Void)](uiviewimplicitlyanimating/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addCompletion((UIViewAnimatingPosition) -> Void)](uiviewimplicitlyanimating/addcompletion(_:).md)
  Adds the specified completion block to the animator.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](uiviewimplicitlyanimating/continueanimation(withtimingparameters:durationfactor:).md)
  Adjusts the final timing and duration of a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/addanimations(_:delayfactor:))*