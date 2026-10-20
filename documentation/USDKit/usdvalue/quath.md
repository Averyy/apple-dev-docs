# USDValue.Quath

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A half-precision quaternion.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@frozen
struct Quath
```

## Topics

### Initializers
- [init()](./quath/init%28%29.md)
  Creates a zero quaternion.
- [init(real: Float16, imaginary: USDValue.Vec3h)](./quath/init%28real,imaginary%29.md)
  Creates a quaternion from real and imaginary components.
### Instance Properties
- [var imaginary: USDValue.Vec3h](./quath/imaginary.md)
  The imaginary (vector) component.
- [var real: Float16](./quath/real.md)
  The real (scalar) component.
### Type Properties
- [static var identity: USDValue.Quath](./quath/identity.md)
  The identity quaternion `(real: 1, imaginary: (0, 0, 0))`.
- [static var zero: USDValue.Quath](./quath/zero.md)
  The zero quaternion `(0, 0, 0, 0)`.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](../usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](../usdstage/object/metadatavalue.md)
- [USDValueProtocol](../usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/quath)*