# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_float4, _ y: simd_float4, _ t: simd_float4) -> simd_float4
```

```c
static simd_float4 simd_mix(simd_float4 x, simd_float4 y, simd_float4 t);
```

## See Also

### Interpolation Functions
- [func mix(SIMD4<Float>, SIMD4<Float>, t: Float) -> SIMD4<Float>](./mix%28_,_,t%29-2uufx.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Float>, SIMD4<Float>, t: SIMD4<Float>) -> SIMD4<Float>](./mix%28_,_,t%29-8qz2g.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_float4, simd_float4, simd_float4) -> simd_float4](./simd_smoothstep%28_,_,_%29-33ugy.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD4<Float>, edge0: SIMD4<Float>, edge1: SIMD4<Float>) -> SIMD4<Float>](./smoothstep%28_,edge0,edge1%29-3gx0q.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-5fpv1)*