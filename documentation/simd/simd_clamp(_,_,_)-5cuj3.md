# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ulong4, _ min: simd_ulong4, _ max: simd_ulong4) -> simd_ulong4
```

```c
static simd_ulong4 simd_clamp(simd_ulong4 x, simd_ulong4 min, simd_ulong4 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ulong4, simd_ulong4) -> simd_bool](./simd_equal%28_,_%29-8d8x.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-5cuj3)*