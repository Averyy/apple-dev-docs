# simd_clamp(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func simd_clamp(_ x: simd_half16, _ min: simd_half16, _ max: simd_half16) -> simd_half16
```

```c
static simd_half16 simd_clamp(simd_half16 x, simd_half16 min, simd_half16 max);
```

## Discussion

X clamped to the range [min, max].

Note that if you want to clamp all lanes to the same range, you can use a scalar value for min and max.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_clamp(_:_:_:)-7ck0a)*