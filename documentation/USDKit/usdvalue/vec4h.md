# USDValue.Vec4h

**Framework**: USDKit  
**Kind**: struct

A 4-component half-precision vector.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct Vec4h
```

## Topics

### Initializers
- [init()](usdvalue/vec4h/init.md)
  Creates a zero vector.
- [init(Float16, Float16, Float16, Float16)](usdvalue/vec4h/init(_:_:_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD4<Float16>](usdvalue/vec4h/simd.md)
  The vector as a `SIMD4<Float16>`.
- [var w: Float16](usdvalue/vec4h/w.md)
- [var x: Float16](usdvalue/vec4h/x.md)
- [var y: Float16](usdvalue/vec4h/y.md)
- [var z: Float16](usdvalue/vec4h/z.md)
### Subscripts
- [subscript(Int) -> Float16](usdvalue/vec4h/subscript(_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec4h)*