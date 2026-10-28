# pauseAnimation()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Pauses a running animation at its current position.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func pauseAnimation()
```

```objc
- (void) pauseAnimation;
```

## Discussion

This method pauses running animations at their current values. Calling this method on an inactive animator moves its state to [`UIViewAnimatingState.active`](../uiviewanimatingstate/active.md) and puts its animations in a paused state right away. To resume the animations, call the [`startAnimation()`](./startanimation%28%29.md) method. If the animation is already paused, this method should do nothing. It is a programmer error to call this method while the state of the animator is set to [`UIViewAnimatingState.stopped`](../uiviewanimatingstate/stopped.md).

## See Also

### Starting and stopping the animations
- [func startAnimation()](./startanimation%28%29.md)
  Starts the animation from its current position.
- [func startAnimation(afterDelay: TimeInterval)](./startanimation%28afterdelay%29.md)
  Starts the animation after the specified delay.
- [func stopAnimation(Bool)](./stopanimation%28_%29.md)
  Stops the animations at their current positions.
- [func finishAnimation(at: UIViewAnimatingPosition)](./finishanimation%28at%29.md)
  Finishes the animations and returns the animator to the inactive state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/pauseanimation())*