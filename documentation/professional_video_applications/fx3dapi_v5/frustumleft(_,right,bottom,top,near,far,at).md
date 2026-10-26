# frustumLeft(_:right:bottom:top:near:far:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Describes the bounds of the viewing solid for generating a projection matrix.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func frustumLeft(_ left: UnsafeMutablePointer<Double>!, right: UnsafeMutablePointer<Double>!, bottom: UnsafeMutablePointer<Double>!, top: UnsafeMutablePointer<Double>!, near: UnsafeMutablePointer<Double>!, far: UnsafeMutablePointer<Double>!, at time: CMTime) throws
```

```objc
- (BOOL) frustumLeft:(double *) left right:(double *) right bottom:(double *) bottom top:(double *) top near:(double *) near far:(double *) far atTime:(CMTime) time error:(NSError * *) error;
```

## Parameters

- `left`: The x coordinate for the left vertical clipping plane.
- `right`: The x coordinate for the right vertical clipping plane.
- `bottom`: The y coordinate for the bottom horizontal clipping plane.
- `top`: The y coordinate for the top horizontal clipping plane.
- `near`: The z distance to the near depth clipping plane. Value must be positive.
- `far`: The z distance to the far depth clipping plane. Value must be positive.
- `time`: Specified time, expressed as a CMTime, to retrieve the matrix.

## See Also

### Accessing the 3D Environment
- [func focalLength(at: CMTime, error: NSErrorPointer) -> Double](./focallength%28at,error%29.md)
  Gets the focal length.
- [func layerMatrix(at: CMTime) throws -> FxMatrix44](./layermatrix%28at%29.md)
  Gets the 4x4 layer matrix, which is equivalent to the model matrix for the object that the effect is applied to.
- [func viewMatrix(at: CMTime) throws -> FxMatrix44](./viewmatrix%28at%29.md)
  Gets the 4x4 view matrix.
- [func metalProjectionMatrix(at: CMTime) throws -> FxMatrix44](./metalprojectionmatrix%28at%29.md)
  Gets the 4x4 Metal projection matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fx3dapi_v5/frustumleft(_:right:bottom:top:near:far:at:))*