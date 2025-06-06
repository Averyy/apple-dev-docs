# UIView.AnimationTransition

**Framework**: UIKit  
**Kind**: enum

Animation transition options for use in an animation block object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum AnimationTransition
```

## Topics

### Constants
- [UIView.AnimationTransition.none](uiview/animationtransition/none.md)
  The option for indicating that no transition is specified.
- [UIView.AnimationTransition.flipFromLeft](uiview/animationtransition/flipfromleft.md)
  A transition that flips a view around a vertical axis from left to right. The left side of the view moves towards the front and right side towards the back.
- [UIView.AnimationTransition.flipFromRight](uiview/animationtransition/flipfromright.md)
  A transition that flips a view around a vertical axis from right to left. The right side of the view moves towards the front and left side towards the back.
- [UIView.AnimationTransition.curlUp](uiview/animationtransition/curlup.md)
  A transition that curls a view up from the bottom.
- [UIView.AnimationTransition.curlDown](uiview/animationtransition/curldown.md)
  A transition that curls a view down from the top.
### Initializers
- [init?(rawValue: Int)](uiview/animationtransition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIView.AnimationCurve](uiview/animationcurve.md)
  Specifies the supported animation curves.
- [UIView.AnimationOptions](uiview/animationoptions.md)
  Options for animating views using block objects.
- [UIView.SystemAnimation](uiview/systemanimation.md)
  Option to remove the views from the hierarchy when animation is complete.
- [UIView.KeyframeAnimationOptions](uiview/keyframeanimationoptions.md)
  Options for configuring keyframe-based animations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/animationtransition)*