# focalLength(at:error:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the focal length.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func focalLength(at time: CMTime, error: NSErrorPointer) -> Double
```

```objc
- (double) focalLengthAtTime:(CMTime) time error:(NSError * *) error;
```

## Return Value

The value of the focal length.

## Parameters

- `time`: Specified time, expressed as a [`CMTime`](../../CoreMedia/cmtime.md), to retrieve the matrix value.
- `error`: Description of the problem if you are unable to retrieve the value.

## See Also

### Accessing the 3D Environment
- [func layerMatrix(at: CMTime) throws -> FxMatrix44](./layermatrix%28at%29.md)
  Gets the 4x4 layer matrix, which is equivalent to the model matrix for the object that the effect is applied to.
- [func viewMatrix(at: CMTime) throws -> FxMatrix44](./viewmatrix%28at%29.md)
  Gets the 4x4 view matrix.
- [func metalProjectionMatrix(at: CMTime) throws -> FxMatrix44](./metalprojectionmatrix%28at%29.md)
  Gets the 4x4 Metal projection matrix.
- [func frustumLeft(UnsafeMutablePointer<Double>!, right: UnsafeMutablePointer<Double>!, bottom: UnsafeMutablePointer<Double>!, top: UnsafeMutablePointer<Double>!, near: UnsafeMutablePointer<Double>!, far: UnsafeMutablePointer<Double>!, at: CMTime) throws](./frustumleft%28_,right,bottom,top,near,far,at%29.md)
  Describes the bounds of the viewing solid for generating a projection matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fx3dapi_v5/focallength(at:error:))*