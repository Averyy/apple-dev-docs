# USDPrim.Property.Variability

**Framework**: USDKit  
**Kind**: enum

Whether a property’s value can change over time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Variability
```

## Topics

### Enumeration Cases
- [USDPrim.Property.Variability.uniform](usdprim/property/variability/uniform.md)
  Value must remain constant across all time samples.
- [USDPrim.Property.Variability.varying](usdprim/property/variability/varying.md)
  Property can have different values at different times (animatable).

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/variability)*