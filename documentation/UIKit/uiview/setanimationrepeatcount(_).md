# setAnimationRepeatCount(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Sets the number of times animations within an animation block repeat.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use [`animate(withDuration:delay:options:animations:completion:)`](./animate%28withduration,delay,options,animations,completion%29.md) instead.

## Declaration

```swift
class func setAnimationRepeatCount(_ repeatCount: Float)
```

```objc
+ (void) setAnimationRepeatCount:(float) repeatCount;
```

## Discussion

Use this method to specify the number of times to repeat the specified animations. This method does nothing if called from outside of an animation block. You can use this method in conjunction with either the block-based methods or the begin/commit methods for defining an animation block. If you do not explicitly set a repeat count, the animation is not repeated.

If you pass the [`repeat`](./animationoptions/repeat.md) option to the [`animate(withDuration:delay:options:animations:completion:)`](./animate%28withduration,delay,options,animations,completion%29.md) method without setting an explicit repeat count, the animation repeats indefinitely. If you want the animation to repeat a finite number of times, call this method from inside your block.

## Parameters

- `repeatCount`: The number of times animations repeat. This value can be a fraction. If you specify the value `0`, the animation is performed once without repeating.

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
- [class func setAnimationRepeatAutoreverses(Bool)](./setanimationrepeatautoreverses%28_%29.md)
  Sets whether the animations within an animation block automatically reverse themselves.
- [class func setAnimationBeginsFromCurrentState(Bool)](./setanimationbeginsfromcurrentstate%28_%29.md)
  Sets whether the animation should begin playing from the current state.
- [class func setAnimationTransition(UIView.AnimationTransition, for: UIView, cache: Bool)](./setanimationtransition%28_,for,cache%29.md)
  Sets a transition to apply to a view during an animation block.
- [class var areAnimationsEnabled: Bool](./areanimationsenabled.md)
  Returns a Boolean value indicating whether animations are enabled.
- [func forBaselineLayout() -> UIView](./forbaselinelayout%28%29.md)
  Returns a view used to satisfy baseline constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationrepeatcount(_:))*