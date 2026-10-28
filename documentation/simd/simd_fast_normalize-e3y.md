# simd_fast_normalize

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the fast normalized vector.

## Declaration

```c
static simd_half3 simd_fast_normalize(simd_half3 __x);
```

## Return Value

The normalized vector.

## Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `__x`: The vector to normalize.

## See Also

### Geometry functions
- [simd_cross](./simd_cross-828tl.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-p9ir.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9c7zv.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_precise_normalize](./simd_precise_normalize-4z7hd.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-5jxfm.md)
  Tests the orientation of the two supplied vectors.
- [simd_project](./simd_project-3e81w.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-9ry7l.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-99ic5.md)
  Returns the fast projected vector.
- [simd_reflect](./simd_reflect-79zx0.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-5dshi.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_fast_normalize-e3y)*