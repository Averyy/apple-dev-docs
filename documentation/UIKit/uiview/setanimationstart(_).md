# setAnimationStart(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Sets the start time for the current animation block.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use [`animate(withDuration:delay:options:animations:completion:)`](./animate%28withduration,delay,options,animations,completion%29.md) instead.

## Declaration

```swift
class func setAnimationStart(_ startDate: Date)
```

```objc
+ (void) setAnimationStartDate:(NSDate *) startDate;
```

#### Discussion

Call this method between the [`beginAnimations(_:context:)`](./beginanimations%28_,context%29.md) and [`commitAnimations()`](./commitanimations%28%29.md) methods to specify the start time for that set of animations. And call this method prior to changing the animatable properties of your views. (Do not call this method in conjunction with a block-based animation.) If you do not call this method, the start time is set to the value returned by the [`CFAbsoluteTimeGetCurrent()`](../../CoreFoundation/cfabsolutetimegetcurrent%28%29.md) function, which begins the animations as soon as possible.

Use of this method is discouraged in iOS 4.0 and later. You should use the block-based animation methods to specify your animations instead.

## Parameters

- `startDate`: The time to begin the animations.

## See Also

### Deprecated methods
- [class func beginAnimations(String?, context: UnsafeMutableRawPointer?)](./beginanimations%28_,context%29.md)
  Marks the beginning of a begin/commit animation block.
- [class func commitAnimations()](./commitanimations%28%29.md)
  Marks the end of a begin/commit animation block and schedules the animations for execution.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationstart(_:))*