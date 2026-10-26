# simd_incircle

**Framework**: simd  
**Kind**: func  
**Role**: Function

Tests whether a single-precision point lies inside, on, or outside a circle.

## Declaration

```c
static _Float16 simd_incircle(simd_half2 __x, simd_half2 __a, simd_half2 __b, simd_half2 __c);
```

#### Return Value

A value that indicates whether the point lies inside, on, or outside the specified circle.

#### Discussion

If the points `a`, `b`, and `c` describe a positively oriented (counterclockwise) circle, the function returns:

- A positive value if `x` is inside the circle
- Zero if `x` is on the circle
- A negative value if `x` is outside the circle

The function flips the sign of the return value if the circle is negatively oriented (clockwise).

## Parameters

- `__x`: The point that the function tests.
- `__a`: The first point that determines the circle.
- `__b`: The second point that determines the circle.
- `__c`: The third point that determines the circle.

## See Also

### Geometry functions
- [simd_cross](./simd_cross-9a0v4.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-8841h.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9fk7c.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-9wx26.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-54cma.md)
  Returns the precise normalized vector.
- [simd_orient](./simd_orient-9db7k.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-4pzf2.md)
  Tests the orientation of the two supplied vectors.
- [simd_orient](./simd_orient-hid7.md)
  Tests the orientation of the two supplied vectors.
- [simd_project](./simd_project-6bme3.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-6uimg.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-8f9wk.md)
  Returns the fast projected vector.
- [simd_reflect](./simd_reflect-1ot4h.md)
  Returns the reflection direction of an incident vector and a unit normal vector.
- [simd_refract](./simd_refract-31085.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_incircle-4k0k0)*