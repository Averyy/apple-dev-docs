# simd_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.

## Declaration

```swift
func simd_equal(_ x: simd_uint3, _ y: simd_uint3) -> simd_bool
```

```c
static simd_bool simd_equal(simd_uint3 x, simd_uint3 y);
```

## See Also

### Common Functions
- [func simd_clamp(simd_uint3, simd_uint3, simd_uint3) -> simd_uint3](./simd_clamp%28_,_,_%29-7ssi2.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<UInt32>, min: UInt32, max: UInt32) -> SIMD3<UInt32>](./clamp%28_,min,max%29-dhvg.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<UInt32>, min: SIMD3<UInt32>, max: SIMD3<UInt32>) -> SIMD3<UInt32>](./clamp%28_,min,max%29-gp7z.md)
  Returns each element in a vector clamped to a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_equal(_:_:)-57xz1)*