# stopAnimation(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Stops the animations at their current positions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func stopAnimation(_ withoutFinishing: Bool)
```

#### Discussion

Call this method when you want to end the animations at their current position. This method removes all of the associated animations from the execution stack and sets the values of any animatable properties to their current values. This method also updates the state of the animator object based on the value of the `withoutFinishing` parameter.

If you specify [`false`](https://developer.apple.com/documentation/swift/false) for the `withoutFinishing` parameter, you can subsequently call the [`finishAnimation(at:)`](uiviewanimating/finishanimation(at:).md) method to perform the animator’s final actions. For example, a [`UIViewPropertyAnimator`](uiviewpropertyanimator.md) object executes its completion blocks when you call this method. You do not have to call the [`finishAnimation(at:)`](uiviewanimating/finishanimation(at:).md) method right away, or at all, and you can perform other animations before calling that method.

## Parameters

- `withoutFinishing`: A Boolean indicating whether any final actions should be performed. Specify   to clear any animations and move the animator directly to the   state without performing any final actions. Specify   to put the animator into the   state.

## See Also

- [func startAnimation()](uiviewanimating/startanimation.md)
  Starts the animation from its current position.
- [func startAnimation(afterDelay: TimeInterval)](uiviewanimating/startanimation(afterdelay:).md)
  Starts the animation after the specified delay.
- [func pauseAnimation()](uiviewanimating/pauseanimation.md)
  Pauses a running animation at its current position.
- [func finishAnimation(at: UIViewAnimatingPosition)](uiviewanimating/finishanimation(at:).md)
  Finishes the animations and returns the animator to the inactive state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/stopanimation(_:))*