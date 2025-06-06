# UIView.AnimationOptions

**Framework**: UIKit  
**Kind**: struct

Options for animating views using block objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct AnimationOptions
```

## Topics

### Constants
- [static var layoutSubviews: UIView.AnimationOptions](uiview/animationoptions/layoutsubviews.md)
  Lay out subviews at commit time so that they are animated along with their parent.
- [static var allowUserInteraction: UIView.AnimationOptions](uiview/animationoptions/allowuserinteraction.md)
  Allow the user to interact with views while they are being animated.
- [static var beginFromCurrentState: UIView.AnimationOptions](uiview/animationoptions/beginfromcurrentstate.md)
  Start the animation from the current setting associated with an already in-flight animation.
- [static var `repeat`: UIView.AnimationOptions](uiview/animationoptions/repeat.md)
  Repeat the animation indefinitely.
- [static var autoreverse: UIView.AnimationOptions](uiview/animationoptions/autoreverse.md)
  Run the animation backwards and forwards (must be combined with the repeat option).
- [static var overrideInheritedDuration: UIView.AnimationOptions](uiview/animationoptions/overrideinheritedduration.md)
  Force the animation to use the original duration value specified when the animation was submitted.
- [static var overrideInheritedCurve: UIView.AnimationOptions](uiview/animationoptions/overrideinheritedcurve.md)
  Force the animation to use the original curve value specified when the animation was submitted.
- [static var allowAnimatedContent: UIView.AnimationOptions](uiview/animationoptions/allowanimatedcontent.md)
  Animate the views by changing the property values dynamically and redrawing the view.
- [static var showHideTransitionViews: UIView.AnimationOptions](uiview/animationoptions/showhidetransitionviews.md)
  Hide or show views during a view transition.
- [static var overrideInheritedOptions: UIView.AnimationOptions](uiview/animationoptions/overrideinheritedoptions.md)
  The option to not inherit the animation type or any options.
- [static var curveEaseInOut: UIView.AnimationOptions](uiview/animationoptions/curveeaseinout.md)
  Specify an ease-in ease-out curve, which causes the animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [static var curveEaseIn: UIView.AnimationOptions](uiview/animationoptions/curveeasein.md)
  An ease-in curve causes the animation to begin slowly, and then speed up as it progresses.
- [static var curveEaseOut: UIView.AnimationOptions](uiview/animationoptions/curveeaseout.md)
  An ease-out curve causes the animation to begin quickly, and then slow as it completes.
- [static var curveLinear: UIView.AnimationOptions](uiview/animationoptions/curvelinear.md)
  A linear animation curve causes an animation to occur evenly over its duration.
- [static var transitionFlipFromLeft: UIView.AnimationOptions](uiview/animationoptions/transitionflipfromleft.md)
  A transition that flips a view around its vertical axis from left to right (the left side of the view moves toward the front and right side toward the back).
- [static var transitionFlipFromRight: UIView.AnimationOptions](uiview/animationoptions/transitionflipfromright.md)
  A transition that flips a view around its vertical axis from right to left (the right side of the view moves toward the front and left side toward the back).
- [static var transitionCurlUp: UIView.AnimationOptions](uiview/animationoptions/transitioncurlup.md)
  A transition that curls a view up from the bottom.
- [static var transitionCurlDown: UIView.AnimationOptions](uiview/animationoptions/transitioncurldown.md)
  A transition that curls a view down from the top.
- [static var transitionCrossDissolve: UIView.AnimationOptions](uiview/animationoptions/transitioncrossdissolve.md)
  A transition that dissolves from one view to the next.
- [static var transitionFlipFromTop: UIView.AnimationOptions](uiview/animationoptions/transitionflipfromtop.md)
  A transition that flips a view around its horizontal axis from top to bottom (the top side of the view moves toward the front and the bottom side toward the back).
- [static var transitionFlipFromBottom: UIView.AnimationOptions](uiview/animationoptions/transitionflipfrombottom.md)
  A transition that flips a view around its horizontal axis from bottom to top (the bottom side of the view moves toward the front and the top side toward the back).
- [static var preferredFramesPerSecond30: UIView.AnimationOptions](uiview/animationoptions/preferredframespersecond30.md)
  A frame rate of 30 frames per second.
- [static var preferredFramesPerSecond60: UIView.AnimationOptions](uiview/animationoptions/preferredframespersecond60.md)
  A frame rate of 60 frames per second.
### Initializers
- [init(rawValue: UInt)](uiview/animationoptions/init(rawvalue:).md)
  Creates an animation options structure with the specified raw value.

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
- [enum UISemanticContentAttribute](uisemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/animationoptions)*