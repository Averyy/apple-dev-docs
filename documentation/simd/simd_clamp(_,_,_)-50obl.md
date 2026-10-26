# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_int4, _ min: simd_int4, _ max: simd_int4) -> simd_int4
```

```c
static simd_int4 simd_clamp(simd_int4 x, simd_int4 min, simd_int4 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_int4) -> simd_int4](./simd_abs%28_%29-81glw.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD4<Int32>) -> SIMD4<Int32>](./abs%28_%29-1b3qo.md)
  Returns the absolute value of each element in a vector.
- [func clamp(SIMD4<Int32>, min: Int32, max: Int32) -> SIMD4<Int32>](./clamp%28_,min,max%29-5if3n.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD4<Int32>, min: SIMD4<Int32>, max: SIMD4<Int32>) -> SIMD4<Int32>](./clamp%28_,min,max%29-5f538.md)
  Returns each element in a vector clamped to a specified scalar range.
- [func simd_equal(simd_int4, simd_int4) -> simd_bool](./simd_equal%28_,_%29-2rypj.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-50obl)*