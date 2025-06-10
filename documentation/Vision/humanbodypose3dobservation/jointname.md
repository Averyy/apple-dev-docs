# HumanBodyPose3DObservation.JointName

**Framework**: Vision  
**Kind**: enum

The supported joint names for the body pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum JointName
```

## Topics

### Getting the joint names
- [HumanBodyPose3DObservation.JointName.centerHead](humanbodypose3dobservation/jointname/centerhead.md)
- [HumanBodyPose3DObservation.JointName.centerShoulder](humanbodypose3dobservation/jointname/centershoulder.md)
- [HumanBodyPose3DObservation.JointName.leftAnkle](humanbodypose3dobservation/jointname/leftankle.md)
- [HumanBodyPose3DObservation.JointName.leftElbow](humanbodypose3dobservation/jointname/leftelbow.md)
- [HumanBodyPose3DObservation.JointName.leftHip](humanbodypose3dobservation/jointname/lefthip.md)
- [HumanBodyPose3DObservation.JointName.leftKnee](humanbodypose3dobservation/jointname/leftknee.md)
- [HumanBodyPose3DObservation.JointName.leftShoulder](humanbodypose3dobservation/jointname/leftshoulder.md)
- [HumanBodyPose3DObservation.JointName.leftWrist](humanbodypose3dobservation/jointname/leftwrist.md)
- [HumanBodyPose3DObservation.JointName.rightAnkle](humanbodypose3dobservation/jointname/rightankle.md)
- [HumanBodyPose3DObservation.JointName.rightElbow](humanbodypose3dobservation/jointname/rightelbow.md)
- [HumanBodyPose3DObservation.JointName.rightHip](humanbodypose3dobservation/jointname/righthip.md)
- [HumanBodyPose3DObservation.JointName.rightKnee](humanbodypose3dobservation/jointname/rightknee.md)
- [HumanBodyPose3DObservation.JointName.rightShoulder](humanbodypose3dobservation/jointname/rightshoulder.md)
- [HumanBodyPose3DObservation.JointName.rightWrist](humanbodypose3dobservation/jointname/rightwrist.md)
- [HumanBodyPose3DObservation.JointName.root](humanbodypose3dobservation/jointname/root.md)
- [HumanBodyPose3DObservation.JointName.spine](humanbodypose3dobservation/jointname/spine.md)
- [HumanBodyPose3DObservation.JointName.topHead](humanbodypose3dobservation/jointname/tophead.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func allJoints(in: HumanBodyPose3DObservation.JointsGroupName?) -> [HumanBodyPose3DObservation.JointName : Joint3D]](humanbodypose3dobservation/alljoints(in:).md)
  Retrieves a dictionary of all joints in a joint group.
- [var availableJointsGroupNames: [HumanBodyPose3DObservation.JointsGroupName]](humanbodypose3dobservation/availablejointsgroupnames.md)
  The names of the available joint groupings in the observation.
- [HumanBodyPose3DObservation.JointsGroupName](humanbodypose3dobservation/jointsgroupname.md)
  The supported joint group names for the body pose.
- [func joint(for: HumanBodyPose3DObservation.JointName) -> Joint3D?](humanbodypose3dobservation/joint(for:).md)
  Retrieves a joint for a given joint name.
- [var availableJointNames: [HumanBodyPose3DObservation.JointName]](humanbodypose3dobservation/availablejointnames.md)
  The names of the available joints in the observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/jointname)*