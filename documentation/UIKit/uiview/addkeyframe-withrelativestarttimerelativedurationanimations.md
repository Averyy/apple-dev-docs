# addKeyframe(withRelativeStartTime:relativeDuration:animations:)

**Framework**: UIKit  
**Kind**: method

Specifies the timing and animation values for a single frame of a keyframe animation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func addKeyframe(withRelativeStartTime frameStartTime: Double, relativeDuration frameDuration: Double, animations: @escaping () -> Void)
```

#### Discussion

To animate view properties during a keyframe animation, call this method from within the animation block you pass to the [`animateKeyframes(withDuration:delay:options:animations:completion:)`](uiview/animatekeyframes(withduration:delay:options:animations:completion:).md) method. To animate between different values, or to tweak the timing of your view property animations, you can call this method multiple times within a block.

The view properties you change in the `animations` block animate over the timespan you specify in `frameDuration` parameter. The properties do not begin animating until the time you specify in the `frameStartTime` parameter. After the frame start time, the animation executes over its specified duration or until interrupted by another animation.

## Parameters

- `frameStartTime`: The time at which to start the specified animations. This value must be in the range   to  , where   represents the start of the overall animation and   represents the end of the overall animation. For example, for an animation that is two seconds in duration, specifying a start time of   causes the animations to begin executing one second after the start of the overall animation.
- `frameDuration`: The length of time over which to animate to the specified value. This value must be in the range   to   and indicates the amount of time relative to the overall animation length. If you specify a value of  , any properties you set in the   block update immediately at the specified start time. If you specify a nonzero value, the properties animate over that amount of time. For example, for an animation that is two seconds in duration, specifying a duration of   results in an animation duration of one second.
- `animations`: A block object containing the animations you want to perform. This is where you programmatically change any animatable properties of the views in your view hierarchy. This block takes no parameters and has no return value. This parameter must not be  .

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
- [class func transition(with: UIView, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiview/transition(with:duration:options:animations:completion:).md)
  Creates a transition animation for the specified container view.
- [class func transition(from: UIView, to: UIView, duration: TimeInterval, options: UIView.AnimationOptions, completion: ((Bool) -> Void)?)](uiview/transition(from:to:duration:options:completion:).md)
  Creates a transition animation between the specified views using the given parameters.
- [class func animateKeyframes(withDuration: TimeInterval, delay: TimeInterval, options: UIView.KeyframeAnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animatekeyframes(withduration:delay:options:animations:completion:).md)
  Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [class func perform(UIView.SystemAnimation, on: [UIView], options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiview/perform(_:on:options:animations:completion:).md)
  Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [class func animate(withDuration: TimeInterval, delay: TimeInterval, usingSpringWithDamping: CGFloat, initialSpringVelocity: CGFloat, options: UIView.AnimationOptions, animations: () -> Void, completion: ((Bool) -> Void)?)](uiview/animate(withduration:delay:usingspringwithdamping:initialspringvelocity:options:animations:completion:).md)
  Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [class func performWithoutAnimation(() -> Void)](uiview/performwithoutanimation(_:).md)
  Disables a view transition animation.
- [class func modifyAnimations(withRepeatCount: CGFloat, autoreverses: Bool, animations: () -> Void)](uiview/modifyanimations(withrepeatcount:autoreverses:animations:).md)
  Repeats the specified animations a specific number of times, optionally running the animation forward and backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addkeyframe(withrelativestarttime:relativeduration:animations:))*