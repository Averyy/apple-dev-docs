# USDValue.Quatf

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
struct Quatf
```

## Topics

### Initializers
- [init()](usdvalue/quatf/init.md)
  Creates a zero quaternion.
- [init(real: Float, imaginary: USDValue.Vec3f)](usdvalue/quatf/init(real:imaginary:).md)
  Creates a quaternion from real and imaginary components.
### Instance Properties
- [var imaginary: USDValue.Vec3f](usdvalue/quatf/imaginary.md)
  The imaginary (vector) component.
- [var real: Float](usdvalue/quatf/real.md)
  The real (scalar) component.
### Type Properties
- [static var identity: USDValue.Quatf](usdvalue/quatf/identity.md)
  The identity quaternion `(real: 1, imaginary: (0, 0, 0))`.
- [static var zero: USDValue.Quatf](usdvalue/quatf/zero.md)
  The zero quaternion `(0, 0, 0, 0)`.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/quatf)*