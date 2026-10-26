# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ulong8, _ min: simd_ulong8, _ max: simd_ulong8) -> simd_ulong8
```

```c
static simd_ulong8 simd_clamp(simd_ulong8 x, simd_ulong8 min, simd_ulong8 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ulong8, simd_ulong8) -> simd_bool](./simd_equal%28_,_%29-4dws0.md)
  Returns true if every element in a matrix is exactly equal to the corresponding element in a second matrix, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-6mt76)*