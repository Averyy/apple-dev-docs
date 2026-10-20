# USDValue.Vec4d

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 4-component double-precision vector.

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
struct Vec4d
```

## Topics

### Initializers
- [init()](./vec4d/init%28%29.md)
  Creates a zero vector.
- [init(SIMD4<Double>)](./vec4d/init%28_%29.md)
  Creates a vector from a `SIMD4<Double>`.
- [init(Double, Double, Double, Double)](./vec4d/init%28_,_,_,_%29.md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD4<Double>](./vec4d/simd.md)
  The vector as a `SIMD4<Double>`.
- [var w: Double](./vec4d/w.md)
- [var x: Double](./vec4d/x.md)
- [var y: Double](./vec4d/y.md)
- [var z: Double](./vec4d/z.md)
### Subscripts
- [subscript(Int) -> Double](./vec4d/subscript%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec4d)*