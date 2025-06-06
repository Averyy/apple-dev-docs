# recognizedPoints(_:)

**Framework**: Vision  
**Kind**: method

Returns a collection of points for the group name you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(_ jointsGroupName: VNHumanBodyPose3DObservation.JointsGroupName) throws -> [VNHumanBodyPose3DObservation.JointName : VNHumanBodyRecognizedPoint3D]
```

#### Return Value

A collection of points.

## Parameters

- `jointsGroupName`: The name of the human body joints group.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/recognizedpoints(_:))*