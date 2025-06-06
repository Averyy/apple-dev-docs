# cameraRelativePosition(_:)

**Framework**: Vision  
**Kind**: method

Returns a position relative to the camera for the body joint you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@nonobjc
func cameraRelativePosition(_ jointName: VNHumanBodyPose3DObservation.JointName) throws -> simd_float4x4
```

## Mentions

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)

#### Return Value

The joint position, in meters.

## Parameters

- `jointName`: The name of the human body joint.

## See Also

- [var cameraOriginMatrix: simd_float4x4](vnhumanbodypose3dobservation/cameraoriginmatrix.md)
  A transform from the skeleton hip to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/camerarelativeposition(_:))*