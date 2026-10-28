# simd_precise_normalize

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the precise normalized vector.

## Declaration

```c
static simd_double4 simd_precise_normalize(simd_double4 __x);
```

## Return Value

The normalized vector.

## Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `__x`: The vector to normalize.

## See Also

### Geometry Functions
- [simd_dot](./simd_dot-85nay.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9o7wa.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-3rv7.md)
  Returns the fast normalized vector.
- [simd_project](./simd_project-6cfku.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-6urv1.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-1f1gc.md)
  Returns the precise projected vector.
- [simd_reflect](./simd_reflect-91ah5.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-7dskm.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_precise_normalize-4vtps)*