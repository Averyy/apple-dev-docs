# simd_almost_equal_elements_relative

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a matrix is within a specified single-precision relative tolerance to the corresponding element in a second matrix.

## Declaration

```c
static simd_bool simd_almost_equal_elements_relative(simd_half3x3 __x, simd_half3x3 __y, _Float16 __tol);
```

## See Also

### Equality functions
- [simd_equal](./simd_equal-75e79.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix.
- [simd_almost_equal_elements](./simd_almost_equal_elements-9mm59.md)
  Returns true if every element in a matrix is within a specified tolerance to the corresponding element in a second matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_almost_equal_elements_relative-2mbzd)*