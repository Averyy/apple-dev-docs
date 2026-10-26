# simd_quaternion(_:)

**Framework**: simd  
**Kind**: func  
**Role**: Function

Returns a new quaternion from a 3 x 3 matrix.

## Declaration

```swift
func simd_quaternion(_ matrix: simd_float3x3) -> simd_quatf
```

```c
static simd_quatf simd_quaternion(simd_float3x3 matrix);
```

## See Also

### Creating a quaternion from other data types
- [func simd_quaternion(Float, Float, Float, Float) -> simd_quatf](./simd_quaternion%28_,_,_,_%29-8aad4.md)
  Returns a new quaternion from 4 scalar values.
- [func simd_quaternion(Float, simd_float3) -> simd_quatf](./simd_quaternion%28_,_%29-5lqb.md)
  Returns a new quaternion from a scalar value and a three-element vector.
- [func simd_quaternion(UnsafePointer<Float>!) -> simd_quatf](./simd_quaternion%28_%29-8kkih.md)
  Returns a new quaternion from a pointer to scalar values.
- [func simd_quaternion(simd_float3, simd_float3) -> simd_quatf](./simd_quaternion%28_,_%29-18t47.md)
  Returns a new quaternion from 2 three-element vectors.
- [func simd_quaternion(simd_float4) -> simd_quatf](./simd_quaternion%28_%29-459a0.md)
  Returns a new quaternion from a four-element vector.
- [func simd_quaternion(simd_float4x4) -> simd_quatf](./simd_quaternion%28_%29-69ido.md)
  Returns a new quaternion from a 4 x 4 matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quaternion(_:)-2qm7k)*