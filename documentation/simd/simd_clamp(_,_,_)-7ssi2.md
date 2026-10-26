# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_uint3, _ min: simd_uint3, _ max: simd_uint3) -> simd_uint3
```

```c
static simd_uint3 simd_clamp(simd_uint3 x, simd_uint3 min, simd_uint3 max);
```

## See Also

### Common Functions
- [func clamp(SIMD3<UInt32>, min: UInt32, max: UInt32) -> SIMD3<UInt32>](./clamp%28_,min,max%29-dhvg.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<UInt32>, min: SIMD3<UInt32>, max: SIMD3<UInt32>) -> SIMD3<UInt32>](./clamp%28_,min,max%29-gp7z.md)
  Returns each element in a vector clamped to a specified range.
- [func simd_equal(simd_uint3, simd_uint3) -> simd_bool](./simd_equal%28_,_%29-57xz1.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-7ssi2)*