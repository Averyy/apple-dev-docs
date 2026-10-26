# animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
+ (void) animateWithSpringDuration:(NSTimeInterval) duration bounce:(CGFloat) bounce initialSpringVelocity:(CGFloat) velocity delay:(NSTimeInterval) delay options:(UIViewAnimationOptions) options animations:(void (^)()) animations completion:(void (^)(BOOL finished)) completion;
```

## See Also

### Animating views
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
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, usingSpringWithDamping: CGFloat, initialSpringVelocity: CGFloat, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](./animate%28withduration,delay,usingspringwithdamping,initialspringvelocity,options,animations,completion%29.md)
  Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [class func performWithoutAnimation(() -> Void)](./performwithoutanimation%28_%29.md)
  Disables a view transition animation.
- [class func modifyAnimations(withRepeatCount: CGFloat, autoreverses: Bool, animations: () -> Void)](./modifyanimations%28withrepeatcount,autoreverses,animations%29.md)
  Repeats the specified animations a specific number of times, optionally running the animation forward and backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/animatewithspringduration:bounce:initialspringvelocity:delay:options:animations:completion:)*