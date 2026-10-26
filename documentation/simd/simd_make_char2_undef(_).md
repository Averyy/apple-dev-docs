# simd_make_char2_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_char2_undef(_ other: CChar) -> simd_char2
```

```c
static simd_char2 simd_make_char2_undef(char other);
```

## See Also

### Functions to Create Two-Element Vectors From Scalar Values
- [func simd_make_char2(CChar) -> simd_char2](./simd_make_char2%28_%29-97vf3.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char2(CChar, CChar) -> simd_char2](./simd_make_char2%28_,_%29.md)
  Returns a new vector from the specified scalar values.
- [vector2](./vector2-5sh4e.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_char2_undef(_:))*