# state

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
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
var state: UIViewAnimatingState { get }
```

```objc
@property (nonatomic, readonly) UIViewAnimatingState state;
```

#### Discussion

This property reflects the current state of the animation. An animator object starts in the [`UIViewAnimatingState.inactive`](../uiviewanimatingstate/inactive.md) state. Calling the [`startAnimation()`](./startanimation%28%29.md) or [`pauseAnimation()`](./pauseanimation%28%29.md) method changes the state to [`UIViewAnimatingState.active`](../uiviewanimatingstate/active.md). Changing the [`fractionComplete`](./fractioncomplete.md) property also moves the animator to the active state. The animator remains in the active state until its animations finish, at which point it moves back to the inactive state.

Calling the [`stopAnimation(_:)`](./stopanimation%28_%29.md) method changes the state of the animator to [`UIViewAnimatingState.stopped`](../uiviewanimatingstate/stopped.md). When in this state, the animations are stopped and cannot be restarted until you call the [`finishAnimation(at:)`](./finishanimation%28at%29.md) method, which returns the animator to the inactive state.

## See Also

### Getting the animator’s state
- [var fractionComplete: CGFloat](./fractioncomplete.md)
  The completion percentage of the animation.
- [var isReversed: Bool](./isreversed.md)
  A Boolean value indicating whether the animation is running in the reverse direction.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value indicating whether the animation is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/state)*