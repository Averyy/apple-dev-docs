# repeat

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The option to repeat an animation indefinitely.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var `repeat`: UIView.KeyframeAnimationOptions { get }
```

```c
UIViewKeyframeAnimationOptionRepeat
```

## See Also

### Constants
- [static var layoutSubviews: UIView.KeyframeAnimationOptions](./layoutsubviews.md)
  The option to lay out subviews at commit time so that they’re animated along with their parent.
- [static var allowUserInteraction: UIView.KeyframeAnimationOptions](./allowuserinteraction.md)
  The option that allows a person to interact with views while they’re being animated.
- [static var beginFromCurrentState: UIView.KeyframeAnimationOptions](./beginfromcurrentstate.md)
  The option to start an animation from the current setting associated with an already in-flight animation.
- [static var autoreverse: UIView.KeyframeAnimationOptions](./autoreverse.md)
  The option to run an animation backwards and forwards.
- [static var overrideInheritedDuration: UIView.KeyframeAnimationOptions](./overrideinheritedduration.md)
  The option to force an animation to use the original duration value specified when the animation was submitted.
- [static var overrideInheritedOptions: UIView.KeyframeAnimationOptions](./overrideinheritedoptions.md)
  The option to not inherit the animation type or any options.
- [static var calculationModeLinear: UIView.KeyframeAnimationOptions](./calculationmodelinear.md)
  The option to use a simple linear calculation when interpolating between keyframe values.
- [static var calculationModeDiscrete: UIView.KeyframeAnimationOptions](./calculationmodediscrete.md)
  The option to not interpolate between keyframe values, but rather to jump directly to each new keyframe value.
- [static var calculationModePaced: UIView.KeyframeAnimationOptions](./calculationmodepaced.md)
  The option to compute intermediate keyframe values using a simple pacing algorithm.
- [static var calculationModeCubic: UIView.KeyframeAnimationOptions](./calculationmodecubic.md)
  The option to compute intermediate frames using a default Catmull-Rom spline that passes through the keyframe values.
- [static var calculationModeCubicPaced: UIView.KeyframeAnimationOptions](./calculationmodecubicpaced.md)
  The option to compute intermediate frames using the cubic scheme while ignoring the timing properties of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/repeat)*