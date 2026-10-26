# simd_make_uint4_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_uint4_undef(_ other: UInt32) -> simd_uint4
```

```c
static simd_uint4 simd_make_uint4_undef(unsigned int other);
```

## See Also

### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_uint4(UInt32) -> simd_uint4](./simd_make_uint4%28_%29-1vdsn.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uint4(UInt32, UInt32, UInt32, UInt32) -> simd_uint4](./simd_make_uint4%28_,_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [vector4](./vector4-2s268.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_uint4_undef(_:)-5wuto)*