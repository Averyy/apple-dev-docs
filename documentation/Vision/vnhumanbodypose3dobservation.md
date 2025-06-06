# VNHumanBodyPose3DObservation

**Framework**: Vision  
**Kind**: class

An observation that provides the 3D body points the request recognizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNHumanBodyPose3DObservation
```

## Mentions

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)

## Topics

### Accessing Points
- [var availableJointNames: [VNHumanBodyPose3DObservation.JointName]](vnhumanbodypose3dobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPose3DObservation.JointName](vnhumanbodypose3dobservation/jointname.md)
  The joint names for a 3D body pose.
- [var availableJointsGroupNames: [VNHumanBodyPose3DObservation.JointsGroupName]](vnhumanbodypose3dobservation/availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname.md)
  The joint group names for a 3D body pose.
- [func recognizedPoint(VNHumanBodyPose3DObservation.JointName) throws -> VNHumanBodyRecognizedPoint3D](vnhumanbodypose3dobservation/recognizedpoint(_:).md)
  Returns the point for a joint name that the observation recognizes.
- [func recognizedPoints(VNHumanBodyPose3DObservation.JointsGroupName) throws -> [VNHumanBodyPose3DObservation.JointName : VNHumanBodyRecognizedPoint3D]](vnhumanbodypose3dobservation/recognizedpoints(_:).md)
  Returns a collection of points for the group name you specify.
### Getting the Joint Position
- [func pointInImage(VNHumanBodyPose3DObservation.JointName) throws -> VNPoint](vnhumanbodypose3dobservation/pointinimage(_:).md)
  Returns a 2D point for the joint name you specify, relative to the input image.
### Getting the Parent Joint Name
- [func parentJointName(VNHumanBodyPose3DObservation.JointName) -> VNHumanBodyPose3DObservation.JointName?](vnhumanbodypose3dobservation/parentjointname(_:).md)
  Returns the parent joint of the joint name you specify.
### Getting the Body Height
- [var heightEstimation: VNHumanBodyPose3DObservation.HeightEstimation](vnhumanbodypose3dobservation/heightestimation-swift.property.md)
  The technique the framework uses to estimate body height.
- [VNHumanBodyPose3DObservation.HeightEstimation](vnhumanbodypose3dobservation/heightestimation-swift.enum.md)
  Constants that identify body height estimation techniques.
- [var bodyHeight: Float](vnhumanbodypose3dobservation/bodyheight.md)
  The estimated human body height, in meters.
### Getting the Camera Position
- [var cameraOriginMatrix: simd_float4x4](vnhumanbodypose3dobservation/cameraoriginmatrix.md)
  A transform from the skeleton hip to the camera.
- [func cameraRelativePosition(VNHumanBodyPose3DObservation.JointName) throws -> simd_float4x4](vnhumanbodypose3dobservation/camerarelativeposition(_:).md)
  Returns a position relative to the camera for the body joint you specify.

## Relationships

### Inherits From
- [VNRecognizedPoints3DObservation](vnrecognizedpoints3dobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)
  Detect three-dimensional human body poses using the Vision framework.
- [Detecting human body poses in 3D with Vision](detecting-human-body-poses-in-3d-with-vision.md)
  Render skeletons of 3D body pose points in a scene overlaying the input image.
- [class VNDetectHumanBodyPose3DRequest](vndetecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.
- [class VNRecognizedPoints3DObservation](vnrecognizedpoints3dobservation.md)
  An observation that provides the 3D points for a request.
- [class VNHumanBodyRecognizedPoint3D](vnhumanbodyrecognizedpoint3d.md)
  A recognized 3D point that includes a parent joint.
- [class VNPoint3D](vnpoint3d.md)
  An object that represents a 3D point in an image.
- [class VNRecognizedPoint3D](vnrecognizedpoint3d.md)
  A 3D point that includes an identifier to the point.
- [VNHumanBodyPose3DObservation.JointName](vnhumanbodypose3dobservation/jointname.md)
  The joint names for a 3D body pose.
- [VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname.md)
  The joint group names for a 3D body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation)*