# simd_matrix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_double3, _ col1: simd_double3, _ col2: simd_double3) -> simd_double3x3
```

```c
static simd_double3x3 simd_matrix(simd_double3 col0, simd_double3 col1, simd_double3 col2);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_double3, simd_double3, simd_double3) -> simd_double3x3](./simd_matrix_from_rows%28_,_,_%29-48v9h.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD3<Double>, SIMD3<Double>, SIMD3<Double>) -> simd_double3x3](./matrix_from_rows%28_,_,_%29-7a60t.md)
  Returns a new matrix with the specified rows.
- [func simd_matrix3x3(simd_quatd) -> simd_double3x3](./simd_matrix3x3%28_%29-60dhx.md)
  Returns a new matrix with the specified quarternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:)-5h0nl)*