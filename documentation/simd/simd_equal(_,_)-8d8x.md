# simd_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.

## Declaration

```swift
func simd_equal(_ x: simd_ulong4, _ y: simd_ulong4) -> simd_bool
```

```c
static simd_bool simd_equal(simd_ulong4 x, simd_ulong4 y);
```

## See Also

### Common Functions
- [func simd_clamp(simd_ulong4, simd_ulong4, simd_ulong4) -> simd_ulong4](./simd_clamp%28_,_,_%29-5cuj3.md)
  Returns each element in a vector clamped to a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_equal(_:_:)-8d8x)*