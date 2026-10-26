# simd_make_half2_undef(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new vector with the first element set to a scalar value, and other elements undefined.

## Declaration

```swift
func simd_make_half2_undef(_ other: Float16) -> simd_half2
```

```c
static simd_half2 simd_make_half2_undef(_Float16 other);
```

## See Also

### Functions to create two-element vectors from scalar values
- [func simd_make_half2(Float16) -> simd_half2](./simd_make_half2%28_%29-9q31.md)
  Returns a new vector with the first element set to a scalar value, and other elements set to zero.
- [func simd_make_half2(Float16, Float16) -> simd_half2](./simd_make_half2%28_,_%29.md)
  Returns a new vector from the specified scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_make_half2_undef(_:))*