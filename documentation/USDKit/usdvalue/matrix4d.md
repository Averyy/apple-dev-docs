# USDValue.Matrix4d

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A 4x4 matrix of double-precision floating-point values.

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
struct Matrix4d
```

## Topics

### Initializers
- [init(ProjectiveTransform3D)](./matrix4d/init%28_%29-6b27q.md)
  Creates a matrix from a Spatial projective transform (double-precision).
- [init(ProjectiveTransform3DFloat)](./matrix4d/init%28_%29-9y0w7.md)
  Creates a matrix from a Spatial projective transform (single-precision).
- [init(Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double)](./matrix4d/init%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a matrix from individual element values in row-major order.
- [init(diagonal: Double)](./matrix4d/init%28diagonal%29.md)
  Creates a diagonal matrix with `s` on the diagonal and zeros elsewhere.
### Instance Properties
- [var projectiveTransform: ProjectiveTransform3D](./matrix4d/projectivetransform.md)
  The matrix as a Spatial projective transform.
### Subscripts
- [subscript(Int) -> USDValue.Matrix4d.VectorType](./matrix4d/subscript%28_%29.md)
  Accesses the row at the specified index.
- [subscript(column _: Int) -> USDValue.Matrix4d.VectorType](./matrix4d/subscript%28column%29.md)
  Accesses the column at the specified index.
### Type Aliases
- [USDValue.Matrix4d.VectorType](./matrix4d/vectortype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix4d)*