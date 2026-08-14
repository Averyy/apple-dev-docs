# USDValue.Vec2d

**Framework**: USDKit  
**Kind**: struct

A 2-component double-precision vector.

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
struct Vec2d
```

## Topics

### Initializers
- [init()](usdvalue/vec2d/init.md)
  Creates a zero vector.
- [init(SIMD2<Double>)](usdvalue/vec2d/init(_:).md)
  Creates a vector from a `SIMD2<Double>`.
- [init(Double, Double)](usdvalue/vec2d/init(_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD2<Double>](usdvalue/vec2d/simd.md)
  The vector as a `SIMD2<Double>`.
- [var x: Double](usdvalue/vec2d/x.md)
- [var y: Double](usdvalue/vec2d/y.md)
### Subscripts
- [subscript(Int) -> Double](usdvalue/vec2d/subscript(_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec2d)*