# getCameraRelativePosition:forJointName:error:

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Gets a position relative to the camera for the body joint you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (BOOL) getCameraRelativePosition:(simd_float4x4 *) modelPositionOut forJointName:(VNHumanBodyPose3DObservationJointName) jointName error:(NSError **) error;
```

#### Return Value

A Boolean value that indicates the success of determining the position.

## Parameters

- `modelPositionOut`: The reference to the position.
- `jointName`: The name of the humany body joint.
- `error`: If an error occurs, an error object that describes the error; otherwise, `nil`.

## See Also

### Getting the Camera Position
- [var cameraOriginMatrix: simd_float4x4](./cameraoriginmatrix.md)
  A transform from the skeleton hip to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/getcamerarelativeposition:forjointname:error:)*