# init(duration:curve:animations:)

**Framework**: UIKit  
**Kind**: init

Initializes the animator with a built-in UIKit timing curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(duration: TimeInterval, curve: UIView.AnimationCurve, animations: (() -> Void)? = nil)
```

#### Return Value

An initialized animator object or `nil` if the object could not be created.

#### Discussion

Use this method to create an animator object that uses the existing UIKit timing curves to control the animation behavior. Standard UIKit timing curves include [`UIView.AnimationCurve.linear`](uiview/animationcurve/linear.md) and [`UIView.AnimationCurve.easeInOut`](uiview/animationcurve/easeinout.md) among others.

The animator object returned by this method begins in the [`UIViewAnimatingState.inactive`](uiviewanimatingstate/inactive.md) state. You must explicitly start the animations by calling the [`startAnimation()`](uiviewanimating/startanimation().md) method.

## Parameters

- `duration`: The duration of the animation, in seconds.
- `curve`: The UIKit timing curve to apply to the animation.
- `animations`: The block containing the animations. This block has no return value and takes no parameters. Use this block to modify any animatable view properties. When you start the animations, those properties are animated from their current values to the new values using the specified animation parameters.

## See Also

- [convenience init(duration: TimeInterval, controlPoint1: CGPoint, controlPoint2: CGPoint, animations: (() -> Void)?)](uiviewpropertyanimator/init(duration:controlpoint1:controlpoint2:animations:).md)
  Initializes the animator object with a cubic Bézier timing curve.
- [convenience init(duration: TimeInterval, dampingRatio: CGFloat, animations: (() -> Void)?)](uiviewpropertyanimator/init(duration:dampingratio:animations:).md)
  Initializes the animator object with spring-based timing information.
- [init(duration: TimeInterval, timingParameters: any UITimingCurveProvider)](uiviewpropertyanimator/init(duration:timingparameters:).md)
  Initializes the animator object with a custom timing curve object.
- [class func runningPropertyAnimator(withDuration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((UIViewAnimatingPosition) -> Void)?) -> Self](uiviewpropertyanimator/runningpropertyanimator(withduration:delay:options:animations:completion:).md)
  Creates and returns an animator object that begins running its animations immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/init(duration:curve:animations:))*