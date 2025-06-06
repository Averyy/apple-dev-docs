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
var availableJointNames: [VNHumanHandPoseObservation.JointName] { get }
```

## See Also

- [VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname.md)
  The supported joint names for the hand pose.
- [var availableJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](vnhumanhandposeobservation/availablejointsgroupnames.md)
  The joint group names available in the observation.
- [VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname.md)
  The supported joint group names for the hand pose.
- [func recognizedPoint(VNHumanHandPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanhandposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanHandPoseObservation.JointsGroupName) throws -> [VNHumanHandPoseObservation.JointName : VNRecognizedPoint]](vnhumanhandposeobservation/recognizedpoints(_:).md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanhandposeobservation/availablejointnames)*