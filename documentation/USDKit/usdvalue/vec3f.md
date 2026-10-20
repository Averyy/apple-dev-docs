# USDValue.Vec3f

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 3-component single-precision vector.

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
struct Vec3f
```

## Topics

### Initializers
- [init()](./vec3f/init%28%29.md)
  Creates a zero vector.
- [init(SIMD3<Float>)](./vec3f/init%28_%29.md)
  Creates a vector from a `SIMD3<Float>`.
- [init(Float, Float, Float)](./vec3f/init%28_,_,_%29.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD3<Float>](./vec3f/simd.md)
  The vector as a `SIMD3<Float>`.
- [var x: Float](./vec3f/x.md)
- [var y: Float](./vec3f/y.md)
- [var z: Float](./vec3f/z.md)
### Subscripts
- [subscript(Int) -> Float](./vec3f/subscript%28_%29.md)
  Accesses the component at the specified index.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](../usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](../usdstage/object/metadatavalue.md)
- [USDValueProtocol](../usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec3f)*