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
func recognizedPoints(_ jointsGroupName: VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]
```

## Mentions

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)

#### Return Value

The array of points associated with the joint group name.

## Parameters

- `jointsGroupName`: The joint group name of the points to retrieve.

## See Also

- [var availableJointNames: [VNHumanBodyPoseObservation.JointName]](vnhumanbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname.md)
  The supported joint names for the body pose.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](vnhumanbodyposeobservation/availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname.md)
  The supported joint group names for the body pose.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanbodyposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation/recognizedpoints(_:))*