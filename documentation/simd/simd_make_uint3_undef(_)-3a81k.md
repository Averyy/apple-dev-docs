# simd_make_uint3_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from the specified two-element vector, and other elements undefined.

## Declaration

```swift
func simd_make_uint3_undef(_ other: simd_uint2) -> simd_uint3
```

```c
static simd_uint3 simd_make_uint3_undef(simd_uint2 other);
```

## See Also

### Functions to Create Three-Element Vectors From Other Vectors
- [func simd_make_uint3(simd_uint2) -> simd_uint3](./simd_make_uint3%28_%29-7e6jd.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_uint3(simd_uint3) -> simd_uint3](./simd_make_uint3%28_%29-7h348.md)
  Returns a new vector from the specified vector.
- [func simd_make_uint3(simd_uint4) -> simd_uint3](./simd_make_uint3%28_%29-77mmf.md)
  Returns a new vector by truncating the specified four-element vector.
- [func simd_make_uint3(simd_uint8) -> simd_uint3](./simd_make_uint3%28_%29-6sqjv.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_uint3(simd_uint16) -> simd_uint3](./simd_make_uint3%28_%29-6rqe9.md)
  Returns a new vector by truncating the specified sixteen-element vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_uint3_undef(_:)-3a81k)*