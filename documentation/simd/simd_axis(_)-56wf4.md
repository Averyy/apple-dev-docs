# simd_axis(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns the normalized axis about which the action of the specified quaternion rotates.

## Declaration

```swift
func simd_axis(_ q: simd_quatd) -> simd_double3
```

```c
static simd_double3 simd_axis(simd_quatd q);
```

#### Return Value

The normalized axis about which the action of the source quaternion rotates.

#### Discussion

This function returns a vector filled with [`nan`](../Swift/double/nan.md) if the source quaternion has a rotation of zero radians.

## Parameters

- `q`: The source quaternion.

## See Also

### Applying geometric operations to quaternions
- [func simd_act(simd_quatd, simd_double3) -> simd_double3](./simd_act%28_,_%29-47h09.md)
  Returns a vector rotated by a quaternion.
- [func act(SIMD3<Double>) -> SIMD3<Double>](./simd_quatd/act%28_%29.md)
  Returns the specified vector rotated by the quaternion.
- [func simd_angle(simd_quatd) -> Double](./simd_angle%28_%29-zuvx.md)
  Returns the angle by which a quaternion rotates.
- [func simd_bezier(simd_quatd, simd_quatd, simd_quatd, simd_quatd, Double) -> simd_quatd](./simd_bezier%28_,_,_,_,_%29-556xd.md)
  Returns the spherical cubic Bezier interpolation between quaternions.
- [func simd_conjugate(simd_quatd) -> simd_quatd](./simd_conjugate%28_%29-98awl.md)
  Returns the conjugate of a quaternion.
- [func simd_imag(simd_quatd) -> simd_double3](./simd_imag%28_%29-2c7fz.md)
  Returns the imaginary (vector) part of a quaternion.
- [func simd_negate(simd_quatd) -> simd_quatd](./simd_negate%28_%29-3ysgu.md)
  Returns the negation of a quaternion.
- [func simd_real(simd_quatd) -> Double](./simd_real%28_%29-75t5f.md)
  Returns the real (scalar) part of a quaternion.
- [func simd_slerp(simd_quatd, simd_quatd, Double) -> simd_quatd](./simd_slerp%28_,_,_%29-65dt5.md)
  Returns a spherical linearly interpolated value along the shortest arc between two quaternions.
- [func simd_slerp_longest(simd_quatd, simd_quatd, Double) -> simd_quatd](./simd_slerp_longest%28_,_,_%29-8hbz2.md)
  Returns a spherical linearly interpolated value along the longest arc between two quaternions.
- [func simd_spline(simd_quatd, simd_quatd, simd_quatd, simd_quatd, Double) -> simd_quatd](./simd_spline%28_,_,_,_,_%29-19wbg.md)
  Returns an interpolated value between two quaternions along a spherical cubic spline.
- [func simd_dot(simd_quatd, simd_quatd) -> Double](./simd_dot%28_,_%29-2bnqp.md)
  Returns the dot product of two quaternions.
- [func dot(simd_quatd, simd_quatd) -> Double](./dot%28_,_%29-438xp.md)
- [func simd_length(simd_quatd) -> Double](./simd_length%28_%29-52o29.md)
  Returns the length of a quaternion.
- [func simd_normalize(simd_quatd) -> simd_quatd](./simd_normalize%28_%29-ud11.md)
  Returns a quaternion pointing in the same direction as the supplied quaternion with a length of 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_axis(_:)-56wf4)*