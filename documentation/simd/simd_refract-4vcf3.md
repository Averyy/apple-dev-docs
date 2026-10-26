# simd_refract

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.

## Declaration

```c
static simd_float2 simd_refract(simd_float2 __x, simd_float2 __n, float __eta);
```

## See Also

### Geometry Functions
- [simd_cross](./simd_cross-3ukic.md)
  Returns the cross product of two vectors.
- [simd_dot](./simd_dot-3pmfs.md)
  Returns the dot product of two vectors.
- [simd_incircle](./simd_incircle-1bi0y.md)
  Tests if a single-precision point lies inside, on, or outside a circle.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_refract-4vcf3)*