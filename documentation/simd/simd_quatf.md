# simd_quatf

**Framework**: simd  
**Kind**: struct  
**Role**: Structure

A single-precision quaternion.

## Declaration

```swift
struct simd_quatf
```

```c
typedef struct { ... } simd_quatf;
```

## Topics

### Initializing a quaternion
- [init()](./simd_quatf/init%28%29.md)
  Creates a new quaternion.
- [init(vector: simd_float4)](./simd_quatf/init%28vector%29.md)
  Creates a new quaternion from a four-element vector.
- [init(simd_float3x3)](./simd_quatf/init%28_%29-1hlsg.md)
  Creates a new quaternion from a 3 x 3 rotation matrix.
- [init(simd_float4x4)](./simd_quatf/init%28_%29-3751.md)
  Creates a new quaternion from a 4 x 4 rotation matrix.
- [init(angle: Float, axis: SIMD3<Float>)](./simd_quatf/init%28angle,axis%29.md)
  Creates a new quaternion with an action that’s a rotation about an axis.
- [init(from: SIMD3<Float>, to: SIMD3<Float>)](./simd_quatf/init%28from,to%29.md)
  Creates a new quaternion with an action that’s a rotation between two vectors.
- [init(ix: Float, iy: Float, iz: Float, r: Float)](./simd_quatf/init%28ix,iy,iz,r%29.md)
  Creates a new quaternion from four scalar values that specify the imaginary and real parts.
- [init(real: Float, imag: SIMD3<Float>)](./simd_quatf/init%28real,imag%29.md)
  Creates a new quaternion from a scalar real part and a vector imaginary part.
- [init(Rotation3D)](./simd_quatf/init%28_%29-9rvr0.md)
### Querying a quaternion’s properties
- [var angle: Float](./simd_quatf/angle.md)
  The angle, in radians, by which the quaternion’s action rotates.
- [var axis: SIMD3<Float>](./simd_quatf/axis.md)
  The normalized axis about which the quaternion’s action rotates.
- [var conjugate: simd_quatf](./simd_quatf/conjugate.md)
  The conjugate of the quaternion.
- [var imag: SIMD3<Float>](./simd_quatf/imag.md)
  The imaginary part of the quaternion.
- [var real: Float](./simd_quatf/real.md)
  The real part of the quaternion.
- [var inverse: simd_quatf](./simd_quatf/inverse.md)
  The inverse of the quaternion.
- [var length: Float](./simd_quatf/length.md)
  The length of the quaternion.
- [var normalized: simd_quatf](./simd_quatf/normalized.md)
  The unit quaternion of the quaternion.
- [var vector: simd_float4](./simd_quatf/vector.md)
  The underlying vector of the quaternion.
### Creating a quaternion from other data types
- [func simd_quaternion(Float, Float, Float, Float) -> simd_quatf](./simd_quaternion%28_,_,_,_%29-8aad4.md)
  Returns a new quaternion from 4 scalar values.
- [func simd_quaternion(Float, simd_float3) -> simd_quatf](./simd_quaternion%28_,_%29-5lqb.md)
  Returns a new quaternion from a scalar value and a three-element vector.
- [func simd_quaternion(UnsafePointer<Float>!) -> simd_quatf](./simd_quaternion%28_%29-8kkih.md)
  Returns a new quaternion from a pointer to scalar values.
- [func simd_quaternion(simd_float3, simd_float3) -> simd_quatf](./simd_quaternion%28_,_%29-18t47.md)
  Returns a new quaternion from 2 three-element vectors.
- [func simd_quaternion(simd_float3x3) -> simd_quatf](./simd_quaternion%28_%29-2qm7k.md)
  Returns a new quaternion from a 3 x 3 matrix.
- [func simd_quaternion(simd_float4) -> simd_quatf](./simd_quaternion%28_%29-459a0.md)
  Returns a new quaternion from a four-element vector.
- [func simd_quaternion(simd_float4x4) -> simd_quatf](./simd_quaternion%28_%29-69ido.md)
  Returns a new quaternion from a 4 x 4 matrix.
### Applying arithmetic operations to quaternions
- [func simd_add(simd_quatf, simd_quatf) -> simd_quatf](./simd_add%28_,_%29-7641g.md)
  Returns the sum of two quaternions.
- [func simd_mul(simd_quatf, simd_quatf) -> simd_quatf](./simd_mul%28_,_%29-4a5hq.md)
  Returns the product of two quaternions.
