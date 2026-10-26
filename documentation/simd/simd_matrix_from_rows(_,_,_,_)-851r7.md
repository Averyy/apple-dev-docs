# simd_matrix_from_rows(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified rows.

## Declaration

```swift
func simd_matrix_from_rows(_ row0: simd_double2, _ row1: simd_double2, _ row2: simd_double2, _ row3: simd_double2) -> simd_double2x4
```

```c
static simd_double2x4 simd_matrix_from_rows(simd_double2 row0, simd_double2 row1, simd_double2 row2, simd_double2 row3);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_double4, simd_double4) -> simd_double2x4](./simd_matrix%28_,_%29-7hafe.md)
  Returns a new matrix with the specified columns.
- [func matrix_from_rows(SIMD2<Double>, SIMD2<Double>, SIMD2<Double>, SIMD2<Double>) -> simd_double2x4](./matrix_from_rows%28_,_,_,_%29-897qw.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix_from_rows(_:_:_:_:)-851r7)*