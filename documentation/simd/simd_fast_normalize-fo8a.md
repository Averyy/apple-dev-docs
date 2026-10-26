# simd_fast_normalize

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the fast normalized vector.

## Declaration

```c
static simd_half16 simd_fast_normalize(simd_half16 __x);
```

#### Return Value

The normalized vector.

#### Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `__x`: The vector to normalize.

## See Also

### Geometry functions
- [simd_dot](./simd_dot-8gymo.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-3r6p1.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_precise_normalize](./simd_precise_normalize-53d5a.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-4n2u6.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-7slej.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-95iib.md)
  Returns the fast projected vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_fast_normalize-fo8a)*