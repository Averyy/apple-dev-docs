# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_int4, _ y: simd_int4, _ mask: simd_int4) -> simd_int4
```

```c
static simd_int4 simd_bitselect(simd_int4 x, simd_int4 y, simd_int4 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_int4) -> simd_bool](./simd_any%28_%29-6cp1b.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_int4) -> simd_bool](./simd_all%28_%29-1jw6t.md)
  Returns true if the high-order bit of every element is set; false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-27mh1)*