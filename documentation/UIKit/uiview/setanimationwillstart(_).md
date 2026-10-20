# setAnimationWillStart(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Sets the message to send to the animation delegate when the animation starts.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use [`animate(withDuration:delay:options:animations:completion:)`](./animate%28withduration,delay,options,animations,completion%29.md) instead.

## Declaration

```swift
class func setAnimationWillStart(_ selector: Selector?)
```

```objc
+ (void) setAnimationWillStartSelector:(SEL) selector;
```

#### Discussion

If you specify an animation delegate for a begin/commit set of animations, you use this method to specify the selector to call before the animations begin. This method does nothing if called from outside of an animation block. It must be called between calls to the [`beginAnimations(_:context:)`](./beginanimations%28_,context%29.md) and [`commitAnimations()`](./commitanimations%28%29.md) methods. This selector is set to `NULL` by default.

> **Note**:  Your start selector is not called if animations are disabled.

Use of this method is discouraged in iOS 4.0 and later. If you are using the block-based animation methods, you can include your delegate’s start code directly inside your block.

## Parameters

- `selector`: The message to send to the animation delegate before animations start. The default value is `NULL`. This selector should be of the form: `- (void)animationDidStart:(NSString *)animationID context:(void *)context`. Your method must take the following arguments:

  - `animationID`

  An [`NSString`](../../Foundation/nsstring.md) containing an optional application-supplied identifier. This is the identifier string that is passed to the [`beginAnimations(_:context:)`](./beginanimations%28_,context%29.md) method. This argument can be `nil`.

  - `context`

  An optional application-supplied context. This is the context data passed to the [`beginAnimations(_:context:)`](./beginanimations%28_,context%29.md) method. This argument can be `nil`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setanimationwillstart(_:))*