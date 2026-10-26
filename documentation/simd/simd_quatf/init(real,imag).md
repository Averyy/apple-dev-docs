# init(real:imag:)

**Framework**: simd  
**Kind**: init  
**Role**: Initializer

Creates a new quaternion from a scalar real part and a vector imaginary part.

## Declaration

```swift
init(real: Float, imag: SIMD3<Float>)
```

## Parameters

- `real`: A scalar value that specifies the real part of the quaternion.
- `imag`: A three-element vector that specifies the imaginary part of the quaternion.

## See Also

### Initializing a quaternion
- [init()](./init%28%29.md)
  Creates a new quaternion.
- [init(vector: simd_float4)](./init%28vector%29.md)
  Creates a new quaternion from a four-element vector.
- [init(simd_float3x3)](./init%28_%29-1hlsg.md)
  Creates a new quaternion from a 3 x 3 rotation matrix.
- [init(simd_float4x4)](./init%28_%29-3751.md)
  Creates a new quaternion from a 4 x 4 rotation matrix.
- [init(angle: Float, axis: SIMD3<Float>)](./init%28angle,axis%29.md)
  Creates a new quaternion with an action that’s a rotation about an axis.
- [init(from: SIMD3<Float>, to: SIMD3<Float>)](./init%28from,to%29.md)
  Creates a new quaternion with an action that’s a rotation between two vectors.
- [init(ix: Float, iy: Float, iz: Float, r: Float)](./init%28ix,iy,iz,r%29.md)
  Creates a new quaternion from four scalar values that specify the imaginary and real parts.
- [init(Rotation3D)](./init%28_%29-9rvr0.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quatf/init(real:imag:))*