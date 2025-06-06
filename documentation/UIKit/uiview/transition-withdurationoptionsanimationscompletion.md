# transition(with:duration:options:animations:completion:)

**Framework**: UIKit  
**Kind**: method

Creates a transition animation for the specified container view.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func transition(with view: UIView, duration: TimeInterval, options: UIView.AnimationOptions = [], animations: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

#### Discussion

This method applies a transition to the specified view so that you can make state changes to it. The block you specify in the `animations` parameter contains whatever state changes you want to make. You can use this block to add, remove, show, or hide subviews of the specified view. If you want to incorporate other animatable changes, you must include the [`allowAnimatedContent`](uiview/animationoptions/allowanimatedcontent.md) key in the `options` parameter.

The following code creates a flip transition for the specified container view. At the appropriate point in the transition, one subview is removed and another is added to the container view. This makes it look as if a new view was flipped into place with the new subview, but really it is just the same view animated back into place with a new configuration.

```objc
[UIView transitionWithView:containerView
           duration:0.2
           options:UIViewAnimationOptionTransitionFlipFromLeft
           animations:^{ [fromView removeFromSuperview]; [containerView addSubview:toView]; }
           completion:NULL];
```

During an animation, user interactions are temporarily disabled for the views being animated. (Prior to iOS 5, user interactions are disabled for the entire application.) If you want users to be able to interact with the views, include the [`allowUserInteraction`](uiview/animationoptions/allowuserinteraction.md) constant in the `options` parameter.

## Parameters

- `view`: The container view that performs the transition.
- `duration`: The duration of the transition animation, measured in seconds. If you specify a negative value or  , the transition is made without animations.
- `options`: A mask of options indicating how you want to perform the animations. For a list of valid constants, see  .
- `animations`: A block object that contains the changes you want to make to the specified view. This block takes no parameters and has no return value. This parameter must not be  .
- `completion`: A block object to be executed when the animation sequence ends. This block has no return value and takes a single Boolean argument that indicates whether or not the animations actually finished before the completion handler was called. If the duration of the animation is 0, this block is performed at the beginning of the next run loop cycle. This parameter may be  .

## See Also

- [static func animate(with: Animation, changes: () -> Void, completion: (() -> Void)?)](uiview/animate(with:changes:completion:).md)
  Animates changes to one or more views using the specified SwiftUI animation.
- [class func animate(springDuration: TimeInterval, bounce: CGFloat, initialSpringVelocity: CGFloat, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(springduration:bounce:initialspringvelocity:delay:options:animations:completion:).md)
  Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(withduration:delay:options:animations:completion:).md)
  Animate changes to one or more views using the specified duration, delay, options, and completion handler.
- [class func animate(withDuration: TimeInterval, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(withduration:animations:completion:).md)
  Animate changes to one or more views using the specified duration and completion handler.
- [class func animate(withDuration: TimeInterval, animations: () -> Void)](uiview/animate(withduration:animations:).md)
  Animate changes to one or more views using the specified duration.
- [class func transition(from: UIView, to: UIView, duration: TimeInterval, options: UIView.AnimationOptions, completion: ((Bool) -> Void)?)](uiview/transition(from:to:duration:options:completion:).md)
  Creates a transition animation between the specified views using the given parameters.
- [class func animateKeyframes(withDuration: TimeInterval, delay: TimeInterval, options: UIView.KeyframeAnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animatekeyframes(withduration:delay:options:animations:completion:).md)
  Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [class func addKeyframe(withRelativeStartTime: Double, relativeDuration: Double, animations: () -> Void)](uiview/addkeyframe(withrelativestarttime:relativeduration:animations:).md)
  Specifies the timing and animation values for a single frame of a keyframe animation.
- [class func perform(UIView.SystemAnimation, on: [UIView], options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiview/perform(_:on:options:animations:completion:).md)
  Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, usingSpringWithDamping: CGFloat, initialSpringVelocity: CGFloat, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(withduration:delay:usingspringwithdamping:initialspringvelocity:options:animations:completion:).md)
  Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [class func performWithoutAnimation(() -> Void)](uiview/performwithoutanimation(_:).md)
  Disables a view transition animation.
- [class func modifyAnimations(withRepeatCount: CGFloat, autoreverses: Bool, animations: () -> Void)](uiview/modifyanimations(withrepeatcount:autoreverses:animations:).md)
  Repeats the specified animations a specific number of times, optionally running the animation forward and backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/transition(with:duration:options:animations:completion:))*