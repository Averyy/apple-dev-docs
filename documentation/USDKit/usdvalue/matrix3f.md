# USDValue.Matrix3f

**Framework**: USDKit  
**Kind**: struct

A 3x3 matrix of single-precision floating-point values.

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
struct Matrix3f
```

## Topics

### Initializers
- [init(float3x3)](usdvalue/matrix3f/init(_:).md)
  Creates a matrix from a SIMD `float3x3` matrix.
- [init(Float, Float, Float, Float, Float, Float, Float, Float, Float)](usdvalue/matrix3f/init(_:_:_:_:_:_:_:_:_:).md)
  Creates a matrix from individual element values in row-major order.
- [init(diagonal: Float)](usdvalue/matrix3f/init(diagonal:).md)
  Creates a diagonal matrix with `s` on the diagonal and zeros elsewhere.
### Instance Properties
- [var matrix: float3x3](usdvalue/matrix3f/matrix.md)
  The matrix as a SIMD `float3x3`.
### Subscripts
- [subscript(Int) -> USDValue.Matrix3f.VectorType](usdvalue/matrix3f/subscript(_:).md)
  Accesses the row at the specified index.
- [subscript(column _: Int) -> USDValue.Matrix3f.VectorType](usdvalue/matrix3f/subscript(column:).md)
  Accesses the column at the specified index.
### Type Aliases
- [USDValue.Matrix3f.VectorType](usdvalue/matrix3f/vectortype.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDValueProtocol](usdvalueprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix3f)*