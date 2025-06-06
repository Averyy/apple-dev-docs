# UISemanticContentAttribute

**Framework**: UIKit  
**Kind**: enum

A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum UISemanticContentAttribute
```

## Topics

### Constants
- [UISemanticContentAttribute.unspecified](uisemanticcontentattribute/unspecified.md)
  The default value for views.
- [UISemanticContentAttribute.playback](uisemanticcontentattribute/playback.md)
  A view representing the playback controls, such as Play, Rewind, or Fast Forward buttons or playhead scrubbers.
- [UISemanticContentAttribute.spatial](uisemanticcontentattribute/spatial.md)
  A view representing a directional control, such as a segment control for text alignment, or a D-pad control for a game.
- [UISemanticContentAttribute.forceLeftToRight](uisemanticcontentattribute/forcelefttoright.md)
  A view that’s always displayed using a left-to-right layout.
- [UISemanticContentAttribute.forceRightToLeft](uisemanticcontentattribute/forcerighttoleft.md)
  A view that’s always displayed using a right-to-left layout.
### Initializers
- [init?(rawValue: Int)](uisemanticcontentattribute/init(rawvalue:).md)

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
- [UIView.AnimationTransition](uiview/animationtransition.md)
  Animation transition options for use in an animation block object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute)*