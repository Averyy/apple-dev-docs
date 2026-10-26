# simd_bitselect(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a vector that contains elements from either the first or second parameter, based on the corresponding element in the third parameter.

## Declaration

```swift
func simd_bitselect(_ x: simd_int8, _ y: simd_int8, _ mask: simd_int8) -> simd_int8
```

```c
static simd_int8 simd_bitselect(simd_int8 x, simd_int8 y, simd_int8 mask);
```

## See Also

### Logic and Bitwise Functions
- [func simd_any(simd_int8) -> simd_bool](./simd_any%28_%29-6pigr.md)
- [func simd_all(simd_int8) -> simd_bool](./simd_all%28_%29-1yx6x.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_bitselect(_:_:_:)-361vz)*