# animate(withDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Performs a view animation using a timing curve corresponding to the motion of a physical spring.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class func animate(withDuration duration: TimeInterval, delay: TimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options: UIView.AnimationOptions = [], animations: () -> Void, completion: ((Bool) -> Void)? = nil)
```

```objc
+ (void) animateWithDuration:(NSTimeInterval) duration delay:(NSTimeInterval) delay usingSpringWithDamping:(CGFloat) dampingRatio initialSpringVelocity:(CGFloat) velocity options:(UIViewAnimationOptions) options animations:(void (^)()) animations completion:(void (^)(BOOL finished)) completion;
```

## Parameters

- `duration`: The total duration of the animations, measured in seconds. If you specify a negative value or `0`, the changes are made without animating them.
- `delay`: The amount of time (measured in seconds) to wait before beginning the animations. Specify a value of `0` to begin the animations immediately.
- `dampingRatio`: The damping ratio for the spring animation as it approaches its quiescent state.

  To smoothly decelerate the animation without oscillation, use a value of `1`. Employ a damping ratio closer to zero to increase oscillation.
- `velocity`: The initial spring velocity. For smooth start to the animation, match this value to the view’s velocity as it was prior to attachment.

  A value of `1` corresponds to the total animation distance traversed in one second. For example, if the total animation distance is 200 points and you want the start of the animation to match a view velocity of 100 pt/s, use a value of `0.5`.
- `options`: A mask of options indicating how you want to perform the animations. For a list of valid constants, see [`UIView.AnimationOptions`](./animationoptions.md).
- `animations`: A block object containing the changes to commit to the views. This is where you programmatically change any animatable properties of the views in your view hierarchy. This block takes no parameters and has no return value. This parameter must not be `NULL`.
- `completion`: A block object to be executed when the animation sequence ends. This block has no return value and takes a single Boolean argument that indicates whether or not the animations actually finished before the completion handler was called. If the duration of the animation is 0, this block is performed at the beginning of the next run loop cycle. This parameter may be `NULL`.

## See Also

### Animating views
- [static func animate(Animation, changes: () -> Void, completion: (() -> Void)?)](./animate%28_,changes,completion%29.md)
- [class func animate(springDuration: TimeInterval, bounce: CGFloat, initialSpringVelocity: CGFloat, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](./animate%28springduration,bounce,initialspringvelocity,delay,options,animations,completion%29.md)
  Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](./animate%28withduration,delay,options,animations,completion%29.md)
  Animate changes to one or more views using the specified duration, delay, options, and completion handler.
- [class func animate(withDuration: TimeInterval, animations: () -> Void, completion: ((Bool) -> Void)?)](./animate%28withduration,animations,completion%29.md)
  Animate changes to one or more views using the specified duration and completion handler.
- [class func animate(withDuration: TimeInterval, animations: () -> Void)](./animate%28withduration,animations%29.md)
  Animate changes to one or more views using the specified duration.
- [class func transition(with: UIView, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](./transition%28with,duration,options,animations,completion%29.md)
  Creates a transition animation for the specified container view.
- [class func transition(from: UIView, to: UIView, duration: TimeInterval, options: UIView.AnimationOptions, completion: ((Bool) -> Void)?)](./transition%28from,to,duration,options,completion%29.md)
  Creates a transition animation between the specified views using the given parameters.
- [class func animateKeyframes(withDuration: TimeInterval, delay: TimeInterval, options: UIView.KeyframeAnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](./animatekeyframes%28withduration,delay,options,animations,completion%29.md)
  Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [class func addKeyframe(withRelativeStartTime: Double, relativeDuration: Double, animations: () -> Void)](./addkeyframe%28withrelativestarttime,relativeduration,animations%29.md)
  Specifies the timing and animation values for a single frame of a keyframe animation.
- [class func perform(UIView.SystemAnimation, on: [UIView], options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](./perform%28_,on,options,animations,completion%29.md)
  Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [class func performWithoutAnimation(() -> Void)](./performwithoutanimation%28_%29.md)
  Disables a view transition animation.
- [class func modifyAnimations(withRepeatCount: CGFloat, autoreverses: Bool, animations: () -> Void)](./modifyanimations%28withrepeatcount,autoreverses,animations%29.md)
  Repeats the specified animations a specific number of times, optionally running the animation forward and backward.
- [+ animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:](./animatewithspringduration_bounce_initialspringvelocity_delay_options_animations_completion_.md)
  Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/animate(withduration:delay:usingspringwithdamping:initialspringvelocity:options:animations:completion:))*