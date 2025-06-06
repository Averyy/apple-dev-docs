# calculationModeCubic

**Framework**: UIKit  
**Kind**: property

The option to compute intermediate frames using a default Catmull-Rom spline that passes through the keyframe values.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static var calculationModeCubic: UIView.KeyframeAnimationOptions { get }
```

#### Discussion

You can’t adjust the parameters of this algorithm.

## See Also

- [static var layoutSubviews: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/layoutsubviews.md)
  The option to lay out subviews at commit time so that they’re animated along with their parent.
- [static var allowUserInteraction: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/allowuserinteraction.md)
  The option that allows a person to interact with views while they’re being animated.
- [static var beginFromCurrentState: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/beginfromcurrentstate.md)
  The option to start an animation from the current setting associated with an already in-flight animation.
- [static var `repeat`: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/repeat.md)
  The option to repeat an animation indefinitely.
- [static var autoreverse: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/autoreverse.md)
  The option to run an animation backwards and forwards.
- [static var overrideInheritedDuration: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/overrideinheritedduration.md)
  The option to force an animation to use the original duration value specified when the animation was submitted.
- [static var overrideInheritedOptions: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/overrideinheritedoptions.md)
  The option to not inherit the animation type or any options.
- [static var calculationModeLinear: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/calculationmodelinear.md)
  The option to use a simple linear calculation when interpolating between keyframe values.
- [static var calculationModeDiscrete: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/calculationmodediscrete.md)
  The option to not interpolate between keyframe values, but rather to jump directly to each new keyframe value.
- [static var calculationModePaced: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/calculationmodepaced.md)
  The option to compute intermediate keyframe values using a simple pacing algorithm.
- [static var calculationModeCubicPaced: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/calculationmodecubicpaced.md)
  The option to compute intermediate frames using the cubic scheme while ignoring the timing properties of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions/calculationmodecubic)*