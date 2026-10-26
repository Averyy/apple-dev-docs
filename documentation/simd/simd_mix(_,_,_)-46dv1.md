# simd_mix(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise linearly interpolated value between two vectors.

## Declaration

```swift
func simd_mix(_ x: simd_double3, _ y: simd_double3, _ t: simd_double3) -> simd_double3
```

```c
static simd_double3 simd_mix(simd_double3 x, simd_double3 y, simd_double3 t);
```

## See Also

### Interpolation Functions
- [func mix(SIMD3<Double>, SIMD3<Double>, t: Double) -> SIMD3<Double>](./mix%28_,_,t%29-1dp7m.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD3<Double>, SIMD3<Double>, t: SIMD3<Double>) -> SIMD3<Double>](./mix%28_,_,t%29-5ifg3.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func simd_smoothstep(simd_double3, simd_double3, simd_double3) -> simd_double3](./simd_smoothstep%28_,_,_%29-9hwr9.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func smoothstep(SIMD3<Double>, edge0: SIMD3<Double>, edge1: SIMD3<Double>) -> SIMD3<Double>](./smoothstep%28_,edge0,edge1%29-5ih1o.md)
  Returns an element-wise smoothly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_mix(_:_:_:)-46dv1)*