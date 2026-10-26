# simd_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.

## Declaration

```swift
func simd_equal(_ x: simd_float3, _ y: simd_float3) -> simd_bool
```

```c
static simd_bool simd_equal(simd_float3 x, simd_float3 y);
```

## See Also

### Common Functions
- [func simd_abs(simd_int3) -> simd_int3](./simd_abs%28_%29-8d4m3.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD3<Int32>) -> SIMD3<Int32>](./abs%28_%29-2m9bi.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_int3, simd_int3, simd_int3) -> simd_int3](./simd_clamp%28_,_,_%29-68p0z.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Int32>, min: Int32, max: Int32) -> SIMD3<Int32>](./clamp%28_,min,max%29-7b2i.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Int32>, min: SIMD3<Int32>, max: SIMD3<Int32>) -> SIMD3<Int32>](./clamp%28_,min,max%29-cim1.md)
  Returns each element in a vector clamped to a specified scalar range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_equal(_:_:)-6i7q4)*