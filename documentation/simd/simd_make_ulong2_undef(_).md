# simd_make_ulong2_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_ulong2_undef(_ other: simd_ulong1) -> simd_ulong2
```

```c
static simd_ulong2 simd_make_ulong2_undef(simd_ulong1 other);
```

## See Also

### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_ulong2(simd_ulong1) -> simd_ulong2](./simd_make_ulong2%28_%29-14omj.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong2(simd_ulong1, simd_ulong1) -> simd_ulong2](./simd_make_ulong2%28_,_%29.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_ulong2_undef(_:))*