- [func simd_mul(Float, simd_quatf) -> simd_quatf](./simd_mul%28_,_%29-391wq.md)
- [func simd_mul(simd_quatf, Float) -> simd_quatf](./simd_mul%28_,_%29-bqqq.md)
- [func simd_sub(simd_quatf, simd_quatf) -> simd_quatf](./simd_sub%28_,_%29-807rv.md)
  Returns the difference between two quaternions.
- [func exp(simd_quatf) -> simd_quatf](./exp%28_%29-9q8na.md)
- [func log(simd_quatf) -> simd_quatf](./log%28_%29-xpx0.md)
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
- [func dot(simd_quatf, simd_quatf) -> Float](./dot%28_,_%29-2en8e.md)
- [func simd_length(simd_quatf) -> Float](./simd_length%28_%29-52nf5.md)
  Returns the length of a quaternion.
- [func simd_normalize(simd_quatf) -> simd_quatf](./simd_normalize%28_%29-uch9.md)
  Returns a quaternion pointing in the same direction as the supplied quaternion with a length of 1.
### Inverting a quaternion
- [func simd_inverse(simd_quatf) -> simd_quatf](./simd_inverse%28_%29-3cvay.md)
  Returns the inverse of a quaternion.
### Providing a hash value
- [func hash(into: inout Hasher)](./simd_quatf/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Deprecated symbols
- [init(rotation: Rotation3D)](./simd_quatf/init%28rotation%29.md)
  Created a new quaternion from a Spatial rotation structure.
### Operators
- [static func * (simd_quatf, Float) -> simd_quatf](./simd_quatf/star%28_,_%29-48x.md)
  Multiplies a quaternion and a scalar value, and produces their product.
- [static func * (Float, simd_quatf) -> simd_quatf](./simd_quatf/star%28_,_%29-9tia3.md)
  Multiplies a scalar value and a quaternion, and produces their product.
- [static func * (simd_quatf, simd_quatf) -> simd_quatf](./simd_quatf/star%28_,_%29-v1lb.md)
  Multiplies two quaternions and produces their product.
- [static func *= (inout simd_quatf, Float)](./simd_quatf/stareq%28_,_%29-51ee0.md)
  Multiplies two quaternions and stores the result in the left-hand-side variable.
- [static func *= (inout simd_quatf, simd_quatf)](./simd_quatf/stareq%28_,_%29-pcoc.md)
  Multiplies a quaternion and a scalar value, and stores the result in the left-hand-side variable.
- [static func + (simd_quatf, simd_quatf) -> simd_quatf](./simd_quatf/plus%28_,_%29.md)
  Adds two quaternions and produces their sum.
- [static func += (inout simd_quatf, simd_quatf)](./simd_quatf/pluseq%28_,_%29.md)
  Adds two quaternions and stores the result in the left-hand-side variable.
- [static func - (simd_quatf) -> simd_quatf](./simd_quatf/minus%28_%29.md)
  Calculates the additive inverse of a quaternion.
- [static func - (simd_quatf, simd_quatf) -> simd_quatf](./simd_quatf/minus%28_,_%29.md)
  Subtracts one quaternion from another and produces their difference.
- [static func -= (inout simd_quatf, simd_quatf)](./simd_quatf/minuseq%28_,_%29.md)
  Subtracts the second quaternion from the first and stores the difference in the left-hand-side variable.
- [static func / (simd_quatf, simd_quatf) -> simd_quatf](./simd_quatf/op%28_,_%29-15qds.md)
  Divides the first quaternion by the second and produces the quotient.
- [static func / (simd_quatf, Float) -> simd_quatf](./simd_quatf/op%28_,_%29-1ba81.md)
  Divides a quaternion by a scalar value and produces the quotient.
- [static func /= (inout simd_quatf, Float)](./simd_quatf/opeq%28_,_%29-2qypk.md)
  Divides a quaternion by a scalar value and stores the quotient in the left-hand-side variable.
- [static func /= (inout simd_quatf, simd_quatf)](./simd_quatf/opeq%28_,_%29-5tm7m.md)
  Divides the first quaternion by the second and stores the quotient in the left-hand-side variable.
### Default Implementations
- [Hashable Implementations](./simd_quatf/hashable-implementations.md)

## Relationships

### Conforms To
- [AnimatableData](../RealityKit/animatabledata.md)
- [BindableData](../RealityKit/bindabledata.md)
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
- [struct simd_quatd](./simd_quatd.md)
  A double-precision quaternion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quatf)*