# simd_abs(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the absolute value of each element in a vector.

## Declaration

```swift
func simd_abs(_ x: simd_int3) -> simd_int3
```

```c
static simd_int3 simd_abs(simd_int3 x);
```

## See Also

### Common Functions
- [func abs(SIMD3<Int32>) -> SIMD3<Int32>](./abs%28_%29-2m9bi.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_int3, simd_int3, simd_int3) -> simd_int3](./simd_clamp%28_,_,_%29-68p0z.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Int32>, min: Int32, max: Int32) -> SIMD3<Int32>](./clamp%28_,min,max%29-7b2i.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD3<Int32>, min: SIMD3<Int32>, max: SIMD3<Int32>) -> SIMD3<Int32>](./clamp%28_,min,max%29-cim1.md)
  Returns each element in a vector clamped to a specified scalar range.
- [func simd_equal(simd_float3, simd_float3) -> simd_bool](./simd_equal%28_,_%29-6i7q4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_abs(_:)-8d4m3)*