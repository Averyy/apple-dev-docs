# Fx3DAPI_v5

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An API that defines the methods the host application provides to get information about the 3D environment, including camera and object transforms.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
protocol Fx3DAPI_v5
```

```objc
@protocol Fx3DAPI_v5
```

## Topics

### Accessing the 3D Environment
- [func focalLength(at: CMTime, error: NSErrorPointer) -> Double](./fx3dapi_v5/focallength%28at,error%29.md)
  Gets the focal length.
- [func layerMatrix(at: CMTime) throws -> FxMatrix44](./fx3dapi_v5/layermatrix%28at%29.md)
  Gets the 4x4 layer matrix, which is equivalent to the model matrix for the object that the effect is applied to.
- [func viewMatrix(at: CMTime) throws -> FxMatrix44](./fx3dapi_v5/viewmatrix%28at%29.md)
  Gets the 4x4 view matrix.
- [func metalProjectionMatrix(at: CMTime) throws -> FxMatrix44](./fx3dapi_v5/metalprojectionmatrix%28at%29.md)
  Gets the 4x4 Metal projection matrix.
- [func frustumLeft(UnsafeMutablePointer<Double>!, right: UnsafeMutablePointer<Double>!, bottom: UnsafeMutablePointer<Double>!, top: UnsafeMutablePointer<Double>!, near: UnsafeMutablePointer<Double>!, far: UnsafeMutablePointer<Double>!, at: CMTime) throws](./fx3dapi_v5/frustumleft%28_,right,bottom,top,near,far,at%29.md)
  Describes the bounds of the viewing solid for generating a projection matrix.

## See Also

### 3D and lighting
- [protocol FxLightingAPI_v3](./fxlightingapi_v3.md)
  An API you use to get information about lights in a scene in a Motion project.
- [class FxMatrix44](./fxmatrix44.md)
  The `FxMatrix` class encapsulates a 4x4 matrix object and provides matrix inversion and transforming of 2D and 3D points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fx3dapi_v5)*