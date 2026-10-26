# simd_make_int4(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from two scalar values and a vector.

## Declaration

```swift
func simd_make_int4(_ x: Int32, _ y: Int32, _ zw: simd_int2) -> simd_int4
```

```c
static simd_int4 simd_make_int4(int x, int y, simd_int2 zw);
```

## See Also

### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_int4(simd_int2, Int32, Int32) -> simd_int4](./simd_make_int4%28_,_,_%29-7cjm7.md)
  Returns a new vector from a vector and scalar values.
- [func simd_make_int4(simd_int3, Int32) -> simd_int4](./simd_make_int4%28_,_%29-7rrqd.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_int4(Int32, simd_int2, Int32) -> simd_int4](./simd_make_int4%28_,_,_%29-8of8y.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_int4(Int32, simd_int3) -> simd_int4](./simd_make_int4%28_,_%29-6p0ui.md)
  Returns a new vector from a scalar value and a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_int4(_:_:_:)-9tjlm)*