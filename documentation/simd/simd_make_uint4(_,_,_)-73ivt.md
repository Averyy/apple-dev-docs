# simd_make_uint4(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from two scalar values and a vector.

## Declaration

```swift
func simd_make_uint4(_ x: UInt32, _ y: UInt32, _ zw: simd_uint2) -> simd_uint4
```

```c
static simd_uint4 simd_make_uint4(unsigned int x, unsigned int y, simd_uint2 zw);
```

## See Also

### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_uint4(simd_uint2, UInt32, UInt32) -> simd_uint4](./simd_make_uint4%28_,_,_%29-5ftg3.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_uint4(simd_uint3, UInt32) -> simd_uint4](./simd_make_uint4%28_,_%29-9arct.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_uint4(UInt32, simd_uint2, UInt32) -> simd_uint4](./simd_make_uint4%28_,_,_%29-45zbh.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_uint4(UInt32, simd_uint3) -> simd_uint4](./simd_make_uint4%28_,_%29-4kh9u.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-91xr7.md)
  Returns a new vector from a vector and a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_uint4(_:_:_:)-73ivt)*