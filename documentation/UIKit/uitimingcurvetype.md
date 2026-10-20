# UITimingCurveType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of timing information to use.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum UITimingCurveType
```

```c
enum UITimingCurveType : NSInteger;
```

## Topics

### Constants
- [UITimingCurveType.builtin](./uitimingcurvetype/builtin.md)
  Use the built-in UIKit timing curves. Specify this value when you want to use one of the constants in the [`UIView.AnimationCurve`](./uiview/animationcurve.md) type. Specify the desired curve using the [`cubicTimingParameters`](./uitimingcurveprovider/cubictimingparameters.md) property.
- [UITimingCurveType.cubic](./uitimingcurvetype/cubic.md)
  Use a custom cubic Bézier curve. Specify the curve information using the [`cubicTimingParameters`](./uitimingcurveprovider/cubictimingparameters.md) property.
- [UITimingCurveType.spring](./uitimingcurvetype/spring.md)
  Use a custom spring animation. Specify the desired curve using the [`springTimingParameters`](./uitimingcurveprovider/springtimingparameters.md) property.
- [UITimingCurveType.composed](./uitimingcurvetype/composed.md)
  Use a combination of timing parameters. This type of curve starts with the curve defined by the [`cubicTimingParameters`](./uitimingcurveprovider/cubictimingparameters.md) property and modifies it using the spring information in the [`springTimingParameters`](./uitimingcurveprovider/springtimingparameters.md) property.
### Initializers
- [init?(rawValue: Int)](./uitimingcurvetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitimingcurvetype)*