# simd_make_double3_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from the specified two-element vector, and other elements undefined.

## Declaration

```swift
func simd_make_double3_undef(_ other: simd_double2) -> simd_double3
```

```c
static simd_double3 simd_make_double3_undef(simd_double2 other);
```

## See Also

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_double3(simd_double2) -> simd_double3](./simd_make_double3%28_%29-5ti92.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_double3(simd_double3) -> simd_double3](./simd_make_double3%28_%29-5qigh.md)
  Returns a new vector from the specified vector.
- [func simd_make_double3(simd_double4) -> simd_double3](./simd_make_double3%28_%29-5zuas.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_double3(simd_double8) -> simd_double3](./simd_make_double3%28_%29-4tl5k.md)
  Returns a new vector by truncating the specified eight-element vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_double3_undef(_:)-95a07)*