# finishAnimation(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Finishes the animations and returns the animator to the inactive state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func finishAnimation(at finalPosition: UIViewAnimatingPosition)
```

```objc
- (void) finishAnimationAtPosition:(UIViewAnimatingPosition) finalPosition;
```

#### Discussion

After putting the animator object into the [`UIViewAnimatingState.stopped`](../uiviewanimatingstate/stopped.md) state, call this method to perform any final cleanup tasks. It is a programmer error to call this method at any time except after a call to the [`stopAnimation(_:)`](./stopanimation%28_%29.md) method where you pass [`false`](../../Swift/false.md) for the `withoutFinishing` parameter. Calling this method is not required, but is recommended in cases where you want to ensure that completion blocks or other final tasks are performed.

Implementations of this method are responsible for setting the state of the animator object to [`UIViewAnimatingState.inactive`](../uiviewanimatingstate/inactive.md) and for performing any final cleanup tasks, such as executing completion blocks.

## Parameters

- `finalPosition`: The final position for any view properties. Specify [`UIViewAnimatingPosition.current`](../uiviewanimatingposition/current.md) to leave the view properties unchanged from their current values.

## See Also

### Starting and stopping the animations
- [func startAnimation()](./startanimation%28%29.md)
  Starts the animation from its current position.
- [func startAnimation(afterDelay: TimeInterval)](./startanimation%28afterdelay%29.md)
  Starts the animation after the specified delay.
- [func pauseAnimation()](./pauseanimation%28%29.md)
  Pauses a running animation at its current position.
- [func stopAnimation(Bool)](./stopanimation%28_%29.md)
  Stops the animations at their current positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/finishanimation(at:))*