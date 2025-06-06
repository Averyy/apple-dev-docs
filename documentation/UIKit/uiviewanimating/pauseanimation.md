# pauseAnimation()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Pauses a running animation at its current position.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func pauseAnimation()
```

#### Discussion

This method pauses running animations at their current values. Calling this method on an inactive animator moves its state to [`UIViewAnimatingState.active`](uiviewanimatingstate/active.md) and puts its animations in a paused state right away. To resume the animations, call the [`startAnimation()`](uiviewanimating/startanimation().md) method. If the animation is already paused, this method should do nothing. It is a programmer error to call this method while the state of the animator is set to [`UIViewAnimatingState.stopped`](uiviewanimatingstate/stopped.md).

## See Also

- [func startAnimation()](uiviewanimating/startanimation.md)
  Starts the animation from its current position.
- [func startAnimation(afterDelay: TimeInterval)](uiviewanimating/startanimation(afterdelay:).md)
  Starts the animation after the specified delay.
- [func stopAnimation(Bool)](uiviewanimating/stopanimation(_:).md)
  Stops the animations at their current positions.
- [func finishAnimation(at: UIViewAnimatingPosition)](uiviewanimating/finishanimation(at:).md)
  Finishes the animations and returns the animator to the inactive state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/pauseanimation())*