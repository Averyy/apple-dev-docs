# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uint3, _ y: simd_uint3, _ mask: simd_int3) -> simd_uint3
```

```c
static simd_uint3 simd_bitselect(simd_uint3 x, simd_uint3 y, simd_int3 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uint3) -> simd_bool](./simd_any%28_%29-69h3c.md)
  Returns true if the high-order bit of any element is set; false otherwise.
- [func simd_all(simd_uint3) -> simd_bool](./simd_all%28_%29-1afl6.md)
  Returns true if the high-order bit of every element is set; false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-4hak)*