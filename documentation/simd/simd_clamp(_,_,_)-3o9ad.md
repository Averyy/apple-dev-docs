# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ushort2, _ min: simd_ushort2, _ max: simd_ushort2) -> simd_ushort2
```

```c
static simd_ushort2 simd_clamp(simd_ushort2 x, simd_ushort2 min, simd_ushort2 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ushort2, simd_ushort2) -> simd_bool](./simd_equal%28_,_%29-ktbu.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-3o9ad)*