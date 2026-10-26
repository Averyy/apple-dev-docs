# simd_make_ulong3_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_ulong3_undef(_ other: simd_ulong1) -> simd_ulong3
```

```c
static simd_ulong3 simd_make_ulong3_undef(simd_ulong1 other);
```

## See Also

### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_ulong3(simd_ulong1) -> simd_ulong3](./simd_make_ulong3%28_%29-3eb9a.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong3(simd_ulong1, simd_ulong1, simd_ulong1) -> simd_ulong3](./simd_make_ulong3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [vector3](./vector3-6utbv.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_ulong3_undef(_:)-7s0qh)*