# USDValue.Matrix3d

**Framework**: USDKit  
**Kind**: struct

A 3x3 matrix of double-precision floating-point values.

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
struct Matrix3d
```

## Topics

### Initializers
- [init(double3x3)](usdvalue/matrix3d/init(_:).md)
  Creates a matrix from a SIMD `double3x3` matrix.
- [init(Double, Double, Double, Double, Double, Double, Double, Double, Double)](usdvalue/matrix3d/init(_:_:_:_:_:_:_:_:_:).md)
  Creates a matrix from individual element values in row-major order.
- [init(diagonal: Double)](usdvalue/matrix3d/init(diagonal:).md)
  Creates a diagonal matrix with `s` on the diagonal and zeros elsewhere.
### Instance Properties
- [var matrix: double3x3](usdvalue/matrix3d/matrix.md)
  The matrix as a SIMD `double3x3`.
### Subscripts
- [subscript(Int) -> USDValue.Matrix3d.VectorType](usdvalue/matrix3d/subscript(_:).md)
  Accesses the row at the specified index.
- [subscript(column _: Int) -> USDValue.Matrix3d.VectorType](usdvalue/matrix3d/subscript(column:).md)
  Accesses the column at the specified index.
### Type Aliases
- [USDValue.Matrix3d.VectorType](usdvalue/matrix3d/vectortype.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [USDPrim.Attribute.MetadataValue](usdprim/attribute/metadatavalue.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix3d)*