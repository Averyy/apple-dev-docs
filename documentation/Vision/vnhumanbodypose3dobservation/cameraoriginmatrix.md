# cameraOriginMatrix

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A transform from the skeleton hip to the camera.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var cameraOriginMatrix: simd_float4x4 { get }
```

```objc
@property (nonatomic, readonly) simd_float4x4 cameraOriginMatrix;
```

## Mentions

- [Identifying 3D human body poses in images](../identifying-3d-human-body-poses-in-images.md)

## See Also

### Getting the Camera Position
- [func cameraRelativePosition(VNHumanBodyPose3DObservation.JointName) throws -> simd_float4x4](./camerarelativeposition%28_%29.md)
  Returns a position relative to the camera for the body joint you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/cameraoriginmatrix)*