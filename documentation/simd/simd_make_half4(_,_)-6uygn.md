# simd_make_half4(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from a vector and a scalar value.

## Declaration

```swift
func simd_make_half4(_ xyz: simd_half3, _ w: Float16) -> simd_half4
```

```c
static simd_half4 simd_make_half4(simd_half3 xyz, _Float16 w);
```

## See Also

### Functions to create four-element vectors from scalar values
- [func simd_make_half4(Float16) -> simd_half4](./simd_make_half4%28_%29-6lkh9.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half4(Float16, Float16, Float16, Float16) -> simd_half4](./simd_make_half4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_half4_undef(Float16) -> simd_half4](./simd_make_half4_undef%28_%29-4axzi.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.
- [func simd_make_half4(Float16, simd_half3) -> simd_half4](./simd_make_half4%28_,_%29-2n13g.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_half4(Float16, simd_half2, Float16) -> simd_half4](./simd_make_half4%28_,_,_%29-43wuv.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_half4(Float16, Float16, simd_half2) -> simd_half4](./simd_make_half4%28_,_,_%29-74ybg.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_half4(simd_half2, Float16, Float16) -> simd_half4](./simd_make_half4%28_,_,_%29-6g0kb.md)
  Returns a new vector from a vector and scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_half4(_:_:)-6uygn)*