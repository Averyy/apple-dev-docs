# simd_make_ulong4(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from two scalar values and a vector.

## Declaration

```swift
func simd_make_ulong4(_ x: simd_ulong1, _ y: simd_ulong1, _ zw: simd_ulong2) -> simd_ulong4
```

```c
static simd_ulong4 simd_make_ulong4(simd_ulong1 x, simd_ulong1 y, simd_ulong2 zw);
```

## See Also

### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_ulong4(simd_ulong1, simd_ulong2, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_,_%29-8asm5.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_ulong4(simd_ulong1, simd_ulong3) -> simd_ulong4](./simd_make_ulong4%28_,_%29-5mtth.md)
  Returns a new vector from a scalar value and a vector.
- [func simd_make_ulong4(simd_ulong2, simd_ulong1, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_,_%29-8g4ch.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_ulong4(simd_ulong3, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_%29-cnt3.md)
  Returns a new vector from a vector and a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_ulong4(_:_:_:)-4du2m)*