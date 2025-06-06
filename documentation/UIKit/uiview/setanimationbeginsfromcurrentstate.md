# setAnimationBeginsFromCurrentState(_:)

**Framework**: UIKit  
**Kind**: method

Sets whether the animation should begin playing from the current state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)
```

#### Discussion

If set to [`true`](https://developer.apple.com/documentation/swift/true) when an animation is in flight, the current view position of the in-flight animation is used as the starting state for the new animation. If set to [`false`](https://developer.apple.com/documentation/swift/false), the in-flight animation ends before the new animation begins using the last view position as the starting state. This method does nothing if an animation is not in flight or invoked outside of an animation block. Use the [`beginAnimations(_:context:)`](uiview/beginanimations(_:context:).md) class method to start and the [`commitAnimations()`](uiview/commitanimations().md) class method to end an animation block. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

Use of this method is discouraged in iOS 4.0 and later. Instead, you should use the[`animate(withDuration:delay:options:animations:completion:)`](uiview/animate(withduration:delay:options:animations:completion:).md) method to specify your animations and the animation options.

## Parameters

- `fromCurrentState`: Specify   if animations should begin from their currently visible state; otherwise,  .

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
- [class func setAnimationRepeatAutoreverses(Bool)](uiview/setanimationrepeatautoreverses(_:).md)
  Sets whether the animations within an animation block automatically reverse themselves.
- [class func setAnimationTransition(UIView.AnimationTransition, for: UIView, cache: Bool)](uiview/setanimationtransition(_:for:cache:).md)
  Sets a transition to apply to a view during an animation block.
- [class var areAnimationsEnabled: Bool](uiview/areanimationsenabled.md)
  Returns a Boolean value indicating whether animations are enabled.
- [func forBaselineLayout() -> UIView](uiview/forbaselinelayout.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationbeginsfromcurrentstate(_:))*