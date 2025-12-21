# areAnimationsEnabled

**Framework**: UIKit  
**Kind**: property

Returns a Boolean value indicating whether animations are enabled.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
class var areAnimationsEnabled: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if animations are enabled; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if animations are enabled; otherwise, it is [`false`](https://developer.apple.com/documentation/Swift/false).

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
- [class func setAnimationTransition(UIView.AnimationTransition, for: UIView, cache: Bool)](uiview/setanimationtransition(_:for:cache:).md)
  Sets a transition to apply to a view during an animation block.
- [func forBaselineLayout() -> UIView](uiview/forbaselinelayout.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/areanimationsenabled)*