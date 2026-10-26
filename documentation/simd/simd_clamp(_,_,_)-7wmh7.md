# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the absolute value of each element in a vector.

## Declaration

```swift
func simd_clamp(_ x: simd_short3, _ min: simd_short3, _ max: simd_short3) -> simd_short3
```

```c
static simd_short3 simd_clamp(simd_short3 x, simd_short3 min, simd_short3 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_short3) -> simd_short3](./simd_abs%28_%29-8d6jr.md)
  Returns the absolute value of each element in a vector.
- [func simd_equal(simd_short3, simd_short3) -> simd_bool](./simd_equal%28_,_%29-40ux3.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-7wmh7)*