# USDValue.Vec3i

**Framework**: USDKit  
**Kind**: struct

A 3-component 32-bit integer vector.

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
struct Vec3i
```

## Topics

### Initializers
- [init()](usdvalue/vec3i/init.md)
  Creates a zero vector.
- [init(SIMD3<Int32>)](usdvalue/vec3i/init(_:).md)
  Creates a vector from a `SIMD3<Int32>`.
- [init(Int, Int, Int)](usdvalue/vec3i/init(_:_:_:)-1jo3u.md)
  Creates a vector with the given components.
- [init(Int32, Int32, Int32)](usdvalue/vec3i/init(_:_:_:)-25s85.md)
### Instance Properties
- [var simd: SIMD3<Int32>](usdvalue/vec3i/simd.md)
  The vector as a `SIMD3<Int32>`.
- [var x: Int32](usdvalue/vec3i/x.md)
- [var y: Int32](usdvalue/vec3i/y.md)
- [var z: Int32](usdvalue/vec3i/z.md)
### Subscripts
- [subscript(Int) -> Int32](usdvalue/vec3i/subscript(_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec3i)*