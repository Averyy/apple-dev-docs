# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_uchar64, _ y: simd_uchar64, _ mask: simd_char64) -> simd_uchar64
```

```c
static simd_uchar64 simd_bitselect(simd_uchar64 x, simd_uchar64 y, simd_char64 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_uchar64) -> simd_bool](./simd_any%28_%29-jl1j.md)
- [func simd_all(simd_uchar64) -> simd_bool](./simd_all%28_%29-2m0jp.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-2bway)*