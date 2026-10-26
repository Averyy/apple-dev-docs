# simd_make_char4(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from two scalar values and a vector.

## Declaration

```swift
func simd_make_char4(_ x: CChar, _ y: CChar, _ zw: simd_char2) -> simd_char4
```

```c
static simd_char4 simd_make_char4(char x, char y, simd_char2 zw);
```

## See Also

### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Value
- [func simd_make_char4(simd_char2, CChar, CChar) -> simd_char4](./simd_make_char4%28_,_,_%29-82ftd.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_char4(simd_char3, CChar) -> simd_char4](./simd_make_char4%28_,_%29-226qq.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_char4(CChar, simd_char2, CChar) -> simd_char4](./simd_make_char4%28_,_,_%29-94kun.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_char4(CChar, simd_char3) -> simd_char4](./simd_make_char4%28_,_%29-76rpp.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-4dfou.md)
  Returns a new vector from a vector and a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_char4(_:_:_:)-9mb46)*