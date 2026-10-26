# dot(_:_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func dot(_ lhs: simd_quatf, _ rhs: simd_quatf) -> Float
```

## See Also

### Applying geometric operations to quaternions
- [func simd_act(simd_quatf, simd_float3) -> simd_float3](./simd_act%28_,_%29-2liww.md)
  Returns a vector rotated by a quaternion.
- [func act(SIMD3<Float>) -> SIMD3<Float>](./simd_quatf/act%28_%29.md)
  Returns the specified vector rotated by the quaternion.
- [func simd_angle(simd_quatf) -> Float](./simd_angle%28_%29-zu9h.md)
  Returns the angle by which a quaternion rotates.
- [func simd_axis(simd_quatf) -> simd_float3](./simd_axis%28_%29-56wzs.md)
  Returns the normalized axis about which the action of the specified quaternion rotates.
- [func simd_bezier(simd_quatf, simd_quatf, simd_quatf, simd_quatf, Float) -> simd_quatf](./simd_bezier%28_,_,_,_,_%29-1z3gf.md)
  Returns the spherical cubic Bezier interpolation between quaternions.
- [func simd_conjugate(simd_quatf) -> simd_quatf](./simd_conjugate%28_%29-98bil.md)
  Returns the conjugate of a quaternion.
- [func simd_imag(simd_quatf) -> simd_float3](./simd_imag%28_%29-2c837.md)
  Returns the imaginary (vector) part of a quaternion.
- [func simd_negate(simd_quatf) -> simd_quatf](./simd_negate%28_%29-3yt2y.md)
  Returns the negation of a quaternion.
- [func simd_real(simd_quatf) -> Float](./simd_real%28_%29-75sl3.md)
  Returns the real (scalar) part of a quaternion.
- [func simd_slerp(simd_quatf, simd_quatf, Float) -> simd_quatf](./simd_slerp%28_,_,_%29-u2db.md)
  Returns a spherical linearly interpolated value along the shortest arc between two quaternions.
- [func simd_slerp_longest(simd_quatf, simd_quatf, Float) -> simd_quatf](./simd_slerp_longest%28_,_,_%29-3qens.md)
  Returns a spherical linearly interpolated value along the longest arc between two quaternions.
- [func simd_spline(simd_quatf, simd_quatf, simd_quatf, simd_quatf, Float) -> simd_quatf](./simd_spline%28_,_,_,_,_%29-1ok51.md)
  Returns an interpolated value between two quaternions along a spherical cubic spline.
- [func simd_dot(simd_quatf, simd_quatf) -> Float](./simd_dot%28_,_%29-7frqx.md)
  Returns the dot product of two quaternions.
- [func simd_length(simd_quatf) -> Float](./simd_length%28_%29-52nf5.md)
  Returns the length of a quaternion.
- [func simd_normalize(simd_quatf) -> simd_quatf](./simd_normalize%28_%29-uch9.md)
  Returns a quaternion pointing in the same direction as the supplied quaternion with a length of 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/dot(_:_:)-2en8e)*