# timingCurveType

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The type of timing information to use.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var timingCurveType: UITimingCurveType { get }
```

#### Discussion

Use this property to specify the type of timing information your timing curve object supplies. The value of this property determines whether the view property animator uses the object in the [`cubicTimingParameters`](uitimingcurveprovider/cubictimingparameters.md) or [`springTimingParameters`](uitimingcurveprovider/springtimingparameters.md) property for timing information.

## See Also

- [var cubicTimingParameters: UICubicTimingParameters?](uitimingcurveprovider/cubictimingparameters.md)
  The cubic timing parameters to use.
- [var springTimingParameters: UISpringTimingParameters?](uitimingcurveprovider/springtimingparameters.md)
  The spring-based timing parameters to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitimingcurveprovider/timingcurvetype)*