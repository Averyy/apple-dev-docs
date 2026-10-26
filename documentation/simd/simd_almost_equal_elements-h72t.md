# simd_almost_equal_elements

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.

## Declaration

```c
static simd_bool simd_almost_equal_elements(simd_double3x4 __x, simd_double3x4 __y, double __tol);
```

## See Also

### Equality Functions
- [simd_equal](./simd_equal-4m10u.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-9q7od.md)
  Returns true if every element in a matrix is within a specified double-precision relative tolerance to the corresponding element in a second matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_almost_equal_elements-h72t)*