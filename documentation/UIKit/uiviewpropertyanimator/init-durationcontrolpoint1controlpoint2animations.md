# init(duration:controlPoint1:controlPoint2:animations:)

**Framework**: UIKit  
**Kind**: init

Initializes the animator object with a cubic Bézier timing curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(duration: TimeInterval, controlPoint1 point1: CGPoint, controlPoint2 point2: CGPoint, animations: (() -> Void)? = nil)
```

#### Return Value

An initialized animator object or `nil` if the object could not be created.

#### Discussion

Use this method to create an animator object using a cubic timing curve whose starting point is (0, 0) and whose end point is (1, 1). The `point1` and `point2` parameters are the control points that define the shape of the resulting Bezier curve. The slope of the curve defines the speed of the animation at different times. Steep slopes cause animations to appear to run faster and shallower slopes cause them to appear to run slower. The following image shows a timing curve where the animations start fast and finish fast but run more slowly through the middle section.

![None](https://docs-assets.developer.apple.com/published/0054ab7fbcfb5dc1810282e7c7d2a202/media-1965739%402x.png)

The animator object returned by this method begins in the [`UIViewAnimatingState.inactive`](uiviewanimatingstate/inactive.md) state. You must explicitly start the animations by calling the [`startAnimation()`](uiviewanimating/startanimation().md) method.

## Parameters

- `duration`: The duration of the animation, in seconds.
- `point1`: The first control point for the cubic Bézier timing curve.
- `point2`: The second control point for the cubic Bézier timing curve.
- `animations`: The block containing the animations. This block has no return value and takes no parameters. Use this block to modify any animatable view properties. When you start the animations, those properties are animated from their current values to the new values using the specified animation parameters.

## See Also

- [convenience init(duration: TimeInterval, curve: UIView.AnimationCurve, animations: (() -> Void)?)](uiviewpropertyanimator/init(duration:curve:animations:).md)
  Initializes the animator with a built-in UIKit timing curve.
- [convenience init(duration: TimeInterval, dampingRatio: CGFloat, animations: (() -> Void)?)](uiviewpropertyanimator/init(duration:dampingratio:animations:).md)
  Initializes the animator object with spring-based timing information.
- [init(duration: TimeInterval, timingParameters: any UITimingCurveProvider)](uiviewpropertyanimator/init(duration:timingparameters:).md)
  Initializes the animator object with a custom timing curve object.
- [class func runningPropertyAnimator(withDuration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((UIViewAnimatingPosition) -> Void)?) -> Self](uiviewpropertyanimator/runningpropertyanimator(withduration:delay:options:animations:completion:).md)
  Creates and returns an animator object that begins running its animations immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/init(duration:controlpoint1:controlpoint2:animations:))*