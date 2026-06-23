# USDValue.Vec3d

**Framework**: USDKit  
**Kind**: struct

A 3-component double-precision vector.

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
struct Vec3d
```

## Topics

### Initializers
- [init()](usdvalue/vec3d/init.md)
  Creates a zero vector.
- [init(SIMD3<Double>)](usdvalue/vec3d/init(_:).md)
  Creates a vector from a `SIMD3<Double>`.
- [init(Double, Double, Double)](usdvalue/vec3d/init(_:_:_:).md)
  Creates a vector with the given components.
### Instance Properties
- [var simd: SIMD3<Double>](usdvalue/vec3d/simd.md)
  The vector as a `SIMD3<Double>`.
- [var x: Double](usdvalue/vec3d/x.md)
- [var y: Double](usdvalue/vec3d/y.md)
- [var z: Double](usdvalue/vec3d/z.md)
### Subscripts
- [subscript(Int) -> Double](usdvalue/vec3d/subscript(_:).md)
  Accesses the component at the specified index.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [USDPrim.Attribute.MetadataValue](usdprim/attribute/metadatavalue.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [var typeName: String](usdvalue/typename.md)
  The name of the wrapped type.
- [var isEmpty: Bool](usdvalue/isempty.md)
  Whether this value is empty.
- [var isArrayValued: Bool](usdvalue/isarrayvalued.md)
  Whether the wrapped value is an array.
- [var arraySize: Int](usdvalue/arraysize.md)
  The number of elements in the wrapped array, or `0` for scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/vec3d)*