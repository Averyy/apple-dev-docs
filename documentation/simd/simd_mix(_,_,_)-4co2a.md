# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_half3, _ y: simd_half3, _ t: simd_half3) -> simd_half3
```

```c
static simd_half3 simd_mix(simd_half3 x, simd_half3 y, simd_half3 t);
```

## See Also

### Interpolation functions
- [func simd_smoothstep(simd_half3, simd_half3, simd_half3) -> simd_half3](./simd_smoothstep%28_,_,_%29-4rnii.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-4co2a)*