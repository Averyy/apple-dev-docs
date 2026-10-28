# springTimingParameters

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The spring-based timing parameters to use.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var springTimingParameters: UISpringTimingParameters? { get }
```

```objc
@property (nonatomic, readonly, nullable) UISpringTimingParameters * springTimingParameters;
```

## Discussion

Implement this property and use it to provide spring-based timing information. If the value of the [`timingCurveType`](./timingcurvetype.md) property is [`UITimingCurveType.spring`](../uitimingcurvetype/spring.md) or [`UITimingCurveType.composed`](../uitimingcurvetype/composed.md), you must return an object from this property.

For more information about configuring spring-based timing parameters, see [`UISpringTimingParameters`](../uispringtimingparameters.md).

## See Also

### Getting the timing information
- [var timingCurveType: UITimingCurveType](./timingcurvetype.md)
  The type of timing information to use.
- [var cubicTimingParameters: UICubicTimingParameters?](./cubictimingparameters.md)
  The cubic timing parameters to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitimingcurveprovider/springtimingparameters)*