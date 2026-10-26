# simd_matrix(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_double2, _ col1: simd_double2, _ col2: simd_double2, _ col3: simd_double2) -> simd_double4x2
```

```c
static simd_double4x2 simd_matrix(simd_double2 col0, simd_double2 col1, simd_double2 col2, simd_double2 col3);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_double4, simd_double4) -> simd_double4x2](./simd_matrix_from_rows%28_,_%29-5xq2d.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Double>, SIMD4<Double>) -> simd_double4x2](./matrix_from_rows%28_,_%29-2rxkt.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:_:)-6cze4)*