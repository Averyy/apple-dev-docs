# VNAnimalBodyPoseObservation.JointsGroupName

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

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

```c
typedef VNRecognizedPointGroupKey VNAnimalBodyPoseObservationJointsGroupName;
```

## Topics

### Getting the Group Names
- [static let all: VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname/all.md)
  A group name that represents all joints.
- [static let forelegs: VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname/forelegs.md)
  A group name that represents the forelegs.
- [static let head: VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname/head.md)
  A group name that represents the head.
- [static let hindlegs: VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname/hindlegs.md)
  A group name that represents the hindlegs.
- [static let tail: VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname/tail.md)
  A group name that represents the tail.
- [static let trunk: VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname/trunk.md)
  A group name that represents the trunk.
### Creating a Group Name
- [init(rawValue: VNRecognizedPointGroupKey)](./jointsgroupname/init%28rawvalue%29.md)
  Creates a joint name with the key you specify.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Points
- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNAnimalBodyPoseObservation.JointName](./jointname.md)
  The joint names for an animal body pose.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](./availablejointgroupnames.md)
  The available joint group names in the observation.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Returns the point for a joint name the observation recognizes.
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/jointsgroupname)*