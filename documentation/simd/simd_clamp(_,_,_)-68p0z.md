# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_int3, _ min: simd_int3, _ max: simd_int3) -> simd_int3
```

```c
static simd_int3 simd_clamp(simd_int3 x, simd_int3 min, simd_int3 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_int3) -> simd_int3](./simd_abs%28_%29-8d4m3.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD3<Int32>) -> SIMD3<Int32>](./abs%28_%29-2m9bi.md)
  Returns the absolute value of each element in a vector.
- [func clamp(SIMD3<Int32>, min: Int32, max: Int32) -> SIMD3<Int32>](./clamp%28_,min,max%29-7b2i.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Int32>, min: SIMD3<Int32>, max: SIMD3<Int32>) -> SIMD3<Int32>](./clamp%28_,min,max%29-cim1.md)
  Returns each element in a vector clamped to a specified scalar range.
- [func simd_equal(simd_float3, simd_float3) -> simd_bool](./simd_equal%28_,_%29-6i7q4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-68p0z)*