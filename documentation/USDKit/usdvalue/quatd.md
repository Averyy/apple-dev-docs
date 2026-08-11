# USDValue.Quatd

**Framework**: USDKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct Quatd
```

## Topics

### Initializers
- [init()](usdvalue/quatd/init.md)
  Creates a zero quaternion.
- [init(real: Double, imaginary: USDValue.Vec3d)](usdvalue/quatd/init(real:imaginary:).md)
  Creates a quaternion from real and imaginary components.
### Instance Properties
- [var imaginary: USDValue.Vec3d](usdvalue/quatd/imaginary.md)
  The imaginary (vector) component.
- [var real: Double](usdvalue/quatd/real.md)
  The real (scalar) component.
### Type Properties
- [static var identity: USDValue.Quatd](usdvalue/quatd/identity.md)
  The identity quaternion `(real: 1, imaginary: (0, 0, 0))`.
- [static var zero: USDValue.Quatd](usdvalue/quatd/zero.md)
  The zero quaternion `(0, 0, 0, 0)`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/quatd)*