# simd_incircle

**Framework**: simd  
**Kind**: func  
**Role**: Function

Tests if a single-precision point lies inside, on, or outside a circle.

## Declaration

```c
static float simd_incircle(simd_float2 __x, simd_float2 __a, simd_float2 __b, simd_float2 __c);
```

## Return Value

A value that indicates whether the point lies inside, on, or outside the specified circle.

## Discussion

If the points `a`, `b`, and `c` describe a positively- or counterclockwise-oriented circle, the function returns:

- A positive value if `x` is inside the circle
- Zero if `x` is on the circle
- A negative value if `x` is outside the circle

The function flips sign of the return value if the circle is negatively- or clockwise-oriented.

## Parameters

- `__x`: The point that the function tests.
- `__a`: The first point that determines the circle.
- `__b`: The second point that determines the circle.
- `__c`: The third point that determines the circle.

## See Also

### Geometry Functions
- [simd_cross](./simd_cross-3ukic.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-3pmfs.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9fok8.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-9wxm2.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-54d5a.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-8wej6.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-6wf24.md)
  Tests the orientation of the three supplied vectors.
- [simd_project](./simd_project-39liq.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-4ei25.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-4chm1.md)
  Returns the fast projected vector.
- [simd_reflect](./simd_reflect-7dnri.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-4vcf3.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_incircle-1bi0y)*