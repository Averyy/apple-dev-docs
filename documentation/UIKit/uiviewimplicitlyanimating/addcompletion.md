# addCompletion(_:)

**Framework**: UIKit  
**Kind**: method

Adds the specified completion block to the animator.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func addCompletion() async -> UIViewAnimatingPosition
```

#### Discussion

Use this method to add the completion blocks to your custom animator object. Completion blocks should execute after the animations finish successfully. If the [`stopAnimation(_:)`](uiviewanimating/stopanimation(_:).md) method is called, do not execute any completion blocks if the `withoutFinishing` parameter for that method contains the value [`true`](https://developer.apple.com/documentation/swift/true). If the parameter is [`false`](https://developer.apple.com/documentation/swift/false) and the client subsequent calls the [`finishAnimation(at:)`](uiviewanimating/finishanimation(at:).md) method, execute the completion blocks in your implementation of that method. Your implementation must be able to handle multiple calls to this method.

## Parameters

- `completion`: A block to execute when the animations finish. This block has no return value and takes the following parameter:

## See Also

- [func addAnimations(() -> Void)](uiviewimplicitlyanimating/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addAnimations(() -> Void, delayFactor: CGFloat)](uiviewimplicitlyanimating/addanimations(_:delayfactor:).md)
  Adds the specified animation block to the animator with a delay.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](uiviewimplicitlyanimating/continueanimation(withtimingparameters:durationfactor:).md)
  Adjusts the final timing and duration of a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating/addcompletion(_:))*