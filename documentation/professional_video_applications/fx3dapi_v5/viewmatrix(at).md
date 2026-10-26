# viewMatrix(at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the 4x4 view matrix.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func viewMatrix(at time: CMTime) throws -> FxMatrix44
```

```objc
- (FxMatrix44 *) viewMatrixAtTime:(CMTime) time error:(NSError * *) error;
```

#### Return Value

An FxMatrix44 containing the matrix.

## Parameters

- `time`: Specified time, expressed as a CMTime, to retrieve the matrix.

## See Also

### Accessing the 3D Environment
- [func focalLength(at: CMTime, error: NSErrorPointer) -> Double](./focallength%28at,error%29.md)
  Gets the focal length.
- [func layerMatrix(at: CMTime) throws -> FxMatrix44](./layermatrix%28at%29.md)
  Gets the 4x4 layer matrix, which is equivalent to the model matrix for the object that the effect is applied to.
- [func metalProjectionMatrix(at: CMTime) throws -> FxMatrix44](./metalprojectionmatrix%28at%29.md)
  Gets the 4x4 Metal projection matrix.
- [func frustumLeft(UnsafeMutablePointer<Double>!, right: UnsafeMutablePointer<Double>!, bottom: UnsafeMutablePointer<Double>!, top: UnsafeMutablePointer<Double>!, near: UnsafeMutablePointer<Double>!, far: UnsafeMutablePointer<Double>!, at: CMTime) throws](./frustumleft%28_,right,bottom,top,near,far,at%29.md)
  Describes the bounds of the viewing solid for generating a projection matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fx3dapi_v5/viewmatrix(at:))*