# simd_equal(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns true if every element in a vector is exactly equal to the corresponding element in a second vector, and otherwise returns false.

## Declaration

```swift
func simd_equal(_ x: simd_char16, _ y: simd_char16) -> simd_bool
```

```c
static simd_bool simd_equal(simd_char16 x, simd_char16 y);
```

## See Also

### Common Functions
- [func simd_abs(simd_char16) -> simd_char16](./simd_abs%28_%29-475ng.md)
  Returns the absolute value of each element in a vector.
- [func simd_clamp(simd_char16, simd_char16, simd_char16) -> simd_char16](./simd_clamp%28_,_,_%29-509lj.md)
  Returns each element in a vector clamped to a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_equal(_:_:)-19z1a)*