# USDValue.Vec3f

**Framework**: USDKit  
**Kind**: struct

A 3-component single-precision vector.

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
struct Vec3f
```

## Topics

### Initializers
- [init()](usdvalue/vec3f/init.md)
  Creates a zero vector.
- [init(SIMD3<Float>)](usdvalue/vec3f/init(_:).md)
  Creates a vector from a `SIMD3<Float>`.
- [init(Float, Float, Float)](usdvalue/vec3f/init(_:_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD3<Float>](usdvalue/vec3f/simd.md)
  The vector as a `SIMD3<Float>`.
- [var x: Float](usdvalue/vec3f/x.md)
- [var y: Float](usdvalue/vec3f/y.md)
- [var z: Float](usdvalue/vec3f/z.md)
### Subscripts
- [subscript(Int) -> Float](usdvalue/vec3f/subscript(_:).md)
  Accesses the component at the specified index.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [USDPrim.Attribute.MetadataValue](usdprim/attribute/metadatavalue.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec3f)*