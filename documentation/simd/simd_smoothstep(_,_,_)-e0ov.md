# simd_smoothstep(_:_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns an element-wise smoothly interpolated value between two vectors.

## Declaration

```swift
func simd_smoothstep(_ edge0: simd_double2, _ edge1: simd_double2, _ x: simd_double2) -> simd_double2
```

```c
static simd_double2 simd_smoothstep(simd_double2 edge0, simd_double2 edge1, simd_double2 x);
```

## See Also

### Interpolation Functions
- [func smoothstep(SIMD2<Double>, edge0: SIMD2<Double>, edge1: SIMD2<Double>) -> SIMD2<Double>](./smoothstep%28_,edge0,edge1%29-2wqo9.md)
  Returns an element-wise smoothly interpolated value between two vectors.
- [func simd_mix(simd_double2, simd_double2, simd_double2) -> simd_double2](./simd_mix%28_,_,_%29-v083.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Double>, SIMD2<Double>, t: Double) -> SIMD2<Double>](./mix%28_,_,t%29-7bjg5.md)
  Returns an element-wise linearly interpolated value between two vectors.
- [func mix(SIMD2<Double>, SIMD2<Double>, t: SIMD2<Double>) -> SIMD2<Double>](./mix%28_,_,t%29-3hfwb.md)
  Returns an element-wise linearly interpolated value between two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-e0ov)*