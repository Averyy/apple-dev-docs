# VNAnimalBodyPoseObservation.JointsGroupName

**Framework**: Vision  
**Kind**: struct

The joint group names for an animal body pose.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct JointsGroupName
```

## Topics

### Getting the Group Names
- [static let all: VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname/all.md)
  A group name that represents all joints.
- [static let forelegs: VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname/forelegs.md)
  A group name that represents the forelegs.
- [static let head: VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname/head.md)
  A group name that represents the head.
- [static let hindlegs: VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname/hindlegs.md)
  A group name that represents the hindlegs.
- [static let tail: VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname/tail.md)
  A group name that represents the tail.
- [static let trunk: VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname/trunk.md)
  A group name that represents the trunk.
### Creating a Group Name
- [init(rawValue: VNRecognizedPointGroupKey)](vnanimalbodyposeobservation/jointsgroupname/init(rawvalue:).md)
  Creates a joint name with the key you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](vnanimalbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname.md)
  The joint names for an animal body pose.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](vnanimalbodyposeobservation/availablejointgroupnames.md)
  The available joint group names in the observation.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnanimalbodyposeobservation/recognizedpoint(_:).md)
  Returns the point for a joint name the observation recognizes.
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](vnanimalbodyposeobservation/recognizedpoints(_:).md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/jointsgroupname)*