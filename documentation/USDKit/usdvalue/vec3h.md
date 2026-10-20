# USDValue.Vec3h

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 3-component half-precision vector.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@frozen
struct Vec3h
```

## Topics

### Initializers
- [init()](./vec3h/init%28%29.md)
  Creates a zero vector.
- [init(Float16, Float16, Float16)](./vec3h/init%28_,_,_%29.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD3<Float16>](./vec3h/simd.md)
  The vector as a `SIMD3<Float16>`.
- [var x: Float16](./vec3h/x.md)
- [var y: Float16](./vec3h/y.md)
- [var z: Float16](./vec3h/z.md)
### Subscripts
- [subscript(Int) -> Float16](./vec3h/subscript%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec3h)*