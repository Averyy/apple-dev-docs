# simd_make_ulong4_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_ulong4_undef(_ other: simd_ulong1) -> simd_ulong4
```

```c
static simd_ulong4 simd_make_ulong4_undef(simd_ulong1 other);
```

## See Also

### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_ulong4(simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_%29-6kawu.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong4(simd_ulong1, simd_ulong1, simd_ulong1, simd_ulong1) -> simd_ulong4](./simd_make_ulong4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [vector4](./vector4-8yxgu.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_ulong4_undef(_:)-jgtr)*