# UIView.TintAdjustmentMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The tint adjustment mode for the view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum TintAdjustmentMode
```

```c
enum UIViewTintAdjustmentMode : NSInteger;
```

## Topics

### Constants
- [UIView.TintAdjustmentMode.automatic](./tintadjustmentmode-swift.enum/automatic.md)
  The tint adjustment mode of the view is the same as its superview’s tint adjustment mode (or `UIViewTintAdjustmentModeNormal` if the view has no superview).
- [UIView.TintAdjustmentMode.normal](./tintadjustmentmode-swift.enum/normal.md)
  The view’s tint color property returns the completely unmodified tint color of the view.
- [UIView.TintAdjustmentMode.dimmed](./tintadjustmentmode-swift.enum/dimmed.md)
  The view’s tint color property returns a desaturated, dimmed version of the view’s original tint color.
### Initializers
- [init?(rawValue: Int)](./tintadjustmentmode-swift.enum/init%28rawvalue%29.md)

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
- [UIView.AnimationCurve](./animationcurve.md)
  Specifies the supported animation curves.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/tintadjustmentmode-swift.enum)*