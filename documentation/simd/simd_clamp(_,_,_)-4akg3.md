# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ushort3, _ min: simd_ushort3, _ max: simd_ushort3) -> simd_ushort3
```

```c
static simd_ushort3 simd_clamp(simd_ushort3 x, simd_ushort3 min, simd_ushort3 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ushort3, simd_ushort3) -> simd_bool](./simd_equal%28_,_%29-9b270.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-4akg3)*