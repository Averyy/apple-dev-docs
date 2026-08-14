# USDValue.Vec2f

**Framework**: USDKit  
**Kind**: struct

A 2-component single-precision vector.

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
struct Vec2f
```

## Topics

### Initializers
- [init()](usdvalue/vec2f/init.md)
  Creates a zero vector.
- [init(SIMD2<Float>)](usdvalue/vec2f/init(_:).md)
  Creates a vector from a `SIMD2<Float>`.
- [init(Float, Float)](usdvalue/vec2f/init(_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD2<Float>](usdvalue/vec2f/simd.md)
  The vector as a `SIMD2<Float>`.
- [var x: Float](usdvalue/vec2f/x.md)
- [var y: Float](usdvalue/vec2f/y.md)
### Subscripts
- [subscript(Int) -> Float](usdvalue/vec2f/subscript(_:).md)
  Accesses the component at the specified index.

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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec2f)*