# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ushort8, _ min: simd_ushort8, _ max: simd_ushort8) -> simd_ushort8
```

```c
static simd_ushort8 simd_clamp(simd_ushort8 x, simd_ushort8 min, simd_ushort8 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ushort8, simd_ushort8) -> simd_bool](./simd_equal%28_,_%29-3fkex.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-81cik)*