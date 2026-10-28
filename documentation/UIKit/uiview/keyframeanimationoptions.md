# UIView.KeyframeAnimationOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Options for configuring keyframe-based animations.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct KeyframeAnimationOptions
```

```c
enum UIViewKeyframeAnimationOptions : NSUInteger;
```

## Overview

Use these options with the [`animateKeyframes(withDuration:delay:options:animations:completion:)`](./animatekeyframes%28withduration,delay,options,animations,completion%29.md) method.

## Topics

### Constants
- [static var layoutSubviews: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/layoutsubviews.md)
  The option to lay out subviews at commit time so that they’re animated along with their parent.
- [static var allowUserInteraction: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/allowuserinteraction.md)
  The option that allows a person to interact with views while they’re being animated.
- [static var beginFromCurrentState: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/beginfromcurrentstate.md)
  The option to start an animation from the current setting associated with an already in-flight animation.
- [static var `repeat`: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/repeat.md)
  The option to repeat an animation indefinitely.
- [static var autoreverse: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/autoreverse.md)
  The option to run an animation backwards and forwards.
- [static var overrideInheritedDuration: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/overrideinheritedduration.md)
  The option to force an animation to use the original duration value specified when the animation was submitted.
- [static var overrideInheritedOptions: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/overrideinheritedoptions.md)
  The option to not inherit the animation type or any options.
- [static var calculationModeLinear: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/calculationmodelinear.md)
  The option to use a simple linear calculation when interpolating between keyframe values.
- [static var calculationModeDiscrete: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/calculationmodediscrete.md)
  The option to not interpolate between keyframe values, but rather to jump directly to each new keyframe value.
- [static var calculationModePaced: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/calculationmodepaced.md)
  The option to compute intermediate keyframe values using a simple pacing algorithm.
- [static var calculationModeCubic: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/calculationmodecubic.md)
  The option to compute intermediate frames using a default Catmull-Rom spline that passes through the keyframe values.
- [static var calculationModeCubicPaced: UIView.KeyframeAnimationOptions](./keyframeanimationoptions/calculationmodecubicpaced.md)
  The option to compute intermediate frames using the cubic scheme while ignoring the timing properties of the animation.
### Initializers
- [init(rawValue: UInt)](./keyframeanimationoptions/init%28rawvalue%29.md)
  Creates keyframe animation options with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [UIView.AnimationCurve](./animationcurve.md)
  Specifies the supported animation curves.
- [UIView.AnimationOptions](./animationoptions.md)
  Options for animating views using block objects.
- [UIView.AnimationTransition](./animationtransition.md)
  Animation transition options for use in an animation block object.
- [UIView.SystemAnimation](./systemanimation.md)
  Option to remove the views from the hierarchy when animation is complete.
- [NSLayoutConstraint.Axis](../nslayoutconstraint/axis.md)
  Keys that specify a horizontal or vertical layout constraint between objects.
- [UIView.TintAdjustmentMode](./tintadjustmentmode-swift.enum.md)
  The tint adjustment mode for the view.
- [class let layoutFittingCompressedSize: CGSize](./layoutfittingcompressedsize.md)
  The option to use the smallest possible size.
- [class let layoutFittingExpandedSize: CGSize](./layoutfittingexpandedsize.md)
  The option to use the largest possible size.
- [class let noIntrinsicMetric: CGFloat](./nointrinsicmetric.md)
  The absence of an intrinsic metric for a given numeric view property.
- [UIView.AutoresizingMask](./autoresizingmask-swift.struct.md)
  Options for automatic view resizing.
- [enum UISemanticContentAttribute](../uisemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions)*