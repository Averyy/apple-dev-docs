# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_half4, _ edge1: simd_half4, _ x: simd_half4) -> simd_half4
```

```c
static simd_half4 simd_smoothstep(simd_half4 edge0, simd_half4 edge1, simd_half4 x);
```

## See Also

### Interpolation functions
- [func simd_mix(simd_half4, simd_half4, simd_half4) -> simd_half4](./simd_mix%28_,_,_%29-4uou1.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-7gsfq)*