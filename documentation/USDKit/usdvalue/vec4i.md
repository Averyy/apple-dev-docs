# USDValue.Vec4i

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 4-component 32-bit integer vector.

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
struct Vec4i
```

## Topics

### Initializers
- [init()](./vec4i/init%28%29.md)
  Creates a zero vector.
- [init(SIMD4<Int32>)](./vec4i/init%28_%29.md)
  Creates a vector from a `SIMD4<Int32>`.
- [init(Int, Int, Int, Int)](./vec4i/init%28_,_,_,_%29-5ou3l.md)
  Creates a vector with the given components.
- [init(Int32, Int32, Int32, Int32)](./vec4i/init%28_,_,_,_%29-80hw8.md)
### Instance Properties
- [var simd: SIMD4<Int32>](./vec4i/simd.md)
  The vector as a `SIMD4<Int32>`.
- [var w: Int32](./vec4i/w.md)
- [var x: Int32](./vec4i/x.md)
- [var y: Int32](./vec4i/y.md)
- [var z: Int32](./vec4i/z.md)
### Subscripts
- [subscript(Int) -> Int32](./vec4i/subscript%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec4i)*