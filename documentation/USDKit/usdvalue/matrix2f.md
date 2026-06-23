# USDValue.Matrix2f

**Framework**: USDKit  
**Kind**: struct

A 2x2 matrix of single-precision floating-point values.

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
struct Matrix2f
```

## Topics

### Initializers
- [init(Float, Float, Float, Float)](usdvalue/matrix2f/init(_:_:_:_:).md)
  Creates a matrix from individual element values in row-major order.
- [init(diagonal: Float)](usdvalue/matrix2f/init(diagonal:).md)
  Creates a diagonal matrix with `s` on the diagonal and zeros elsewhere.
### Subscripts
- [subscript(Int) -> USDValue.Matrix2f.VectorType](usdvalue/matrix2f/subscript(_:).md)
  Accesses the row at the specified index.
- [subscript(column _: Int) -> USDValue.Matrix2f.VectorType](usdvalue/matrix2f/subscript(column:).md)
  Accesses the column at the specified index.
### Type Aliases
- [USDValue.Matrix2f.VectorType](usdvalue/matrix2f/vectortype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/matrix2f)*