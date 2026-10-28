# simd_normalize

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector pointing in the same direction of the supplied vector, with a length of 1.

## Declaration

```c
static simd_float3 simd_normalize(simd_float3 __x);
```

## Return Value

The normalized vector.

## Discussion

This function returns an undefined value if the supplied vector has zero length or is poorly scaled such that an intermediate computation overflows or underflows.

## Parameters

- `__x`: The vector to normalize.

## See Also

### Geometry Functions
- [simd_cross](./simd_cross-4jxj0.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-3ndxt.md)
  Returns the dot product of two vectors.
- [simd_insphere](./simd_insphere-5jw77.md)
  Tests if a single-precision point lies inside, on, or outside a sphere.
- [simd_fast_normalize](./simd_fast_normalize-dj6.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-4z9ah.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-6ae1u.md)
  Tests the orientation of the three supplied vectors.
- [simd_orient](./simd_orient-kj8u.md)
  Tests the orientation of the four supplied vectors.
- [simd_project](./simd_project-6qmce.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-7du9p.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-3sxbh.md)
  Returns the precise projected vector.
- [simd_reflect](./simd_reflect-4bvhy.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-2fvfh.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_normalize-9c3mv)*