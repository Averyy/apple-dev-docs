# timingCurveType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
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
var timingCurveType: UITimingCurveType { get }
```

```objc
@property (nonatomic, readonly) UITimingCurveType timingCurveType;
```

## Discussion

Use this property to specify the type of timing information your timing curve object supplies. The value of this property determines whether the view property animator uses the object in the [`cubicTimingParameters`](./cubictimingparameters.md) or [`springTimingParameters`](./springtimingparameters.md) property for timing information.

## See Also

### Getting the timing information
- [var cubicTimingParameters: UICubicTimingParameters?](./cubictimingparameters.md)
  The cubic timing parameters to use.
- [var springTimingParameters: UISpringTimingParameters?](./springtimingparameters.md)
  The spring-based timing parameters to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitimingcurveprovider/timingcurvetype)*