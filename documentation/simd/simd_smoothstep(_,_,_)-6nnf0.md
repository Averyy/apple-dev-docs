# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_half32, _ edge1: simd_half32, _ x: simd_half32) -> simd_half32
```

```c
static simd_half32 simd_smoothstep(simd_half32 edge0, simd_half32 edge1, simd_half32 x);
```

## See Also

### Interpolation functions
- [func simd_mix(simd_half32, simd_half32, simd_half32) -> simd_half32](./simd_mix%28_,_,_%29-4qwly.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-6nnf0)*