# simd_make_int3_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from the specified two-element vector, and other elements undefined.

## Declaration

```swift
func simd_make_int3_undef(_ other: simd_int2) -> simd_int3
```

```c
static simd_int3 simd_make_int3_undef(simd_int2 other);
```

## See Also

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_int3(simd_int2) -> simd_int3](./simd_make_int3%28_%29-2tix4.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_int3(simd_int3) -> simd_int3](./simd_make_int3%28_%29-2r609.md)
  Returns a new vector from the specified vector.
- [func simd_make_int3(simd_int4) -> simd_int3](./simd_make_int3%28_%29-3fioe.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_int3(simd_int8) -> simd_int3](./simd_make_int3%28_%29-28n96.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_int3(simd_int16) -> simd_int3](./simd_make_int3%28_%29-4wbrt.md)
  Returns a new vector by truncating the specified sixteen-element vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_int3_undef(_:)-5kpok)*