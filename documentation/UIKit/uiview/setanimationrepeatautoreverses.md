# setAnimationRepeatAutoreverses(_:)

**Framework**: UIKit  
**Kind**: method

Sets whether the animations within an animation block automatically reverse themselves.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)
```

#### Discussion

If you enable autoreversing, a single animation cycle changes the properties being animated to their new values and then back to their original values. At the end of the animations, the affected views are then updated immediately to reflect the new values. This method does nothing if called from outside of an animation block. By default, autoreversing is disabled.

If you combine autoreversing with a repeat count (settable using the [`setAnimationRepeatCount(_:)`](uiview/setanimationrepeatcount(_:).md) method), you can create animations that shift back and forth between the old and new values the specified number of times. However, remember that the repeat count indicates the number of complete cycles. If you specify an integral value such as `2.0`, the animation ends on the old value, which is followed by the view immediately updating itself to show the new value, which might be jarring. If you want the animation to end on the new value (instead of the old value), add `0.5` to the repeat count value. This adds an extra half cycle to the animation.

Use of this method is discouraged in iOS 4.0 and later. Instead, you should use the[`animate(withDuration:delay:options:animations:completion:)`](uiview/animate(withduration:delay:options:animations:completion:).md) method to specify your animations and the animation options.

## Parameters

- `repeatAutoreverses`: Specify   to enable autoreversing or   to disable it.

## See Also

- [class func beginAnimations(String?, context: UnsafeMutableRawPointer?)](uiview/beginanimations(_:context:).md)
  Marks the beginning of a begin/commit animation block.
- [class func commitAnimations()](uiview/commitanimations.md)
  Marks the end of a begin/commit animation block and schedules the animations for execution.
- [class func setAnimationStart(Date)](uiview/setanimationstart(_:).md)
  Sets the start time for the current animation block.
- [class func setAnimationsEnabled(Bool)](uiview/setanimationsenabled(_:).md)
  Sets whether animations are enabled.
- [class func setAnimationDelegate(Any?)](uiview/setanimationdelegate(_:).md)
  Sets the delegate for any animation messages.
- [class func setAnimationWillStart(Selector?)](uiview/setanimationwillstart(_:).md)
  Sets the message to send to the animation delegate when the animation starts.
- [class func setAnimationDidStop(Selector?)](uiview/setanimationdidstop(_:).md)
  Sets the message to send to the animation delegate when animation stops.
- [class func setAnimationDuration(TimeInterval)](uiview/setanimationduration(_:).md)
  Sets the duration (measured in seconds) of the animations in an animation block.
- [class func setAnimationDelay(TimeInterval)](uiview/setanimationdelay(_:).md)
  Sets the amount of time (in seconds) to wait before animating property changes within an animation block.
- [class func setAnimationCurve(UIView.AnimationCurve)](uiview/setanimationcurve(_:).md)
  Sets the curve to use when animating property changes within an animation block.
- [class func setAnimationRepeatCount(Float)](uiview/setanimationrepeatcount(_:).md)
  Sets the number of times animations within an animation block repeat.
- [class func setAnimationBeginsFromCurrentState(Bool)](uiview/setanimationbeginsfromcurrentstate(_:).md)
  Sets whether the animation should begin playing from the current state.
- [class func setAnimationTransition(UIView.AnimationTransition, for: UIView, cache: Bool)](uiview/setanimationtransition(_:for:cache:).md)
  Sets a transition to apply to a view during an animation block.
- [class var areAnimationsEnabled: Bool](uiview/areanimationsenabled.md)
  Returns a Boolean value indicating whether animations are enabled.
- [func forBaselineLayout() -> UIView](uiview/forbaselinelayout.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationrepeatautoreverses(_:))*