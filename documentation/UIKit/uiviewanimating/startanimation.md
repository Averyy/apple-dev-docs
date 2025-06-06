# startAnimation()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Starts the animation from its current position.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func startAnimation()
```

#### Discussion

Call this method to start the animations or to resume the animation after they were paused. This method sets the state of the animator to [`UIViewAnimatingState.active`](uiviewanimatingstate/active.md), if it isn’t already there. It’s a programmer error to call this method while the state of the animator is set to [`UIViewAnimatingState.stopped`](uiviewanimatingstate/stopped.md).

When implementing a custom animator, use this method to transition your animator to the active state and to run the animations. Run your animations from the progress point in the [`fractionComplete`](uiviewanimating/fractioncomplete.md) property. Update the [`state`](uiviewanimating/state.md) and [`isRunning`](uiviewanimating/isrunning.md) properties, as well as any other relevant properties of your custom animator object.

## See Also

- [func startAnimation(afterDelay: TimeInterval)](uiviewanimating/startanimation(afterdelay:).md)
  Starts the animation after the specified delay.
- [func pauseAnimation()](uiviewanimating/pauseanimation.md)
  Pauses a running animation at its current position.
- [func stopAnimation(Bool)](uiviewanimating/stopanimation(_:).md)
  Stops the animations at their current positions.
- [func finishAnimation(at: UIViewAnimatingPosition)](uiviewanimating/finishanimation(at:).md)
  Finishes the animations and returns the animator to the inactive state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/startanimation())*