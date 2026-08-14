# USDValue.Vec2h

**Framework**: USDKit  
**Kind**: struct

A 2-component half-precision vector.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct Vec2h
```

## Topics

### Initializers
- [init()](usdvalue/vec2h/init.md)
  Creates a zero vector.
- [init(Float16, Float16)](usdvalue/vec2h/init(_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD2<Float16>](usdvalue/vec2h/simd.md)
  The vector as a `SIMD2<Float16>`.
- [var x: Float16](usdvalue/vec2h/x.md)
- [var y: Float16](usdvalue/vec2h/y.md)
### Subscripts
- [subscript(Int) -> Float16](usdvalue/vec2h/subscript(_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec2h)*