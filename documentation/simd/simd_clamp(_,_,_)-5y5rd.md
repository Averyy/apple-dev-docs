# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ulong2, _ min: simd_ulong2, _ max: simd_ulong2) -> simd_ulong2
```

```c
static simd_ulong2 simd_clamp(simd_ulong2 x, simd_ulong2 min, simd_ulong2 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ulong2, simd_ulong2) -> simd_bool](./simd_equal%28_,_%29-80jzi.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-5y5rd)*