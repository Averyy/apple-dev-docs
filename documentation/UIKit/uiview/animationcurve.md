# UIView.AnimationCurve

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the supported animation curves.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum AnimationCurve
```

```c
enum UIViewAnimationCurve : NSInteger;
```

## Topics

### Constants
- [UIView.AnimationCurve.easeInOut](./animationcurve/easeinout.md)
  An ease-in ease-out curve causes the animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing. This is the default curve for most animations.
- [UIView.AnimationCurve.easeIn](./animationcurve/easein.md)
  An ease-in curve causes the animation to begin slowly, and then speed up as it progresses.
- [UIView.AnimationCurve.easeOut](./animationcurve/easeout.md)
  An ease-out curve causes the animation to begin quickly, and then slow down as it completes.
- [UIView.AnimationCurve.linear](./animationcurve/linear.md)
  A linear animation curve causes an animation to occur evenly over its duration.
### Initializers
- [init?(rawValue: Int)](./animationcurve/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIView.AnimationOptions](./animationoptions.md)
  Options for animating views using block objects.
- [UIView.AnimationTransition](./animationtransition.md)
  Animation transition options for use in an animation block object.
- [UIView.SystemAnimation](./systemanimation.md)
  Option to remove the views from the hierarchy when animation is complete.
- [UIView.KeyframeAnimationOptions](./keyframeanimationoptions.md)
  Options for configuring keyframe-based animations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/animationcurve)*