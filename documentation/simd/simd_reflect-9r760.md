# simd_reflect

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the reflection direction of an incident vector and a unit normal vector.

## Declaration

```c
static simd_half4 simd_reflect(simd_half4 __x, simd_half4 __n);
```

## See Also

### Geometry functions
- [simd_dot](./simd_dot-87ssc.md)
  Returns the dot product of two vectors.
- [simd_normalize](./simd_normalize-9o6iq.md)
  Returns a vector pointing in the same direction of the supplied vector, with a length of 1.
- [simd_fast_normalize](./simd_fast_normalize-3vaz.md)
  Returns the fast normalized vector.
- [simd_precise_normalize](./simd_precise_normalize-4vqaw.md)
  Returns the precise normalized vector.
- [simd_project](./simd_project-24ld6.md)
  Returns the first vector projected onto the second vector.
- [simd_precise_project](./simd_precise_project-1cw2i.md)
  Returns the precise projected vector.
- [simd_fast_project](./simd_fast_project-6ymj6.md)
  Returns the fast projected vector.
- [simd_refract](./simd_refract-6q75f.md)
  Returns the refraction direction of an incident vector, a unit normal vector, and an index of refraction eta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_reflect-9r760)*