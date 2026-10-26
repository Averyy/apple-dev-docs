# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_float2, _ y: simd_float2, _ t: simd_float2) -> simd_float2
```

```c
static simd_float2 simd_mix(simd_float2 x, simd_float2 y, simd_float2 t);
```

## See Also

### Interpolation Functions
- [func mix(SIMD2<Float>, SIMD2<Float>, t: Float) -> SIMD2<Float>](./mix%28_,_,t%29-2z3yo.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Float>, SIMD2<Float>, t: SIMD2<Float>) -> SIMD2<Float>](./mix%28_,_,t%29-14tli.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_float2, simd_float2, simd_float2) -> simd_float2](./simd_smoothstep%28_,_,_%29-7iziv.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD2<Float>, edge0: SIMD2<Float>, edge1: SIMD2<Float>) -> SIMD2<Float>](./smoothstep%28_,edge0,edge1%29-43udr.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-bvhh)*