# simd_make_half3(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from a scalar value and a vector.

## Declaration

```swift
func simd_make_half3(_ x: Float16, _ yz: simd_half2) -> simd_half3
```

```c
static simd_half3 simd_make_half3(_Float16 x, simd_half2 yz);
```

## See Also

### Functions to create three-element vectors from scalar values
- [func simd_make_half3(Float16) -> simd_half3](./simd_make_half3%28_%29-9gqvo.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half3(Float16, Float16, Float16) -> simd_half3](./simd_make_half3%28_,_,_%29.md)
  Returns a new vector from the specified scalar values.
- [func simd_make_half3(simd_half2, Float16) -> simd_half3](./simd_make_half3%28_,_%29-5wwpl.md)
  Returns a new vector from a vector and a scalar value.
- [func simd_make_half3_undef(Float16) -> simd_half3](./simd_make_half3_undef%28_%29-6lcqp.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_half3(_:_:)-4svq0)*