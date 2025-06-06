# recognizedPoints(_:)

**Framework**: Vision  
**Kind**: method

Retrieves the recognized points associated with the joint group name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(_ jointsGroupName: VNHumanHandPoseObservation.JointsGroupName) throws -> [VNHumanHandPoseObservation.JointName : VNRecognizedPoint]
```

#### Return Value

The array of points associated with the joint group name.

## Parameters

- `jointsGroupName`: The joint group name of the points to retrieve.

## See Also

- [var availableJointNames: [VNHumanHandPoseObservation.JointName]](vnhumanhandposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname.md)
  The supported joint names for the hand pose.
- [var availableJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](vnhumanhandposeobservation/availablejointsgroupnames.md)
  The joint group names available in the observation.
- [VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname.md)
  The supported joint group names for the hand pose.
- [func recognizedPoint(VNHumanHandPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanhandposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanhandposeobservation/recognizedpoints(_:))*