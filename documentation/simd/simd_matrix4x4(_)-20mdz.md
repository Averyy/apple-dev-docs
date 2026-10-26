# simd_matrix4x4(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified quarternion.

## Declaration

```swift
func simd_matrix4x4(_ q: simd_quatd) -> simd_double4x4
```

```c
static simd_double4x4 simd_matrix4x4(simd_quatd q);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix(simd_double4, simd_double4, simd_double4, simd_double4) -> simd_double4x4](./simd_matrix%28_,_,_,_%29-28at0.md)
  Returns a new matrix with the specified columns.
- [func simd_matrix_from_rows(simd_double4, simd_double4, simd_double4, simd_double4) -> simd_double4x4](./simd_matrix_from_rows%28_,_,_,_%29-898tw.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double4x4](./matrix_from_rows%28_,_,_,_%29-37t0w.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix4x4(_:)-20mdz)*