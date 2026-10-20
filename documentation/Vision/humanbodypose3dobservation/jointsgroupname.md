# HumanBodyPose3DObservation.JointsGroupName

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

The supported joint group names for the body pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum JointsGroupName
```

## Topics

### Getting the group names
- [HumanBodyPose3DObservation.JointsGroupName.head](./jointsgroupname/head.md)
- [HumanBodyPose3DObservation.JointsGroupName.leftArm](./jointsgroupname/leftarm.md)
- [HumanBodyPose3DObservation.JointsGroupName.leftLeg](./jointsgroupname/leftleg.md)
- [HumanBodyPose3DObservation.JointsGroupName.rightArm](./jointsgroupname/rightarm.md)
- [HumanBodyPose3DObservation.JointsGroupName.rightLeg](./jointsgroupname/rightleg.md)
- [HumanBodyPose3DObservation.JointsGroupName.torso](./jointsgroupname/torso.md)

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the joints
- [func allJoints(in: HumanBodyPose3DObservation.JointsGroupName?) -> [HumanBodyPose3DObservation.JointName : Joint3D]](./alljoints%28in%29.md)
  Retrieves a dictionary of all joints in a joint group.
- [var availableJointsGroupNames: [HumanBodyPose3DObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The names of the available joint groupings in the observation.
- [func joint(for: HumanBodyPose3DObservation.JointName) -> Joint3D?](./joint%28for%29.md)
  Retrieves a joint for a given joint name.
- [var availableJointNames: [HumanBodyPose3DObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [HumanBodyPose3DObservation.JointName](./jointname.md)
  The supported joint names for the body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/jointsgroupname)*