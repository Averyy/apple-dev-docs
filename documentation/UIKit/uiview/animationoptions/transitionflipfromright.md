# transitionFlipFromRight

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A transition that flips a view around its vertical axis from right to left (the right side of the view moves toward the front and left side toward the back).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var transitionFlipFromRight: UIView.AnimationOptions { get }
```

```c
UIViewAnimationOptionTransitionFlipFromRight
```

## See Also

### Constants
- [static var layoutSubviews: UIView.AnimationOptions](./layoutsubviews.md)
  Lay out subviews at commit time so that they are animated along with their parent.
- [static var allowUserInteraction: UIView.AnimationOptions](./allowuserinteraction.md)
  Allow the user to interact with views while they are being animated.
- [static var beginFromCurrentState: UIView.AnimationOptions](./beginfromcurrentstate.md)
  Start the animation from the current setting associated with an already in-flight animation.
- [static var `repeat`: UIView.AnimationOptions](./repeat.md)
  Repeat the animation indefinitely.
- [static var autoreverse: UIView.AnimationOptions](./autoreverse.md)
  Run the animation backwards and forwards (must be combined with the repeat option).
- [static var overrideInheritedDuration: UIView.AnimationOptions](./overrideinheritedduration.md)
  Force the animation to use the original duration value specified when the animation was submitted.
- [static var overrideInheritedCurve: UIView.AnimationOptions](./overrideinheritedcurve.md)
  Force the animation to use the original curve value specified when the animation was submitted.
- [static var allowAnimatedContent: UIView.AnimationOptions](./allowanimatedcontent.md)
  Animate the views by changing the property values dynamically and redrawing the view.
- [static var showHideTransitionViews: UIView.AnimationOptions](./showhidetransitionviews.md)
  Hide or show views during a view transition.
- [static var overrideInheritedOptions: UIView.AnimationOptions](./overrideinheritedoptions.md)
  The option to not inherit the animation type or any options.
- [static var curveEaseInOut: UIView.AnimationOptions](./curveeaseinout.md)
  Specify an ease-in ease-out curve, which causes the animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [static var curveEaseIn: UIView.AnimationOptions](./curveeasein.md)
  An ease-in curve causes the animation to begin slowly, and then speed up as it progresses.
- [static var curveEaseOut: UIView.AnimationOptions](./curveeaseout.md)
  An ease-out curve causes the animation to begin quickly, and then slow as it completes.
- [static var curveLinear: UIView.AnimationOptions](./curvelinear.md)
  A linear animation curve causes an animation to occur evenly over its duration.
- [static var transitionFlipFromLeft: UIView.AnimationOptions](./transitionflipfromleft.md)
  A transition that flips a view around its vertical axis from left to right (the left side of the view moves toward the front and right side toward the back).
- [UIViewAnimationOptionTransitionNone](../../uiviewanimationoptions/uiviewanimationoptiontransitionnone.md)
  No transition is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/animationoptions/transitionflipfromright)*