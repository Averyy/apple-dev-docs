# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ushort16, _ min: simd_ushort16, _ max: simd_ushort16) -> simd_ushort16
```

```c
static simd_ushort16 simd_clamp(simd_ushort16 x, simd_ushort16 min, simd_ushort16 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ushort16, simd_ushort16) -> simd_bool](./simd_equal%28_,_%29-9luz4.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-5hezy)*