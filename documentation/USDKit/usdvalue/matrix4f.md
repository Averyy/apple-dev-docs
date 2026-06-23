# USDValue.Matrix4f

**Framework**: USDKit  
**Kind**: struct

A 4x4 matrix of single-precision floating-point values.

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
struct Matrix4f
```

## Topics

### Initializers
- [init(ProjectiveTransform3DFloat)](usdvalue/matrix4f/init(_:).md)
  Creates a matrix from a Spatial projective transform (single-precision).
- [init(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float)](usdvalue/matrix4f/init(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a matrix from individual element values in row-major order.
- [init(diagonal: Float)](usdvalue/matrix4f/init(diagonal:).md)
  Creates a diagonal matrix with `s` on the diagonal and zeros elsewhere.
### Instance Properties
- [var projectiveTransform: ProjectiveTransform3DFloat](usdvalue/matrix4f/projectivetransform.md)
  The matrix as a Spatial projective transform.
### Subscripts
- [subscript(Int) -> USDValue.Matrix4f.VectorType](usdvalue/matrix4f/subscript(_:).md)
  Accesses the row at the specified index.
- [subscript(column _: Int) -> USDValue.Matrix4f.VectorType](usdvalue/matrix4f/subscript(column:).md)
  Accesses the column at the specified index.
### Type Aliases
- [USDValue.Matrix4f.VectorType](usdvalue/matrix4f/vectortype.md)

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
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix4f)*