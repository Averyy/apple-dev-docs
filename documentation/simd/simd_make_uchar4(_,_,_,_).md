# simd_make_uchar4(_:_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from the specified scalar values.

## Declaration

```swift
func simd_make_uchar4(_ x: UInt8, _ y: UInt8, _ z: UInt8, _ w: UInt8) -> simd_uchar4
```

```c
static simd_uchar4 simd_make_uchar4(unsigned char x, unsigned char y, unsigned char z, unsigned char w);
```

## See Also

### Functions to Create Four-Element Vectors From Scalar Values
- [func simd_make_uchar4(UInt8) -> simd_uchar4](./simd_make_uchar4%28_%29-7gszj.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_uchar4_undef(UInt8) -> simd_uchar4](./simd_make_uchar4_undef%28_%29-7uno.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_uchar4(_:_:_:_:))*