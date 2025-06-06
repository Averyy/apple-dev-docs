# recognizedPoints(_:)

**Framework**: Vision  
**Kind**: method

Returns the points for a joint group name the observation recognizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(_ jointsGroupName: VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]
```

#### Return Value

The dictionary of points the observation associates with the group name.

## Parameters

- `jointsGroupName`: The joint group of the points to retrieve.

## See Also

- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](vnanimalbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname.md)
  The joint names for an animal body pose.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](vnanimalbodyposeobservation/availablejointgroupnames.md)
  The available joint group names in the observation.
- [VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname.md)
  The joint group names for an animal body pose.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnanimalbodyposeobservation/recognizedpoint(_:).md)
  Returns the point for a joint name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/recognizedpoints(_:))*