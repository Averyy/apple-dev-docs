# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_float3, _ y: simd_float3, _ t: simd_float3) -> simd_float3
```

```c
static simd_float3 simd_mix(simd_float3 x, simd_float3 y, simd_float3 t);
```

## See Also

### Interpolation Functions
- [func mix(SIMD3<Float>, SIMD3<Float>, t: Float) -> SIMD3<Float>](./mix%28_,_,t%29-9o58r.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD3<Float>, SIMD3<Float>, t: SIMD3<Float>) -> SIMD3<Float>](./mix%28_,_,t%29-6c4d3.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_float3, simd_float3, simd_float3) -> simd_float3](./simd_smoothstep%28_,_,_%29-mz0x.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD3<Float>, edge0: SIMD3<Float>, edge1: SIMD3<Float>) -> SIMD3<Float>](./smoothstep%28_,edge0,edge1%29-6m76x.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-6l1x8)*