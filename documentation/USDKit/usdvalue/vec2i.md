# USDValue.Vec2i

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 2-component 32-bit integer vector.

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
struct Vec2i
```

## Topics

### Initializers
- [init()](./vec2i/init%28%29.md)
  Creates a zero vector.
- [init(SIMD2<Int32>)](./vec2i/init%28_%29.md)
  Creates a vector from a `SIMD2<Int32>`.
- [init(Int32, Int32)](./vec2i/init%28_,_%29-7uw95.md)
- [init(Int, Int)](./vec2i/init%28_,_%29-8faxo.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD2<Int32>](./vec2i/simd.md)
  The vector as a `SIMD2<Int32>`.
- [var x: Int32](./vec2i/x.md)
- [var y: Int32](./vec2i/y.md)
### Subscripts
- [subscript(Int) -> Int32](./vec2i/subscript%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec2i)*