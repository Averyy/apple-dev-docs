# simd_matrix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_double2, _ col1: simd_double2, _ col2: simd_double2) -> simd_double3x2
```

```c
static simd_double3x2 simd_matrix(simd_double2 col0, simd_double2 col1, simd_double2 col2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_double3, simd_double3) -> simd_double3x2](./simd_matrix_from_rows%28_,_%29-7mxf9.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Double>, SIMD3<Double>) -> simd_double3x2](./matrix_from_rows%28_,_%29-630eh.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:)-59y1c)*