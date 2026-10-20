# UIView.AutoresizingMask

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Options for automatic view resizing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct AutoresizingMask
```

```c
enum UIViewAutoresizing : NSUInteger;
```

## Topics

### Constants
- [static var flexibleLeftMargin: UIView.AutoresizingMask](./autoresizingmask-swift.struct/flexibleleftmargin.md)
  Resizing performed by expanding or shrinking a view in the direction of the left margin.
- [static var flexibleWidth: UIView.AutoresizingMask](./autoresizingmask-swift.struct/flexiblewidth.md)
  Resizing performed by expanding or shrinking a view’s width.
- [static var flexibleRightMargin: UIView.AutoresizingMask](./autoresizingmask-swift.struct/flexiblerightmargin.md)
  Resizing performed by expanding or shrinking a view in the direction of the right margin.
- [static var flexibleTopMargin: UIView.AutoresizingMask](./autoresizingmask-swift.struct/flexibletopmargin.md)
  Resizing performed by expanding or shrinking a view in the direction of the top margin.
- [static var flexibleHeight: UIView.AutoresizingMask](./autoresizingmask-swift.struct/flexibleheight.md)
  Resizing performed by expanding or shrinking a view’s height.
- [static var flexibleBottomMargin: UIView.AutoresizingMask](./autoresizingmask-swift.struct/flexiblebottommargin.md)
  Resizing performed by expanding or shrinking a view in the direction of the bottom margin.
### Initializers
- [init(rawValue: UInt)](./autoresizingmask-swift.struct/init%28rawvalue%29.md)
  Creates an autoresizing mask structure with the specified raw value.

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
- [enum UISemanticContentAttribute](../uisemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/autoresizingmask-swift.struct)*