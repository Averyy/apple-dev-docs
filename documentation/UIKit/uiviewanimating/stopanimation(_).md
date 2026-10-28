# stopAnimation(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stops the animations at their current positions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func stopAnimation(_ withoutFinishing: Bool)
```

```objc
- (void) stopAnimation:(BOOL) withoutFinishing;
```

## Discussion

Call this method when you want to end the animations at their current position. This method removes all of the associated animations from the execution stack and sets the values of any animatable properties to their current values. This method also updates the state of the animator object based on the value of the `withoutFinishing` parameter.

If you specify [`false`](../../Swift/false.md) for the `withoutFinishing` parameter, you can subsequently call the [`finishAnimation(at:)`](./finishanimation%28at%29.md) method to perform the animator’s final actions. For example, a [`UIViewPropertyAnimator`](../uiviewpropertyanimator.md) object executes its completion blocks when you call this method. You do not have to call the [`finishAnimation(at:)`](./finishanimation%28at%29.md) method right away, or at all, and you can perform other animations before calling that method.

## Parameters

- `withoutFinishing`: A Boolean indicating whether any final actions should be performed. Specify [`true`](../../Swift/true.md) to clear any animations and move the animator directly to the [`UIViewAnimatingState.inactive`](../uiviewanimatingstate/inactive.md) state without performing any final actions. Specify [`false`](../../Swift/false.md) to put the animator into the [`UIViewAnimatingState.stopped`](../uiviewanimatingstate/stopped.md) state.

## See Also

### Starting and stopping the animations
- [func startAnimation()](./startanimation%28%29.md)
  Starts the animation from its current position.
- [func startAnimation(afterDelay: TimeInterval)](./startanimation%28afterdelay%29.md)
  Starts the animation after the specified delay.
- [func pauseAnimation()](./pauseanimation%28%29.md)
  Pauses a running animation at its current position.
- [func finishAnimation(at: UIViewAnimatingPosition)](./finishanimation%28at%29.md)
  Finishes the animations and returns the animator to the inactive state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/stopanimation(_:))*