# simd_make_int4(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from a vector and scalar values.

## Declaration

```swift
func simd_make_int4(_ xy: simd_int2, _ z: Int32, _ w: Int32) -> simd_int4
```

```c
static simd_int4 simd_make_int4(simd_int2 xy, int z, int w);
```

## See Also

### Functions to Create Four-Element Vectors From Combinations of Vectors and Scalar Values
- [func simd_make_int4(simd_int3, Int32) -> simd_int4](./simd_make_int4%28_,_%29-7rrqd.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_int4(Int32, Int32, simd_int2) -> simd_int4](./simd_make_int4%28_,_,_%29-9tjlm.md)
  Returns a new vector from two scalar values and a vector.
- [func simd_make_int4(Int32, simd_int2, Int32) -> simd_int4](./simd_make_int4%28_,_,_%29-8of8y.md)
  Returns a new vector from a scalar value, a vector, and a scalar value.
- [func simd_make_int4(Int32, simd_int3) -> simd_int4](./simd_make_int4%28_,_%29-6p0ui.md)
  Returns a new vector from a scalar value and a vector.
- [vector4](./vector4-6wxif.md)
  Returns a new vector from a vector and a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_int4(_:_:_:)-7cjm7)*