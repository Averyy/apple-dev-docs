# USDPrim.Property.Variability

**Framework**: USDKit  
**Kind**: enum  
**Role**: Enumeration

Whether a property’s value can change over time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Variability
```

## Topics

### Enumeration Cases
- [USDPrim.Property.Variability.uniform](./variability/uniform.md)
  Value must remain constant across all time samples.
- [USDPrim.Property.Variability.varying](./variability/varying.md)
  Property can have different values at different times (animatable).

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [USDValueProtocol](../../usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/variability)*