# simd_make_long2_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_long2_undef(_ other: simd_long1) -> simd_long2
```

```c
static simd_long2 simd_make_long2_undef(simd_long1 other);
```

## See Also

### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_long2(simd_long1) -> simd_long2](./simd_make_long2%28_%29-698vu.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_long2(simd_long1, simd_long1) -> simd_long2](./simd_make_long2%28_,_%29.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_long2_undef(_:))*