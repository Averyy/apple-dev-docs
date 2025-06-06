# cubicTimingParameters

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The cubic timing parameters to use.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var cubicTimingParameters: UICubicTimingParameters? { get }
```

#### Discussion

Implement this property and use it to provide your custom cubic timing information. If the value of the [`timingCurveType`](uitimingcurveprovider/timingcurvetype.md) property is [`UITimingCurveType.builtin`](uitimingcurvetype/builtin.md), [`UITimingCurveType.cubic`](uitimingcurvetype/cubic.md), or [`UITimingCurveType.composed`](uitimingcurvetype/composed.md), you must return an object from this property. The object you return can specify one of the built-in UIKit curves, such as [`UIView.AnimationCurve.linear`](uiview/animationcurve/linear.md), or it can specify a timing curve based on a custom Bézier path.

For more information about configuring this object, see [`UICubicTimingParameters`](uicubictimingparameters.md).

## See Also

- [var timingCurveType: UITimingCurveType](uitimingcurveprovider/timingcurvetype.md)
  The type of timing information to use.
- [var springTimingParameters: UISpringTimingParameters?](uitimingcurveprovider/springtimingparameters.md)
  The spring-based timing parameters to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitimingcurveprovider/cubictimingparameters)*