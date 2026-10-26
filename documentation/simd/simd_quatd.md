# simd_quatd

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A double-precision quaternion.

## Declaration

```swift
struct simd_quatd
```

```c
typedef struct { ... } simd_quatd;
```

## Topics

### Initializing a quaternion
- [init()](./simd_quatd/init%28%29.md)
  Creates a new quaternion.
- [init(vector: simd_double4)](./simd_quatd/init%28vector%29.md)
  Creates a new quaternion from a four-element vector.
- [init(simd_double3x3)](./simd_quatd/init%28_%29-791zk.md)
  Creates a new quaternion from a 3 x 3 rotation matrix.
- [init(simd_double4x4)](./simd_quatd/init%28_%29-5vcd5.md)
  Creates a new quaternion from a 4 x 4 rotation matrix.
- [init(angle: Double, axis: SIMD3<Double>)](./simd_quatd/init%28angle,axis%29.md)
  Creates a new quaternion with an action that’s a rotation about an axis.
- [init(from: SIMD3<Double>, to: SIMD3<Double>)](./simd_quatd/init%28from,to%29.md)
  Creates a new quaternion with an action that’s a rotation between two vectors.
- [init(ix: Double, iy: Double, iz: Double, r: Double)](./simd_quatd/init%28ix,iy,iz,r%29.md)
  Creates a new quaternion from four scalar values that specify the imaginary and real parts.
- [init(real: Double, imag: SIMD3<Double>)](./simd_quatd/init%28real,imag%29.md)
  Creates a new quaternion from a scalar real part and a vector imaginary part.
### Querying a quaternion’s properties
- [var angle: Double](./simd_quatd/angle.md)
  The angle, in radians, by which the quaternion’s action rotates.
- [var axis: SIMD3<Double>](./simd_quatd/axis.md)
  The normalized axis about which the quaternion’s action rotates.
- [var conjugate: simd_quatd](./simd_quatd/conjugate.md)
  The conjugate of the quaternion.
- [var imag: SIMD3<Double>](./simd_quatd/imag.md)
  The imaginary part of the quaternion.
- [var real: Double](./simd_quatd/real.md)
  The real part of the quaternion.
- [var inverse: simd_quatd](./simd_quatd/inverse.md)
  The inverse of the quaternion.
- [var length: Double](./simd_quatd/length.md)
  The length of the quaternion.
- [var normalized: simd_quatd](./simd_quatd/normalized.md)
  The unit quaternion of the quaternion.
- [var vector: simd_double4](./simd_quatd/vector.md)
  The underlying vector of the quaternion.
### Creating a quaternion from other data types
- [func simd_quaternion(Double, Double, Double, Double) -> simd_quatd](./simd_quaternion%28_,_,_,_%29-1adm9.md)
  Returns a new quaternion from 4 scalar values.
- [func simd_quaternion(Double, simd_double3) -> simd_quatd](./simd_quaternion%28_,_%29-2jzvc.md)
  Returns a new quaternion from a scalar value and a three-element vector.
- [func simd_quaternion(UnsafePointer<Double>!) -> simd_quatd](./simd_quaternion%28_%29-8kl4p.md)
  Returns a new quaternion from a pointer to scalar values.
- [func simd_quaternion(simd_double3, simd_double3) -> simd_quatd](./simd_quaternion%28_,_%29-2yoqw.md)
  Returns a new quaternion from 2 three-element vectors.
- [func simd_quaternion(simd_double3x3) -> simd_quatd](./simd_quaternion%28_%29-7paor.md)
  Returns a new quaternion from a 3 x 3 matrix.
- [func simd_quaternion(simd_double4) -> simd_quatd](./simd_quaternion%28_%29-459vs.md)
  Returns a new quaternion from a four-element vector.
- [func simd_quaternion(simd_double4x4) -> simd_quatd](./simd_quaternion%28_%29-8e0xf.md)
  Returns a new quaternion from a 4 x 4 matrix.
### Applying arithmetic operations to quaternions
- [func simd_add(simd_quatd, simd_quatd) -> simd_quatd](./simd_add%28_,_%29-6ohmq.md)
  Returns the sum of two quaternions.
- [func simd_mul(simd_quatd, simd_quatd) -> simd_quatd](./simd_mul%28_,_%29-531pe.md)
  Returns the product of two quaternions.
- [func simd_mul(Double, simd_quatd) -> simd_quatd](./simd_mul%28_,_%29-8aedk.md)
- [func simd_mul(simd_quatd, Double) -> simd_quatd](./simd_mul%28_,_%29-8uidm.md)
- [func simd_sub(simd_quatd, simd_quatd) -> simd_quatd](./simd_sub%28_,_%29-87caf.md)
  Returns the difference between two quaternions.
