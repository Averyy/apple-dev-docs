# recognizedPoint(_:)

**Framework**: Vision  
**Kind**: method

Returns the point for a joint name that the observation recognizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoint(_ jointName: VNHumanBodyPose3DObservation.JointName) throws -> VNHumanBodyRecognizedPoint3D
```

#### Return Value

The point for the joint name.

## Parameters

- `jointName`: The joint name to retrieve.

## See Also

- [var availableJointNames: [VNHumanBodyPose3DObservation.JointName]](vnhumanbodypose3dobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPose3DObservation.JointName](vnhumanbodypose3dobservation/jointname.md)
  The joint names for a 3D body pose.
- [var availableJointsGroupNames: [VNHumanBodyPose3DObservation.JointsGroupName]](vnhumanbodypose3dobservation/availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname.md)
  The joint group names for a 3D body pose.
- [func recognizedPoints(VNHumanBodyPose3DObservation.JointsGroupName) throws -> [VNHumanBodyPose3DObservation.JointName : VNHumanBodyRecognizedPoint3D]](vnhumanbodypose3dobservation/recognizedpoints(_:).md)
  Returns a collection of points for the group name you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/recognizedpoint(_:))*