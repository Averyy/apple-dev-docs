# UIView.KeyframeAnimationOptions

**Framework**: UIKit  
**Kind**: struct

Options for configuring keyframe-based animations.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct KeyframeAnimationOptions
```

#### Overview

Use these options with the [`animateKeyframes(withDuration:delay:options:animations:completion:)`](uiview/animatekeyframes(withduration:delay:options:animations:completion:).md) method.

## Topics

### Constants
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
- [static var calculationModeCubic: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/calculationmodecubic.md)
  The option to compute intermediate frames using a default Catmull-Rom spline that passes through the keyframe values.
- [static var calculationModeCubicPaced: UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions/calculationmodecubicpaced.md)
  The option to compute intermediate frames using the cubic scheme while ignoring the timing properties of the animation.
### Initializers
- [init(rawValue: UInt)](uiview/keyframeanimationoptions/init(rawvalue:).md)
  Creates keyframe animation options with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [UIView.AnimationCurve](uiview/animationcurve.md)
  Specifies the supported animation curves.
- [UIView.AnimationOptions](uiview/animationoptions.md)
  Options for animating views using block objects.
- [UIView.AnimationTransition](uiview/animationtransition.md)
  Animation transition options for use in an animation block object.
- [UIView.SystemAnimation](uiview/systemanimation.md)
  Option to remove the views from the hierarchy when animation is complete.
- [NSLayoutConstraint.Axis](nslayoutconstraint/axis.md)
  Keys that specify a horizontal or vertical layout constraint between objects.
- [UIView.TintAdjustmentMode](uiview/tintadjustmentmode-swift.enum.md)
  The tint adjustment mode for the view.
- [class let layoutFittingCompressedSize: CGSize](uiview/layoutfittingcompressedsize.md)
  The option to use the smallest possible size.
- [class let layoutFittingExpandedSize: CGSize](uiview/layoutfittingexpandedsize.md)
  The option to use the largest possible size.
- [class let noIntrinsicMetric: CGFloat](uiview/nointrinsicmetric.md)
  The absence of an intrinsic metric for a given numeric view property.
- [UIView.AutoresizingMask](uiview/autoresizingmask-swift.struct.md)
  Options for automatic view resizing.
- [enum UISemanticContentAttribute](uisemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions)*