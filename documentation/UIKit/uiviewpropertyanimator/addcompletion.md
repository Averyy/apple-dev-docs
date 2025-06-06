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
func addCompletion() async -> UIViewAnimatingPosition
```

#### Discussion

Completion blocks are executed after the animations finish normally. If you call the [`stopAnimation(_:)`](uiviewanimating/stopanimation(_:).md) method, the completion blocks are not called if you specify [`true`](https://developer.apple.com/documentation/swift/true) for the method’s parameter. If you specify [`false`](https://developer.apple.com/documentation/swift/false) for the parameter, the animator executes the completion blocks normally after you call the its [`finishAnimation(at:)`](uiviewanimating/finishanimation(at:).md) method.

You may add completion blocks to an animator at any time, including while it is stopped.

## Parameters

- `completion`: A block to execute when the animations finish. This block has no return value and takes the following parameter:

## See Also

- [func addAnimations(() -> Void)](uiviewpropertyanimator/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addAnimations(() -> Void, delayFactor: CGFloat)](uiviewpropertyanimator/addanimations(_:delayfactor:).md)
  Adds the specified animation block with a delay.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](uiviewpropertyanimator/continueanimation(withtimingparameters:durationfactor:).md)
  Adjusts the timing and duration of a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/addcompletion(_:))*