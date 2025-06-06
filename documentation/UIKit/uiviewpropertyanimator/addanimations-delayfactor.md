# addAnimations(_:delayFactor:)

**Framework**: UIKit  
**Kind**: method

Adds the specified animation block with a delay.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addAnimations(_ animation: @escaping () -> Void, delayFactor: CGFloat)
```

#### Discussion

Use this method to add new animation blocks to the animator. The animations in the new block run alongside any previously configured animations after the specified delay. Blocks added while the animator’s state is [`UIViewAnimatingState.inactive`](uiviewanimatingstate/inactive.md) are executed over the time specified by the [`duration`](uiviewpropertyanimator/duration.md) property minus any delay. Blocks added while the animator’s state is [`UIViewAnimatingState.active`](uiviewanimatingstate/active.md) are executed over the remaining portion of the total run time minus the delay. For example, if the duration is `2.0` and you add an animation block with a delay factor of `0.25` to a running animator whose [`fractionComplete`](uiviewanimating/fractioncomplete.md) property is `0.25`, the animations run for `1.0` second.

If the `animation` block modifies a property that is being modified by a different property animator, then the animators combine their changes in the most appropriate way. For many properties, the changes from each animator are added together to yield a new intermediate value. If a property cannot be modified in this additive manner, the new animations take over as if the [`beginFromCurrentState`](uiview/animationoptions/beginfromcurrentstate.md) option had been specified for a view-based animation.

You can call this method multiple times to add multiple blocks to the animator. It is a programmer error to call this method when the animator’s [`state`](uiviewanimating/state.md) property is set to [`UIViewAnimatingState.stopped`](uiviewanimatingstate/stopped.md).

## Parameters

- `animation`: A block containing the animations you want to add to the animator object. This block has no return value and takes no parameters. This parameter must not be  .
- `delayFactor`: The factor to use for delaying the start of the animations. The value you specify must be between   and  . This value is multiplied by the animator’s remaining duration to determine the actual delay in seconds. For example, specifying the value   when the duration is   results in a one second delay for the start of the animations.

## See Also

- [func addAnimations(() -> Void)](uiviewpropertyanimator/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addCompletion((UIViewAnimatingPosition) -> Void)](uiviewpropertyanimator/addcompletion(_:).md)
  Adds the specified completion block to the animator.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](uiviewpropertyanimator/continueanimation(withtimingparameters:durationfactor:).md)
  Adjusts the timing and duration of a paused animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/addanimations(_:delayfactor:))*