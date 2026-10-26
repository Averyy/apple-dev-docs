# simd_make_char4_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_char4_undef(_ other: CChar) -> simd_char4
```

```c
static simd_char4 simd_make_char4_undef(char other);
```

## See Also

### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_char4(CChar) -> simd_char4](./simd_make_char4%28_%29-8kfe3.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char4(CChar, CChar, CChar, CChar) -> simd_char4](./simd_make_char4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [vector4](./vector4-2lql7.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_char4_undef(_:)-99pql)*