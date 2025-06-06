# HumanBodyPose3DObservation.JointsGroupName

**Framework**: Vision  
**Kind**: enum

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
- [HumanBodyPose3DObservation.JointsGroupName.head](humanbodypose3dobservation/jointsgroupname/head.md)
- [HumanBodyPose3DObservation.JointsGroupName.leftArm](humanbodypose3dobservation/jointsgroupname/leftarm.md)
- [HumanBodyPose3DObservation.JointsGroupName.leftLeg](humanbodypose3dobservation/jointsgroupname/leftleg.md)
- [HumanBodyPose3DObservation.JointsGroupName.rightArm](humanbodypose3dobservation/jointsgroupname/rightarm.md)
- [HumanBodyPose3DObservation.JointsGroupName.rightLeg](humanbodypose3dobservation/jointsgroupname/rightleg.md)
- [HumanBodyPose3DObservation.JointsGroupName.torso](humanbodypose3dobservation/jointsgroupname/torso.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func allJoints(in: HumanBodyPose3DObservation.JointsGroupName?) -> [HumanBodyPose3DObservation.JointName : Joint3D]](humanbodypose3dobservation/alljoints(in:).md)
  Retrieves a dictionary of all joints in a joint group.
- [var availableJointsGroupNames: [HumanBodyPose3DObservation.JointsGroupName]](humanbodypose3dobservation/availablejointsgroupnames.md)
  The names of the available joint groupings in the observation.
- [func joint(for: HumanBodyPose3DObservation.JointName) -> Joint3D?](humanbodypose3dobservation/joint(for:).md)
  Retrieves a joint for a given joint name.
- [var availableJointNames: [HumanBodyPose3DObservation.JointName]](humanbodypose3dobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [HumanBodyPose3DObservation.JointName](humanbodypose3dobservation/jointname.md)
  The supported joint names for the body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/jointsgroupname)*