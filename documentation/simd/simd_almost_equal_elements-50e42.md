# simd_almost_equal_elements

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.

## Declaration

```c
static simd_bool simd_almost_equal_elements(simd_float2x2 __x, simd_float2x2 __y, float __tol);
```

## See Also

### Equality Functions
- [simd_equal](./simd_equal-9hy16.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements_relative](./simd_almost_equal_elements_relative-6ia0i.md)
  Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_almost_equal_elements-50e42)*