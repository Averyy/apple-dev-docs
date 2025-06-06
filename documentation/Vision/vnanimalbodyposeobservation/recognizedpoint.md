# recognizedPoint(_:)

**Framework**: Vision  
**Kind**: method

Returns the point for a joint name the observation recognizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoint(_ jointName: VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint
```

#### Return Value

The point for the joint name.

## Parameters

- `jointName`: The joint name to retrieve.

## See Also

- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](vnanimalbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname.md)
  The joint names for an animal body pose.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](vnanimalbodyposeobservation/availablejointgroupnames.md)
  The available joint group names in the observation.
- [VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname.md)
  The joint group names for an animal body pose.
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](vnanimalbodyposeobservation/recognizedpoints(_:).md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/recognizedpoint(_:))*