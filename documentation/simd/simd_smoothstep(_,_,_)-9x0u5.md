# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_half2, _ edge1: simd_half2, _ x: simd_half2) -> simd_half2
```

```c
static simd_half2 simd_smoothstep(simd_half2 edge0, simd_half2 edge1, simd_half2 x);
```

## See Also

### Interpolation functions
- [func simd_mix(simd_half2, simd_half2, simd_half2) -> simd_half2](./simd_mix%28_,_,_%29-33iiq.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-9x0u5)*