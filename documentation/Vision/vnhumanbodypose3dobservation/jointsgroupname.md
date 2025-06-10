# VNHumanBodyPose3DObservation.JointsGroupName

**Framework**: Vision  
**Kind**: struct

The joint group names for a 3D body pose.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct JointsGroupName
```

## Topics

### Getting the Group Names
- [static let all: VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname/all.md)
  A group name that represents all joints.
- [static let head: VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname/head.md)
  A group name that represents the head joints.
- [static let leftArm: VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname/leftarm.md)
  A group name that represents the left arm joints.
- [static let leftLeg: VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname/leftleg.md)
  A group name that represents the left leg joints.
- [static let rightArm: VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname/rightarm.md)
  A group name that represents the right arm joints.
- [static let rightLeg: VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname/rightleg.md)
  A group name that represents the right leg joints.
- [static let torso: VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname/torso.md)
  A group name that represents the torso joints.
### Creating a Group Name
- [init(rawValue: VNRecognizedPointGroupKey)](vnhumanbodypose3dobservation/jointsgroupname/init(rawvalue:).md)
  Creates a joint name with the key you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)
  Detect three-dimensional human body poses using the Vision framework.
- [Detecting human body poses in 3D with Vision](detecting-human-body-poses-in-3d-with-vision.md)
  Render skeletons of 3D body pose points in a scene overlaying the input image.
- [class VNDetectHumanBodyPose3DRequest](vndetecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.
- [class VNHumanBodyPose3DObservation](vnhumanbodypose3dobservation.md)
  An observation that provides the 3D body points the request recognizes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/jointsgroupname)*