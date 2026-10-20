# availableJointNames

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The names of the available joints in the observation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var availableJointNames: [HumanBodyPose3DObservation.JointName] { get }
```

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
- [HumanBodyPose3DObservation.JointName](./jointname.md)
  The supported joint names for the body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/availablejointnames)*