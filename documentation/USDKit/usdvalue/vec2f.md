# USDValue.Vec2f

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 2-component single-precision vector.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@frozen
struct Vec2f
```

## Topics

### Initializers
- [init()](./vec2f/init%28%29.md)
  Creates a zero vector.
- [init(SIMD2<Float>)](./vec2f/init%28_%29.md)
  Creates a vector from a `SIMD2<Float>`.
- [init(Float, Float)](./vec2f/init%28_,_%29.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD2<Float>](./vec2f/simd.md)
  The vector as a `SIMD2<Float>`.
- [var x: Float](./vec2f/x.md)
- [var y: Float](./vec2f/y.md)
### Subscripts
- [subscript(Int) -> Float](./vec2f/subscript%28_%29.md)
  Accesses the component at the specified index.

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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec2f)*