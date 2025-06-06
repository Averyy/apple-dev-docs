# availableJointsGroupNames

**Framework**: Vision  
**Kind**: property

The available joint group names in the observation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var availableJointsGroupNames: [VNHumanBodyPose3DObservation.JointsGroupName] { get }
```

## See Also

- [var availableJointNames: [VNHumanBodyPose3DObservation.JointName]](vnhumanbodypose3dobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPose3DObservation.JointName](vnhumanbodypose3dobservation/jointname.md)
  The joint names for a 3D body pose.
- [VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname.md)
  The joint group names for a 3D body pose.
- [func recognizedPoint(VNHumanBodyPose3DObservation.JointName) throws -> VNHumanBodyRecognizedPoint3D](vnhumanbodypose3dobservation/recognizedpoint(_:).md)
  Returns the point for a joint name that the observation recognizes.
- [func recognizedPoints(VNHumanBodyPose3DObservation.JointsGroupName) throws -> [VNHumanBodyPose3DObservation.JointName : VNHumanBodyRecognizedPoint3D]](vnhumanbodypose3dobservation/recognizedpoints(_:).md)
  Returns a collection of points for the group name you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/availablejointsgroupnames)*