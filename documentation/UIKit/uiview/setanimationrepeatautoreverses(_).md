# setAnimationRepeatAutoreverses(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Sets whether the animations within an animation block automatically reverse themselves.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use [`animate(withDuration:delay:options:animations:completion:)`](./animate%28withduration,delay,options,animations,completion%29.md) instead.

## Declaration

```swift
class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)
```

```objc
+ (void) setAnimationRepeatAutoreverses:(BOOL) repeatAutoreverses;
```

## Discussion

If you enable autoreversing, a single animation cycle changes the properties being animated to their new values and then back to their original values. At the end of the animations, the affected views are then updated immediately to reflect the new values. This method does nothing if called from outside of an animation block. By default, autoreversing is disabled.

If you combine autoreversing with a repeat count (settable using the [`setAnimationRepeatCount(_:)`](./setanimationrepeatcount%28_%29.md) method), you can create animations that shift back and forth between the old and new values the specified number of times. However, remember that the repeat count indicates the number of complete cycles. If you specify an integral value such as `2.0`, the animation ends on the old value, which is followed by the view immediately updating itself to show the new value, which might be jarring. If you want the animation to end on the new value (instead of the old value), add `0.5` to the repeat count value. This adds an extra half cycle to the animation.

Use of this method is discouraged in iOS 4.0 and later. Instead, you should use the[`animate(withDuration:delay:options:animations:completion:)`](./animate%28withduration,delay,options,animations,completion%29.md) method to specify your animations and the animation options.

## Parameters

- `repeatAutoreverses`: Specify [`true`](../../Swift/true.md) to enable autoreversing or [`false`](../../Swift/false.md) to disable it.

## See Also

### Deprecated methods
- [class func beginAnimations(String?, context: UnsafeMutableRawPointer?)](./beginanimations%28_,context%29.md)
  Marks the beginning of a begin/commit animation block.
- [class func commitAnimations()](./commitanimations%28%29.md)
  Marks the end of a begin/commit animation block and schedules the animations for execution.
- [class func setAnimationStart(Date)](./setanimationstart%28_%29.md)
  Sets the start time for the current animation block.
- [class func setAnimationsEnabled(Bool)](./setanimationsenabled%28_%29.md)
  Sets whether animations are enabled.
- [class func setAnimationDelegate(Any?)](./setanimationdelegate%28_%29.md)
  Sets the delegate for any animation messages.
- [class func setAnimationWillStart(Selector?)](./setanimationwillstart%28_%29.md)
  Sets the message to send to the animation delegate when the animation starts.
- [class func setAnimationDidStop(Selector?)](./setanimationdidstop%28_%29.md)
  Sets the message to send to the animation delegate when animation stops.
- [class func setAnimationDuration(TimeInterval)](./setanimationduration%28_%29.md)
  Sets the duration (measured in seconds) of the animations in an animation block.
- [class func setAnimationDelay(TimeInterval)](./setanimationdelay%28_%29.md)
  Sets the amount of time (in seconds) to wait before animating property changes within an animation block.
- [class func setAnimationCurve(UIView.AnimationCurve)](./setanimationcurve%28_%29.md)
  Sets the curve to use when animating property changes within an animation block.
- [class func setAnimationRepeatCount(Float)](./setanimationrepeatcount%28_%29.md)
  Sets the number of times animations within an animation block repeat.
- [class func setAnimationBeginsFromCurrentState(Bool)](./setanimationbeginsfromcurrentstate%28_%29.md)
  Sets whether the animation should begin playing from the current state.
- [class func setAnimationTransition(UIView.AnimationTransition, for: UIView, cache: Bool)](./setanimationtransition%28_,for,cache%29.md)
  Sets a transition to apply to a view during an animation block.
- [class var areAnimationsEnabled: Bool](./areanimationsenabled.md)
  Returns a Boolean value indicating whether animations are enabled.
- [func forBaselineLayout() -> UIView](./forbaselinelayout%28%29.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationrepeatautoreverses(_:))*