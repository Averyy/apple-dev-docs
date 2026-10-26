# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_float2, _ edge1: simd_float2, _ x: simd_float2) -> simd_float2
```

```c
static simd_float2 simd_smoothstep(simd_float2 edge0, simd_float2 edge1, simd_float2 x);
```

## See Also

### Interpolation Functions
- [func simd_mix(simd_float2, simd_float2, simd_float2) -> simd_float2](./simd_mix%28_,_,_%29-bvhh.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Float>, SIMD2<Float>, t: Float) -> SIMD2<Float>](./mix%28_,_,t%29-2z3yo.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Float>, SIMD2<Float>, t: SIMD2<Float>) -> SIMD2<Float>](./mix%28_,_,t%29-14tli.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func smoothstep(SIMD2<Float>, edge0: SIMD2<Float>, edge1: SIMD2<Float>) -> SIMD2<Float>](./smoothstep%28_,edge0,edge1%29-43udr.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-7iziv)*