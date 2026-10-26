# simd_quaternion(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new quaternion from a pointer to scalar values.

## Declaration

```swift
func simd_quaternion(_ xyzr: UnsafePointer<Double>!) -> simd_quatd
```

```c
static simd_quatd simd_quaternion(const double xyzr[4]);
```

## See Also

### Creating a quaternion from other data types
- [func simd_quaternion(Double, Double, Double, Double) -> simd_quatd](./simd_quaternion%28_,_,_,_%29-1adm9.md)
  Returns a new quaternion from 4 scalar values.
- [func simd_quaternion(Double, simd_double3) -> simd_quatd](./simd_quaternion%28_,_%29-2jzvc.md)
  Returns a new quaternion from a scalar value and a three-element vector.
- [func simd_quaternion(simd_double3, simd_double3) -> simd_quatd](./simd_quaternion%28_,_%29-2yoqw.md)
  Returns a new quaternion from 2 three-element vectors.
- [func simd_quaternion(simd_double3x3) -> simd_quatd](./simd_quaternion%28_%29-7paor.md)
  Returns a new quaternion from a 3 x 3 matrix.
- [func simd_quaternion(simd_double4) -> simd_quatd](./simd_quaternion%28_%29-459vs.md)
  Returns a new quaternion from a four-element vector.
- [func simd_quaternion(simd_double4x4) -> simd_quatd](./simd_quaternion%28_%29-8e0xf.md)
  Returns a new quaternion from a 4 x 4 matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quaternion(_:)-8kl4p)*