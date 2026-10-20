# HumanBodyPose3DObservation.JointName

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

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
- [HumanBodyPose3DObservation.JointName.centerHead](./jointname/centerhead.md)
- [HumanBodyPose3DObservation.JointName.centerShoulder](./jointname/centershoulder.md)
- [HumanBodyPose3DObservation.JointName.leftAnkle](./jointname/leftankle.md)
- [HumanBodyPose3DObservation.JointName.leftElbow](./jointname/leftelbow.md)
- [HumanBodyPose3DObservation.JointName.leftHip](./jointname/lefthip.md)
- [HumanBodyPose3DObservation.JointName.leftKnee](./jointname/leftknee.md)
- [HumanBodyPose3DObservation.JointName.leftShoulder](./jointname/leftshoulder.md)
- [HumanBodyPose3DObservation.JointName.leftWrist](./jointname/leftwrist.md)
- [HumanBodyPose3DObservation.JointName.rightAnkle](./jointname/rightankle.md)
- [HumanBodyPose3DObservation.JointName.rightElbow](./jointname/rightelbow.md)
- [HumanBodyPose3DObservation.JointName.rightHip](./jointname/righthip.md)
- [HumanBodyPose3DObservation.JointName.rightKnee](./jointname/rightknee.md)
- [HumanBodyPose3DObservation.JointName.rightShoulder](./jointname/rightshoulder.md)
- [HumanBodyPose3DObservation.JointName.rightWrist](./jointname/rightwrist.md)
- [HumanBodyPose3DObservation.JointName.root](./jointname/root.md)
- [HumanBodyPose3DObservation.JointName.spine](./jointname/spine.md)
- [HumanBodyPose3DObservation.JointName.topHead](./jointname/tophead.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
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
- [HumanBodyPose3DObservation.JointsGroupName](./jointsgroupname.md)
  The supported joint group names for the body pose.
- [func joint(for: HumanBodyPose3DObservation.JointName) -> Joint3D?](./joint%28for%29.md)
  Retrieves a joint for a given joint name.
- [var availableJointNames: [HumanBodyPose3DObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/jointname)*