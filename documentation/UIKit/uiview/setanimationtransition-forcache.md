# setAnimationTransition(_:for:cache:)

**Framework**: UIKit  
**Kind**: method

Sets a transition to apply to a view during an animation block.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
class func setAnimationTransition(_ transition: UIView.AnimationTransition, for view: UIView, cache: Bool)
```

#### Discussion

If you want to change the appearance of a view during a transition—for example, flip from one view to another—then use a container view, an instance of [`UIView`](uiview.md), as follows:

1. Begin an animation block.
2. Set the transition on the container view.
3. Remove the subview from the container view.
4. Add the new subview to the container view.
5. Commit the animation block.

Use of this method is discouraged in iOS 4.0 and later. You should use the [`transition(with:duration:options:animations:completion:)`](uiview/transition(with:duration:options:animations:completion:).md) method to perform transitions instead.

## Parameters

- `transition`: A transition to apply to `view`. Possible values are described in [`UIView.AnimationTransition`](uiview/animationtransition.md).
- `view`: The view to apply the transition to.
- `cache`: If [`true`](https://developer.apple.com/documentation/Swift/true), the before and after images of `view` are rendered once and used to create the frames in the animation. Caching can improve performance but if you set this parameter to [`true`](https://developer.apple.com/documentation/Swift/true), you must not update the view or its subviews during the transition. Updating the view and its subviews may interfere with the caching behaviors and cause the view contents to be rendered incorrectly (or in the wrong location) during the animation. You must wait until the transition ends to update the view. If [`false`](https://developer.apple.com/documentation/Swift/false), the view and its contents must be updated for each frame of the transition animation, which may noticeably affect the frame rate.

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
- [class func setAnimationBeginsFromCurrentState(Bool)](uiview/setanimationbeginsfromcurrentstate(_:).md)
  Sets whether the animation should begin playing from the current state.
- [class var areAnimationsEnabled: Bool](uiview/areanimationsenabled.md)
  Returns a Boolean value indicating whether animations are enabled.
- [func forBaselineLayout() -> UIView](uiview/forbaselinelayout.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationtransition(_:for:cache:))*