# simd_matrix_from_rows(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_double4, _ row1: simd_double4, _ row2: simd_double4) -> simd_double4x3
```

```c
static simd_double4x3 simd_matrix_from_rows(simd_double4 row0, simd_double4 row1, simd_double4 row2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_double3, simd_double3, simd_double3, simd_double3) -> simd_double4x3](./simd_matrix%28_,_,_,_%29-4swfv.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double4x3](./matrix_from_rows%28_,_,_%29-19j6n.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:)-6525o)*