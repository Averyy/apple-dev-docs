# simd_make_char4(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from the specified scalar values.

## Declaration

```swift
func simd_make_char4(_ x: CChar, _ y: CChar, _ z: CChar, _ w: CChar) -> simd_char4
```

```c
static simd_char4 simd_make_char4(char x, char y, char z, char w);
```

## See Also

### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_char4(CChar) -> simd_char4](./simd_make_char4%28_%29-8kfe3.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_char4_undef(CChar) -> simd_char4](./simd_make_char4_undef%28_%29-99pql.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_char4(_:_:_:_:))*