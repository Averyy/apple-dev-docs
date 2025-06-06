# addAnimations(_:)

**Framework**: UIKit  
**Kind**: method

Adds the specified animation block to the animator.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional func addAnimations(_ animation: @escaping () -> Void)
```

#### Discussion

Use this method to add new animation blocks to your custom animator object. The animations in the specified block should run alongside any previously configured animations, starting at the current time and finishing at the same time as any original animations. Your implementation must be able to handle multiple calls to this method.

## Parameters

- `animation`: A block containing the animations to add to the animator object. This block has no return value and takes no parameters.

## See Also

- [func addAnimations(() -> Void, delayFactor: CGFloat)](uiviewimplicitlyanimating/addanimations(_:delayfactor:).md)
  Adds the specified animation block to the animator with a delay.
- [func addCompletion((UIViewAnimatingPosition) -> Void)](uiviewimplicitlyanimating/addcompletion(_:).md)
  Adds the specified completion block to the animator.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](uiviewimplicitlyanimating/continueanimation(withtimingparameters:durationfactor:).md)
  Adjusts the final timing and duration of a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/addanimations(_:))*