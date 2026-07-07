# USDValue.Vec3h

**Framework**: USDKit  
**Kind**: struct

A 3-component half-precision vector.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct Vec3h
```

## Topics

### Initializers
- [init()](usdvalue/vec3h/init.md)
  Creates a zero vector.
- [init(Float16, Float16, Float16)](usdvalue/vec3h/init(_:_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD3<Float16>](usdvalue/vec3h/simd.md)
  The vector as a `SIMD3<Float16>`.
- [var x: Float16](usdvalue/vec3h/x.md)
- [var y: Float16](usdvalue/vec3h/y.md)
- [var z: Float16](usdvalue/vec3h/z.md)
### Subscripts
- [subscript(Int) -> Float16](usdvalue/vec3h/subscript(_:).md)
  Accesses the component at the specified index.

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
- [USDPrim.Attribute.MetadataValue](usdprim/attribute/metadatavalue.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec3h)*