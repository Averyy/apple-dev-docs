# matrix_from_diagonal(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified vector on the main diagonal.

**Availability**:
- Swift - Deprecated in 4.0 (renamed: simd_double2x2(diagonal:))

## Declaration

```swift
func matrix_from_diagonal(_ d: SIMD2<Double>) -> simd_double2x2
```

## See Also

### Deprecated Symbols
- [func matrix_invert(simd_double2x2) -> simd_double2x2](./matrix_invert%28_%29-nkj5.md)
  Returns the inverse of the specified matrix.
- [func matrix_equal(simd_double2x2, simd_double2x2) -> Bool](./matrix_equal%28_,_%29-4claa.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.
- [func matrix_determinant(simd_double2x2) -> Double](./matrix_determinant%28_%29-7kglv.md)
  Returns the determinant of the specified matrix.
- [func matrix_from_columns(SIMD2<Double>, SIMD2<Double>) -> simd_double2x2](./matrix_from_columns%28_,_%29-37jug.md)
  Returns a new matrix with the specified columns.
- [func matrix_transpose(simd_double2x2) -> double2x2](./matrix_transpose%28_%29-6qaez.md)
  Returns the transpose of a matrix.
- [init(simd_double2x2)](./simd_double2x2/init%28_%29-9vxjx.md)
  Creates a new matrix with the specified matrix.
- [var cmatrix: simd_double2x2](./simd_double2x2/cmatrix.md)
  Returns the matrix as the corresponding C matrix type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/matrix_from_diagonal(_:)-7i8pm)*