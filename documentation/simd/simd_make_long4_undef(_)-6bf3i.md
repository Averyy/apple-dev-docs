# simd_make_long4_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_long4_undef(_ other: simd_long1) -> simd_long4
```

```c
static simd_long4 simd_make_long4_undef(simd_long1 other);
```

## See Also

### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_long4(simd_long1) -> simd_long4](./simd_make_long4%28_%29-4ir93.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_long4(simd_long1, simd_long1, simd_long1, simd_long1) -> simd_long4](./simd_make_long4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_long4_undef(_:)-6bf3i)*