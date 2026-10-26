# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_half8, _ edge1: simd_half8, _ x: simd_half8) -> simd_half8
```

```c
static simd_half8 simd_smoothstep(simd_half8 edge0, simd_half8 edge1, simd_half8 x);
```

## See Also

### Interpolation functions
- [func simd_mix(simd_half8, simd_half8, simd_half8) -> simd_half8](./simd_mix%28_,_,_%29-6gojc.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-96q78)*