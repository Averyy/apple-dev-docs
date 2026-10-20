# USDValue.Matrix4f

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 4x4 matrix of single-precision floating-point values.

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
struct Matrix4f
```

## Topics

### Initializers
- [init(ProjectiveTransform3DFloat)](./matrix4f/init%28_%29.md)
  Creates a matrix from a Spatial projective transform (single-precision).
- [init(Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float, Float)](./matrix4f/init%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a matrix from individual element values in row-major order.
- [init(diagonal: Float)](./matrix4f/init%28diagonal%29.md)
  Creates a diagonal matrix with `s` on the diagonal and zeros elsewhere.
### Instance Properties
- [var projectiveTransform: ProjectiveTransform3DFloat](./matrix4f/projectivetransform.md)
  The matrix as a Spatial projective transform.
### Subscripts
- [subscript(Int) -> USDValue.Matrix4f.VectorType](./matrix4f/subscript%28_%29.md)
  Accesses the row at the specified index.
- [subscript(column _: Int) -> USDValue.Matrix4f.VectorType](./matrix4f/subscript%28column%29.md)
  Accesses the column at the specified index.
### Type Aliases
- [USDValue.Matrix4f.VectorType](./matrix4f/vectortype.md)

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
- [USDValueProtocol](../usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix4f)*