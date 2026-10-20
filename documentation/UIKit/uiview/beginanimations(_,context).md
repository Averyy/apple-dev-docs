# beginAnimations(_:context:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Marks the beginning of a begin/commit animation block.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use [`animate(withDuration:delay:options:animations:completion:)`](./animate%28withduration,delay,options,animations,completion%29.md) instead.

## Declaration

```swift
class func beginAnimations(_ animationID: String?, context: UnsafeMutableRawPointer?)
```

```objc
+ (void) beginAnimations:(NSString *) animationID context:(void *) context;
```

#### Discussion

This method signals to the system that you want to specify one or more animations to perform. After calling this method, configure the animation options (using the `setAnimation…` class methods) and then change the desired animatable properties of your views. When you are done changing your view properties, call the [`commitAnimations()`](./commitanimations%28%29.md) method to close the set and schedule the animations.

You can nest sets of animations (by calling this method again before committing a previous set of animations) as needed. Nesting animations groups them together and allows you to set different animation options for the nested group.

If you install a start or stop selector using the [`setAnimationWillStart(_:)`](./setanimationwillstart%28_%29.md) or [`setAnimationDidStop(_:)`](./setanimationdidstop%28_%29.md) method, the values you specify for the `animationID` and `context` parameters are passed to your selectors at runtime. You can use these parameters to pass additional information to those selectors.

Use of this method is discouraged in iOS 4.0 and later. You should use the block-based animation methods to specify your animations instead.

## Parameters

- `animationID`: An application-supplied identifier for the animations.
- `context`: Custom data that you want to associate with this set of animations. information that is passed to the animation delegate messages—the selectors set using the [`setAnimationWillStart(_:)`](./setanimationwillstart%28_%29.md) and [`setAnimationDidStop(_:)`](./setanimationdidstop%28_%29.md) methods.

## See Also

### Deprecated methods
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/beginanimations(_:context:))*