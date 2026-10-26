# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_float4, _ edge1: simd_float4, _ x: simd_float4) -> simd_float4
```

```c
static simd_float4 simd_smoothstep(simd_float4 edge0, simd_float4 edge1, simd_float4 x);
```

## See Also

### Interpolation Functions
- [func simd_mix(simd_float4, simd_float4, simd_float4) -> simd_float4](./simd_mix%28_,_,_%29-5fpv1.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Float>, SIMD4<Float>, t: Float) -> SIMD4<Float>](./mix%28_,_,t%29-2uufx.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Float>, SIMD4<Float>, t: SIMD4<Float>) -> SIMD4<Float>](./mix%28_,_,t%29-8qz2g.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func smoothstep(SIMD4<Float>, edge0: SIMD4<Float>, edge1: SIMD4<Float>) -> SIMD4<Float>](./smoothstep%28_,edge0,edge1%29-3gx0q.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-33ugy)*