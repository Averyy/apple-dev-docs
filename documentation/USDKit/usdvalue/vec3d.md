# USDValue.Vec3d

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 3-component double-precision vector.

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
struct Vec3d
```

## Topics

### Initializers
- [init()](./vec3d/init%28%29.md)
  Creates a zero vector.
- [init(SIMD3<Double>)](./vec3d/init%28_%29.md)
  Creates a vector from a `SIMD3<Double>`.
- [init(Double, Double, Double)](./vec3d/init%28_,_,_%29.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD3<Double>](./vec3d/simd.md)
  The vector as a `SIMD3<Double>`.
- [var x: Double](./vec3d/x.md)
- [var y: Double](./vec3d/y.md)
- [var z: Double](./vec3d/z.md)
### Subscripts
- [subscript(Int) -> Double](./vec3d/subscript%28_%29.md)
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

## See Also

### Inspecting the value
- [var typeName: String](./typename.md)
  The name of the wrapped type.
- [var isEmpty: Bool](./isempty.md)
  Whether this value is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec3d)*