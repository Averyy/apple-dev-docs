# addAnimations(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified animation block to the animator.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional func addAnimations(_ animation: @escaping () -> Void)
```

```objc
- (void) addAnimations:(void (^)()) animation;
```

#### Discussion

Use this method to add new animation blocks to your custom animator object. The animations in the specified block should run alongside any previously configured animations, starting at the current time and finishing at the same time as any original animations. Your implementation must be able to handle multiple calls to this method.

## Parameters

- `animation`: A block containing the animations to add to the animator object. This block has no return value and takes no parameters.

## See Also

### Modifying animations
- [func addAnimations(() -> Void, delayFactor: CGFloat)](./addanimations%28_,delayfactor%29.md)
  Adds the specified animation block to the animator with a delay.
- [func addCompletion((UIViewAnimatingPosition) -> Void)](./addcompletion%28_%29.md)
  Adds the specified completion block to the animator.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](./continueanimation%28withtimingparameters,durationfactor%29.md)
  Adjusts the final timing and duration of a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/addanimations(_:))*