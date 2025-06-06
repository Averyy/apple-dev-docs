# setAnimationRepeatCount(_:)

**Framework**: UIKit  
**Kind**: method

Sets the number of times animations within an animation block repeat.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class func setAnimationRepeatCount(_ repeatCount: Float)
```

#### Discussion

Use this method to specify the number of times to repeat the specified animations. This method does nothing if called from outside of an animation block. You can use this method in conjunction with either the block-based methods or the begin/commit methods for defining an animation block. If you do not explicitly set a repeat count, the animation is not repeated.

If you pass the [`repeat`](uiview/animationoptions/repeat.md) option to the [`animate(withDuration:delay:options:animations:completion:)`](uiview/animate(withduration:delay:options:animations:completion:).md) method without setting an explicit repeat count, the animation repeats indefinitely. If you want the animation to repeat a finite number of times, call this method from inside your block.

## Parameters

- `repeatCount`: The number of times animations repeat. This value can be a fraction. If you specify the value  , the animation is performed once without repeating.

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
- [class func setAnimationRepeatAutoreverses(Bool)](uiview/setanimationrepeatautoreverses(_:).md)
  Sets whether the animations within an animation block automatically reverse themselves.
- [class func setAnimationBeginsFromCurrentState(Bool)](uiview/setanimationbeginsfromcurrentstate(_:).md)
  Sets whether the animation should begin playing from the current state.
- [class func setAnimationTransition(UIView.AnimationTransition, for: UIView, cache: Bool)](uiview/setanimationtransition(_:for:cache:).md)
  Sets a transition to apply to a view during an animation block.
- [class var areAnimationsEnabled: Bool](uiview/areanimationsenabled.md)
  Returns a Boolean value indicating whether animations are enabled.
- [func forBaselineLayout() -> UIView](uiview/forbaselinelayout.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationrepeatcount(_:))*