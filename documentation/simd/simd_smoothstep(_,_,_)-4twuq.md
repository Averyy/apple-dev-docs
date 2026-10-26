# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_half16, _ edge1: simd_half16, _ x: simd_half16) -> simd_half16
```

```c
static simd_half16 simd_smoothstep(simd_half16 edge0, simd_half16 edge1, simd_half16 x);
```

## See Also

### Interpolation functions
- [func simd_mix(simd_half16, simd_half16, simd_half16) -> simd_half16](./simd_mix%28_,_,_%29-7hbla.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-4twuq)*