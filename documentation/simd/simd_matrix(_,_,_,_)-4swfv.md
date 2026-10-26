# simd_matrix(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new matrix with the specified columns.

## Declaration

```swift
func simd_matrix(_ col0: simd_double3, _ col1: simd_double3, _ col2: simd_double3, _ col3: simd_double3) -> simd_double4x3
```

```c
static simd_double4x3 simd_matrix(simd_double3 col0, simd_double3 col1, simd_double3 col2, simd_double3 col3);
```

## See Also

### Matrix Creation Functions
- [func simd_matrix_from_rows(simd_double4, simd_double4, simd_double4) -> simd_double4x3](./simd_matrix_from_rows%28_,_,_%29-6525o.md)
  Returns a new matrix with the specified rows.
- [func matrix_from_rows(SIMD4<Double>, SIMD4<Double>, SIMD4<Double>) -> simd_double4x3](./matrix_from_rows%28_,_,_%29-19j6n.md)
  Returns a new matrix with the specified rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_matrix(_:_:_:_:)-4swfv)*