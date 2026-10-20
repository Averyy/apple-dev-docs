# perform(_:on:options:animations:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class func perform(_ animation: UIView.SystemAnimation, on views: [UIView], options: UIView.AnimationOptions = [], animations parallelAnimations: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

```objc
+ (void) performSystemAnimation:(UISystemAnimation) animation onViews:(NSArray<__kindof UIView *> *) views options:(UIViewAnimationOptions) options animations:(void (^)()) parallelAnimations completion:(void (^)(BOOL finished)) completion;
```

## Parameters

- `animation`: The system animation to perform; a constant from the [`UIView.SystemAnimation`](./systemanimation.md) enum.
- `views`: The views to perform the animations on.
- `options`: A mask of options indicating how you want to perform the animations. For a list of valid constants, see [`UIView.AnimationOptions`](./animationoptions.md).
- `parallelAnimations`: Additional animations you specify to run alongside the system animation, with the same timing and duration that the system animation defines or inherits.

  In your additional animations, do not modify properties of the view on which the system animation is being performed.
- `completion`: A block object to be executed when the animation sequence ends. The single Boolean argument indicates whether or not the animations finished before the completion handler was called. If the animation duration is `0`, this block is performed at the beginning of the next run-loop cycle. You can use a `nil` value for this parameter.

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
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, usingSpringWithDamping: CGFloat, initialSpringVelocity: CGFloat, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](./animate%28withduration,delay,usingspringwithdamping,initialspringvelocity,options,animations,completion%29.md)
  Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [class func performWithoutAnimation(() -> Void)](./performwithoutanimation%28_%29.md)
  Disables a view transition animation.
- [class func modifyAnimations(withRepeatCount: CGFloat, autoreverses: Bool, animations: () -> Void)](./modifyanimations%28withrepeatcount,autoreverses,animations%29.md)
  Repeats the specified animations a specific number of times, optionally running the animation forward and backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/perform(_:on:options:animations:completion:))*