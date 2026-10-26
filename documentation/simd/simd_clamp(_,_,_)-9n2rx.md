# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_int2, _ min: simd_int2, _ max: simd_int2) -> simd_int2
```

```c
static simd_int2 simd_clamp(simd_int2 x, simd_int2 min, simd_int2 max);
```

## See Also

### Common Functions
- [func simd_abs(simd_int2) -> simd_int2](./simd_abs%28_%29-88kbu.md)
  Returns the absolute value of each element in a vector.
- [func abs(SIMD2<Int32>) -> SIMD2<Int32>](./abs%28_%29-770jg.md)
  Returns the absolute value of each element in a vector.
- [func clamp(SIMD2<Int32>, min: SIMD2<Int32>, max: SIMD2<Int32>) -> SIMD2<Int32>](./clamp%28_,min,max%29-y596.md)
  Returns each element in a vector clamped to a specified range.
- [func clamp(SIMD2<Int32>, min: Int32, max: Int32) -> SIMD2<Int32>](./clamp%28_,min,max%29-11cyt.md)
  Returns each element in a vector clamped to a specified scalar range.
- [func simd_equal(simd_int2, simd_int2) -> simd_bool](./simd_equal%28_,_%29-8sg1t.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-9n2rx)*