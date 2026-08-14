# USDValue.Vec4d

**Framework**: USDKit  
**Kind**: struct

A 4-component double-precision vector.

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
struct Vec4d
```

## Topics

### Initializers
- [init()](usdvalue/vec4d/init.md)
  Creates a zero vector.
- [init(SIMD4<Double>)](usdvalue/vec4d/init(_:).md)
  Creates a vector from a `SIMD4<Double>`.
- [init(Double, Double, Double, Double)](usdvalue/vec4d/init(_:_:_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD4<Double>](usdvalue/vec4d/simd.md)
  The vector as a `SIMD4<Double>`.
- [var w: Double](usdvalue/vec4d/w.md)
- [var x: Double](usdvalue/vec4d/x.md)
- [var y: Double](usdvalue/vec4d/y.md)
- [var z: Double](usdvalue/vec4d/z.md)
### Subscripts
- [subscript(Int) -> Double](usdvalue/vec4d/subscript(_:).md)
  Accesses the component at the specified index.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](usdstage/object/metadatavalue.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec4d)*