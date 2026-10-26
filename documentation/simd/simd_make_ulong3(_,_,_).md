# simd_make_ulong3(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector from the specified scalar values.

## Declaration

```swift
func simd_make_ulong3(_ x: simd_ulong1, _ y: simd_ulong1, _ z: simd_ulong1) -> simd_ulong3
```

```c
static simd_ulong3 simd_make_ulong3(simd_ulong1 x, simd_ulong1 y, simd_ulong1 z);
```

## See Also

### Functions to Create Three-Element Vectors From Scalar Values
- [func simd_make_ulong3(simd_ulong1) -> simd_ulong3](./simd_make_ulong3%28_%29-3eb9a.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_ulong3_undef(simd_ulong1) -> simd_ulong3](./simd_make_ulong3_undef%28_%29-7s0qh.md)
  Returns a new vector with the first element set to a scalar value, and other elements undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_ulong3(_:_:_:))*