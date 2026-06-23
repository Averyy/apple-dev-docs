# USDValue.Matrix4d

**Framework**: USDKit  
**Kind**: struct

A 4x4 matrix of double-precision floating-point values.

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
struct Matrix4d
```

## Topics

### Initializers
- [init(ProjectiveTransform3D)](usdvalue/matrix4d/init(_:)-6b27q.md)
  Creates a matrix from a Spatial projective transform (double-precision).
- [init(ProjectiveTransform3DFloat)](usdvalue/matrix4d/init(_:)-9y0w7.md)
  Creates a matrix from a Spatial projective transform (single-precision).
- [init(Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double)](usdvalue/matrix4d/init(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a matrix from individual element values in row-major order.
- [init(diagonal: Double)](usdvalue/matrix4d/init(diagonal:).md)
  Creates a diagonal matrix with `s` on the diagonal and zeros elsewhere.
### Instance Properties
- [var projectiveTransform: ProjectiveTransform3D](usdvalue/matrix4d/projectivetransform.md)
  The matrix as a Spatial projective transform.
### Subscripts
- [subscript(Int) -> USDValue.Matrix4d.VectorType](usdvalue/matrix4d/subscript(_:).md)
  Accesses the row at the specified index.
- [subscript(column _: Int) -> USDValue.Matrix4d.VectorType](usdvalue/matrix4d/subscript(column:).md)
  Accesses the column at the specified index.
### Type Aliases
- [USDValue.Matrix4d.VectorType](usdvalue/matrix4d/vectortype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix4d)*