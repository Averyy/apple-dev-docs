# state

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The current state of the animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var state: UIViewAnimatingState { get }
```

#### Discussion

This property reflects the current state of the animation. An animator object starts in the [`UIViewAnimatingState.inactive`](uiviewanimatingstate/inactive.md) state. Calling the [`startAnimation()`](uiviewanimating/startanimation().md) or [`pauseAnimation()`](uiviewanimating/pauseanimation().md) method changes the state to [`UIViewAnimatingState.active`](uiviewanimatingstate/active.md). Changing the [`fractionComplete`](uiviewanimating/fractioncomplete.md) property also moves the animator to the active state. The animator remains in the active state until its animations finish, at which point it moves back to the inactive state.

Calling the [`stopAnimation(_:)`](uiviewanimating/stopanimation(_:).md) method changes the state of the animator to [`UIViewAnimatingState.stopped`](uiviewanimatingstate/stopped.md). When in this state, the animations are stopped and cannot be restarted until you call the [`finishAnimation(at:)`](uiviewanimating/finishanimation(at:).md) method, which returns the animator to the inactive state.

## See Also

- [var fractionComplete: CGFloat](uiviewanimating/fractioncomplete.md)
  The completion percentage of the animation.
- [var isReversed: Bool](uiviewanimating/isreversed.md)
  A Boolean value indicating whether the animation is running in the reverse direction.
- [var isRunning: Bool](uiviewanimating/isrunning.md)
  A Boolean value indicating whether the animation is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/state)*