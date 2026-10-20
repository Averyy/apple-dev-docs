# addCompletion(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified completion block to the animator.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func addCompletion(_ completion: @escaping (UIViewAnimatingPosition) -> Void)
```

```swift
func addCompletion() async -> UIViewAnimatingPosition
```

```objc
- (void) addCompletion:(void (^)(UIViewAnimatingPosition finalPosition)) completion;
```

#### Discussion

Completion blocks are executed after the animations finish normally. If you call the [`stopAnimation(_:)`](../uiviewanimating/stopanimation%28_%29.md) method, the completion blocks are not called if you specify [`true`](../../Swift/true.md) for the method’s parameter. If you specify [`false`](../../Swift/false.md) for the parameter, the animator executes the completion blocks normally after you call its [`finishAnimation(at:)`](../uiviewanimating/finishanimation%28at%29.md) method.

You may add completion blocks to an animator at any time, including while it is stopped.

## Parameters

- `completion`: A block to execute when the animations finish. This block has no return value and takes the following parameter:

  - **finalPosition**: The ending position of the animations. Use this value to determine whether the animations stopped at the beginning, end, or somewhere in the middle.

## See Also

### Modifying animations
- [func addAnimations(() -> Void)](./addanimations%28_%29.md)
  Adds the specified animation block to the animator.
- [func addAnimations(() -> Void, delayFactor: CGFloat)](./addanimations%28_,delayfactor%29.md)
  Adds the specified animation block with a delay.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](./continueanimation%28withtimingparameters,durationfactor%29.md)
  Adjusts the timing and duration of a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/addcompletion(_:))*