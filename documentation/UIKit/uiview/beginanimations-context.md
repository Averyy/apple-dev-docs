# beginAnimations(_:context:)

**Framework**: UIKit  
**Kind**: method

Marks the beginning of a begin/commit animation block.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class func beginAnimations(_ animationID: String?, context: UnsafeMutableRawPointer?)
```

#### Discussion

This method signals to the system that you want to specify one or more animations to perform. After calling this method, configure the animation options (using the `setAnimation…` class methods) and then change the desired animatable properties of your views. When you are done changing your view properties, call the [`commitAnimations()`](uiview/commitanimations().md) method to close the set and schedule the animations.

You can nest sets of animations (by calling this method again before committing a previous set of animations) as needed. Nesting animations groups them together and allows you to set different animation options for the nested group.

If you install a start or stop selector using the [`setAnimationWillStart(_:)`](uiview/setanimationwillstart(_:).md) or [`setAnimationDidStop(_:)`](uiview/setanimationdidstop(_:).md) method, the values you specify for the `animationID` and `context` parameters are passed to your selectors at runtime. You can use these parameters to pass additional information to those selectors.

Use of this method is discouraged in iOS 4.0 and later. You should use the block-based animation methods to specify your animations instead.

## Parameters

- `animationID`: An application-supplied identifier for the animations.
- `context`: Custom data that you want to associate with this set of animations. information that is passed to the animation delegate messages—the selectors set using the   and   methods.

## See Also

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
- [class func setAnimationBeginsFromCurrentState(Bool)](uiview/setanimationbeginsfromcurrentstate(_:).md)
  Sets whether the animation should begin playing from the current state.
- [class func setAnimationTransition(UIView.AnimationTransition, for: UIView, cache: Bool)](uiview/setanimationtransition(_:for:cache:).md)
  Sets a transition to apply to a view during an animation block.
- [class var areAnimationsEnabled: Bool](uiview/areanimationsenabled.md)
  Returns a Boolean value indicating whether animations are enabled.
- [func forBaselineLayout() -> UIView](uiview/forbaselinelayout.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/beginanimations(_:context:))*