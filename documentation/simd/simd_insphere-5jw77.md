# simd_insphere

**Framework**: simd  
**Kind**: func  
**Role**: Function

Tests if a single-precision point lies inside, on, or outside a sphere.

## Declaration

```c
static float simd_insphere(simd_float3 __x, simd_float3 __a, simd_float3 __b, simd_float3 __c, simd_float3 __d);
```

## Return Value

A value that indicates whether the point lies inside, on, or outside the specified sphere.

## Discussion

If the points `a`, `b`, `c`, and `d` describe a positively-oriented sphere (that is, the sphere’s normals point away from its center), the function returns:

- A positive value if `x` is inside the sphere
- Zero if `x` is on the sphere
- A negative value if `x` is outside the sphere

The function flips sign of the return value if the sphere is negatively-oriented (that is, the sphere’s normals point towards its center).

## Parameters

- `__x`: The point that the function tests.
- `__a`: The first point that determines the sphere.
- `__b`: The second point that determines the sphere.
- `__c`: The third point that determines the sphere.
- `__d`: The fourth point that determines the sphere.

## See Also

### Geometry Functions
- [simd_cross](./simd_cross-4jxj0.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-3ndxt.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9c3mv.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
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

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_insphere-5jw77)*