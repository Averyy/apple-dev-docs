# availableJointNames

**Framework**: Vision  
**Kind**: property

The names of the available joints in the observation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var availableJointNames: [VNAnimalBodyPoseObservation.JointName] { get }
```

## See Also

- [VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname.md)
  The joint names for an animal body pose.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](vnanimalbodyposeobservation/availablejointgroupnames.md)
  The available joint group names in the observation.
- [VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname.md)
  The joint group names for an animal body pose.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnanimalbodyposeobservation/recognizedpoint(_:).md)
  Returns the point for a joint name the observation recognizes.
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](vnanimalbodyposeobservation/recognizedpoints(_:).md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/availablejointnames)*