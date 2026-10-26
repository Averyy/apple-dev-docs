# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns each element in a vector clamped to a specified range.

## Declaration

```swift
func simd_clamp(_ x: simd_ushort4, _ min: simd_ushort4, _ max: simd_ushort4) -> simd_ushort4
```

```c
static simd_ushort4 simd_clamp(simd_ushort4 x, simd_ushort4 min, simd_ushort4 max);
```

## See Also

### Common Functions
- [func simd_equal(simd_ushort4, simd_ushort4) -> simd_bool](./simd_equal%28_,_%29-9613j.md)
  Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-72wjb)*