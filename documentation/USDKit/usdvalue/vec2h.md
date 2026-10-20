# USDValue.Vec2h

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 2-component half-precision vector.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@frozen
struct Vec2h
```

## Topics

### Initializers
- [init()](./vec2h/init%28%29.md)
  Creates a zero vector.
- [init(Float16, Float16)](./vec2h/init%28_,_%29.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD2<Float16>](./vec2h/simd.md)
  The vector as a `SIMD2<Float16>`.
- [var x: Float16](./vec2h/x.md)
- [var y: Float16](./vec2h/y.md)
### Subscripts
- [subscript(Int) -> Float16](./vec2h/subscript%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec2h)*