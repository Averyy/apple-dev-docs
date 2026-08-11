# USDValue.Vec4f

**Framework**: USDKit  
**Kind**: struct

A 4-component single-precision vector.

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
struct Vec4f
```

## Topics

### Initializers
- [init()](usdvalue/vec4f/init.md)
  Creates a zero vector.
- [init(SIMD4<Float>)](usdvalue/vec4f/init(_:).md)
  Creates a vector from a `SIMD4<Float>`.
- [init(Float, Float, Float, Float)](usdvalue/vec4f/init(_:_:_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD4<Float>](usdvalue/vec4f/simd.md)
  The vector as a `SIMD4<Float>`.
- [var w: Float](usdvalue/vec4f/w.md)
- [var x: Float](usdvalue/vec4f/x.md)
- [var y: Float](usdvalue/vec4f/y.md)
- [var z: Float](usdvalue/vec4f/z.md)
### Subscripts
- [subscript(Int) -> Float](usdvalue/vec4f/subscript(_:).md)
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
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec4f)*