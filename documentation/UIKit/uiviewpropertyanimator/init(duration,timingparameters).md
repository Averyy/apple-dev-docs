# init(duration:timingParameters:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes the animator object with a custom timing curve object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(duration: TimeInterval, timingParameters parameters: any UITimingCurveProvider)
```

```objc
- (instancetype) initWithDuration:(NSTimeInterval) duration timingParameters:(id<UITimingCurveProvider>) parameters;
```

## Return Value

An initialized animator object or `nil` if the object could not be created.

## Discussion

Use this method to initialize the animator with a custom timing curve. After initializing the animator, you must add one or more animation blocks before calling starting the animations.

The animator object returned by this method begins in the [`UIViewAnimatingState.inactive`](../uiviewanimatingstate/inactive.md) state. You must explicitly start the animations by calling the [`startAnimation()`](../uiviewanimating/startanimation%28%29.md) method.

## Parameters

- `duration`: The duration of the animation, in seconds.
- `parameters`: The object providing the timing information. This object must adopt the [`UITimingCurveProvider`](../uitimingcurveprovider.md) protocol.

## See Also

### Initializing a property animator
- [convenience init(duration: TimeInterval, curve: UIView.AnimationCurve, animations: (() -> Void)?)](./init%28duration,curve,animations%29.md)
  Initializes the animator with a built-in UIKit timing curve.
- [convenience init(duration: TimeInterval, controlPoint1: CGPoint, controlPoint2: CGPoint, animations: (() -> Void)?)](./init%28duration,controlpoint1,controlpoint2,animations%29.md)
  Initializes the animator object with a cubic Bézier timing curve.
- [convenience init(duration: TimeInterval, dampingRatio: CGFloat, animations: (() -> Void)?)](./init%28duration,dampingratio,animations%29.md)
  Initializes the animator object with spring-based timing information.
- [class func runningPropertyAnimator(withDuration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions, animations: () -> Void, completion: ((UIViewAnimatingPosition) -> Void)?) -> Self](./runningpropertyanimator%28withduration,delay,options,animations,completion%29.md)
  Creates and returns an animator object that begins running its animations immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/init(duration:timingparameters:))*