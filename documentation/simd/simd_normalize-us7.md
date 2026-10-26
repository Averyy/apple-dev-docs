# simd_normalize

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector pointing in the same direction of the supplied vector, with a length of 1.

## Declaration

```c
static simd_half8 simd_normalize(simd_half8 __x);
```

#### Return Value

The normalized vector.

#### Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `__x`: The vector to normalize.

## See Also

### Geometry functions
- [simd_dot](./simd_dot-16ezc.md)
  Returns the dot product of two vectors.
- [simd_fast_normalize](./simd_fast_normalize-8x56w.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-621rw.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-472vy.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-8kipf.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-2k6sp.md)
  Returns the fast projected vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_normalize-us7)*