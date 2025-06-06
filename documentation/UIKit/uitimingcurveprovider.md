# UITimingCurveProvider

**Framework**: UIKit  
**Kind**: protocol

An interface for providing the timing information needed to perform animations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITimingCurveProvider : NSCoding, NSCopying
```

#### Overview

An object that adopts the [`UITimingCurveProvider`](uitimingcurveprovider.md) protocol provides the timing information needed to perform animations with a [`UIViewPropertyAnimator`](uiviewpropertyanimator.md) object. A timing curve defines the velocity at which animated properties change to their new values over the duration of the animation. A custom timing curve provider can specify timing using the built-in UIKit curves, a cubic Bézier curve, a spring-based timing function, or a combination of timing information.

When implementing this protocol in a custom object, you must provide implementations for all of the properties. Use the [`timingCurveType`](uitimingcurveprovider/timingcurvetype.md) property to specify which timing information your object provides. Configure the other properties with the actual timing curve values.

## Topics

### Getting the timing information
- [var timingCurveType: UITimingCurveType](uitimingcurveprovider/timingcurvetype.md)
  The type of timing information to use.
- [var cubicTimingParameters: UICubicTimingParameters?](uitimingcurveprovider/cubictimingparameters.md)
  The cubic timing parameters to use.
- [var springTimingParameters: UISpringTimingParameters?](uitimingcurveprovider/springtimingparameters.md)
  The spring-based timing parameters to use.
### Constants
- [enum UITimingCurveType](uitimingcurvetype.md)
  Constants indicating the type of timing information to use.

## Relationships

### Inherits From
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
### Conforming Types
- [UICubicTimingParameters](uicubictimingparameters.md)
- [UISpringTimingParameters](uispringtimingparameters.md)

## See Also

- [class UISpringTimingParameters](uispringtimingparameters.md)
  The timing information for animations that mimics the behavior of a spring.
- [class UICubicTimingParameters](uicubictimingparameters.md)
  The timing information for animations in the form of a cubic Bézier curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitimingcurveprovider)*