- [func exp(simd_quatd) -> simd_quatd](./exp%28_%29-9nl1f.md)
- [func log(simd_quatd) -> simd_quatd](./log%28_%29-77xdo.md)
### Applying geometric operations to quaternions
- [func simd_act(simd_quatd, simd_double3) -> simd_double3](./simd_act%28_,_%29-47h09.md)
  Returns a vector rotated by a quaternion.
- [func act(SIMD3<Double>) -> SIMD3<Double>](./simd_quatd/act%28_%29.md)
  Returns the specified vector rotated by the quaternion.
- [func simd_angle(simd_quatd) -> Double](./simd_angle%28_%29-zuvx.md)
  Returns the angle by which a quaternion rotates.
- [func simd_axis(simd_quatd) -> simd_double3](./simd_axis%28_%29-56wf4.md)
  Returns the normalized axis about which the action of the specified quaternion rotates.
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
### Inverting a quaternion
- [func simd_inverse(simd_quatd) -> simd_quatd](./simd_inverse%28_%29-3cvvi.md)
  Returns the inverse of a quaternion.
### Providing a hash value
- [func hash(into: inout Hasher)](./simd_quatd/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Operators
- [static func * (simd_quatd, simd_quatd) -> simd_quatd](./simd_quatd/star%28_,_%29-5wd9q.md)
  Multiplies two quaternions and produces their product.
- [static func * (simd_quatd, Double) -> simd_quatd](./simd_quatd/star%28_,_%29-5wtdl.md)
  Multiplies a quaternion and a scalar value, and produces their product.
- [static func * (Double, simd_quatd) -> simd_quatd](./simd_quatd/star%28_,_%29-6yv0o.md)
  Multiplies a scalar value and a quaternion, and produces their product.
- [static func *= (inout simd_quatd, Double)](./simd_quatd/stareq%28_,_%29-66wf4.md)
  Multiplies a quaternion and a scalar value, and stores the result in the left-hand-side variable.
- [static func *= (inout simd_quatd, simd_quatd)](./simd_quatd/stareq%28_,_%29-9rhrs.md)
  Multiplies two quaternions and stores the result in the left-hand-side variable.
- [static func + (simd_quatd, simd_quatd) -> simd_quatd](./simd_quatd/plus%28_,_%29.md)
  Adds two quaternions and produces their sum.
- [static func += (inout simd_quatd, simd_quatd)](./simd_quatd/pluseq%28_,_%29.md)
  Adds two quaternions and stores the result in the left-hand-side variable.
- [static func - (simd_quatd) -> simd_quatd](./simd_quatd/minus%28_%29.md)
  Calculates the additive inverse of a quaternion.
- [static func - (simd_quatd, simd_quatd) -> simd_quatd](./simd_quatd/minus%28_,_%29.md)
  Subtracts one quaternion from another and produces their difference.
- [static func -= (inout simd_quatd, simd_quatd)](./simd_quatd/minuseq%28_,_%29.md)
  Subtracts the second quaternion from the first and stores the difference in the left-hand-side variable.
- [static func / (simd_quatd, Double) -> simd_quatd](./simd_quatd/op%28_,_%29-2ftmo.md)
  Divides a quaternion by a scalar value and produces the quotient.
- [static func / (simd_quatd, simd_quatd) -> simd_quatd](./simd_quatd/op%28_,_%29-dhx4.md)
  Divides the first quaternion by the second and produces the quotient.
- [static func /= (inout simd_quatd, simd_quatd)](./simd_quatd/opeq%28_,_%29-40h2o.md)
  Divides the first quaternion by the second and stores the quotient in the left-hand-side variable.
- [static func /= (inout simd_quatd, Double)](./simd_quatd/opeq%28_,_%29-4w1si.md)
  Divides a quaternion by a scalar value and stores the quotient in the left-hand-side variable.
### Initializers
- [init(Rotation3DFloat)](./simd_quatd/init%28_%29-3wkyg.md)
  Returns a new quaternion from a Spatial rotation.
### Default Implementations
- [Hashable Implementations](./simd_quatd/hashable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Quaternions
- [Working with Quaternions](../Accelerate/working-with-quaternions.md)
  Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](../Accelerate/rotating-a-cube-by-transforming-its-vertices.md)
  Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- [struct simd_quatf](./simd_quatf.md)
  A single-precision quaternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quatd)*