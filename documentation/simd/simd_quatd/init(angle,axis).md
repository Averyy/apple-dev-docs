# init(angle:axis:)

**Framework**: simd  
**Kind**: init  
**Role**: Initializer

Creates a new quaternion with an action that’s a rotation about an axis.

## Declaration

```swift
init(angle: Double, axis: SIMD3<Double>)
```

## Parameters

- `angle`: The rotation angle in radians.
- `axis`: A three-element vector that specifies the rotation axis.

## See Also

### Initializing a quaternion
- [init()](./init%28%29.md)
  Creates a new quaternion.
- [init(vector: simd_double4)](./init%28vector%29.md)
  Creates a new quaternion from a four-element vector.
- [init(simd_double3x3)](./init%28_%29-791zk.md)
  Creates a new quaternion from a 3 x 3 rotation matrix.
- [init(simd_double4x4)](./init%28_%29-5vcd5.md)
  Creates a new quaternion from a 4 x 4 rotation matrix.
- [init(from: SIMD3<Double>, to: SIMD3<Double>)](./init%28from,to%29.md)
  Creates a new quaternion with an action that’s a rotation between two vectors.
- [init(ix: Double, iy: Double, iz: Double, r: Double)](./init%28ix,iy,iz,r%29.md)
  Creates a new quaternion from four scalar values that specify the imaginary and real parts.
- [init(real: Double, imag: SIMD3<Double>)](./init%28real,imag%29.md)
  Creates a new quaternion from a scalar real part and a vector imaginary part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/simd/simd_quatd/init(angle:axis:))*