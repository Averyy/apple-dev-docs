# VNAnimalBodyPoseObservation

**Framework**: Vision  
**Kind**: class

An observation that provides the animal body points the analysis recognizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNAnimalBodyPoseObservation
```

## Topics

### Accessing Points
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
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](vnanimalbodyposeobservation/recognizedpoints(_:).md)
  Returns the points for a joint group name the observation recognizes.

## Relationships

### Inherits From
- [VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Detecting animal body poses with Vision](detecting-animal-body-poses-with-vision.md)
  Draw the skeleton of an animal by using Vision’s capability to detect animal body poses.
- [class VNDetectAnimalBodyPoseRequest](vndetectanimalbodyposerequest.md)
  A request that detects an animal body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation)*