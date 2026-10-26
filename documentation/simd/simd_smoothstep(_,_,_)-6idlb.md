# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_double4, _ edge1: simd_double4, _ x: simd_double4) -> simd_double4
```

```c
static simd_double4 simd_smoothstep(simd_double4 edge0, simd_double4 edge1, simd_double4 x);
```

## See Also

### Interpolation Functions
- [func smoothstep(SIMD4<Double>, edge0: SIMD4<Double>, edge1: SIMD4<Double>) -> SIMD4<Double>](./smoothstep%28_,edge0,edge1%29-3gmrv.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(simd_double4, simd_double4, simd_double4) -> simd_double4](./simd_mix%28_,_,_%29-49aeg.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Double>, SIMD4<Double>, t: Double) -> SIMD4<Double>](./mix%28_,_,t%29-9jxxl.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD4<Double>, SIMD4<Double>, t: SIMD4<Double>) -> SIMD4<Double>](./mix%28_,_,t%29-92fbo.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-6idlb)*