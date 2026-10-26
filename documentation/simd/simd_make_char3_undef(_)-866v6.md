# simd_make_char3_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_char3_undef(_ other: CChar) -> simd_char3
```

```c
static simd_char3 simd_make_char3_undef(char other);
```

## See Also

### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_char3(CChar) -> simd_char3](./simd_make_char3%28_%29-9zbpd.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char3(CChar, CChar, CChar) -> simd_char3](./simd_make_char3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_char3_undef(_:)-866v6)*