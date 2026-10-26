# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ulong3, _ min: simd_ulong3, _ max: simd_ulong3) -> simd_ulong3
```

```c
static simd_ulong3 simd_clamp(simd_ulong3 x, simd_ulong3 min, simd_ulong3 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ulong3, simd_ulong3) -> simd_bool](./simd_equal%28_,_%29-2p336.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-5ce6)*