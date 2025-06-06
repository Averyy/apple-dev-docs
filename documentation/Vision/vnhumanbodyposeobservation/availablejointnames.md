# availableJointNames

**Framework**: Vision  
**Kind**: property

The names of the available joints in the observation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var availableJointNames: [VNHumanBodyPoseObservation.JointName] { get }
```

## See Also

- [VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname.md)
  The supported joint names for the body pose.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](vnhumanbodyposeobservation/availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname.md)
  The supported joint group names for the body pose.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanbodyposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]](vnhumanbodyposeobservation/recognizedpoints(_:).md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation/availablejointnames)*