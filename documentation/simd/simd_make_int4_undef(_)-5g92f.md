# simd_make_int4_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from the specified two-element vector, and other elements undefined.

## Declaration

```swift
func simd_make_int4_undef(_ other: simd_int2) -> simd_int4
```

```c
static simd_int4 simd_make_int4_undef(simd_int2 other);
```

## See Also

### Functions to Create Four-Element Vectors From Other Vectors
- [func simd_make_int4(simd_int2) -> simd_int4](./simd_make_int4%28_%29-1suou.md)
  Returns a new vector from the specified two-element vector, and other elements set to zero.
- [func simd_make_int4(simd_int3) -> simd_int4](./simd_make_int4%28_%29-1wbev.md)
  Returns a new vector from the specified three-element vector, and other elements set to zero.
- [func simd_make_int4(simd_int4) -> simd_int4](./simd_make_int4%28_%29-1kx2w.md)
  Returns a new vector from the specified vector.
- [func simd_make_int4(simd_int8) -> simd_int4](./simd_make_int4%28_%29-2qk04.md)
  Returns a new vector by truncating the specified eight-element vector.
- [func simd_make_int4(simd_int16) -> simd_int4](./simd_make_int4%28_%29-2rtb0.md)
  Returns a new vector by truncating the specified sixteen-element vector.
- [func simd_make_int4(simd_int2, simd_int2) -> simd_int4](./simd_make_int4%28_,_%29-4phxy.md)
  Returns a new vector from the specified vectors.
- [func simd_make_int4_undef(simd_int3) -> simd_int4](./simd_make_int4_undef%28_%29-5dw9q.md)
  Returns a new vector from the specified three-element vector, and other elements undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_int4_undef(_:)-5g92f)*