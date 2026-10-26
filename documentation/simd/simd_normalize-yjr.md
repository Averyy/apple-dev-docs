# simd_normalize

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector pointing in the same direction of the supplied vector, with a length of 1.

## Declaration

```c
static simd_double8 simd_normalize(simd_double8 __x);
```

#### Return Value

The normalized vector.

#### Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `__x`: The vector to normalize.

## See Also

### Geometry Functions
- [simd_dot](./simd_dot-5vlda.md)
  Returns the dot product of two vectors.
- [simd_fast_normalize](./simd_fast_normalize-8x3pc.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-6237w.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-8o56y.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-61mm1.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-2x3bb.md)
  Returns the precise projected vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_normalize-yjr)*