# simd_incircle

**Framework**: simd  
**Kind**: func  
**Role**: Function

Tests if a double-precision point lies inside, on, or outside a circle.

## Declaration

```c
static double simd_incircle(simd_double2 __x, simd_double2 __a, simd_double2 __b, simd_double2 __c);
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
- [simd_cross](./simd_cross-1dixl.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-3r1vl.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9fo1c.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-9wy6m.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-54dru.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-9fgki.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-9b2wf.md)
  Tests the orientation of the three supplied vectors.
- [simd_project](./simd_project-1mg5p.md)
  Returns the first vector projected onto the second vector.
- [simd_fast_project](./simd_fast_project-6c68k.md)
  Returns the fast projected vector.
- [simd_precise_project](./simd_precise_project-7t3qn.md)
  Returns the precise projected vector.
- [simd_reflect](./simd_reflect-7c8f9.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-4ani9.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_incircle-8iogb)*