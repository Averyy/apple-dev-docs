# PoseProviding

**Framework**: Vision  
**Kind**: protocol

An observation that provides a collection of joints that make up a pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol PoseProviding
```

## Topics

### Getting the joints
- [func joint(for: Self.PoseJointName) -> Joint?](poseproviding/joint(for:).md)
  Retrieves a joint for a given joint name.
- [func allJoints(in: Self.PoseJointsGroupName?) -> [Self.PoseJointName : Joint]](poseproviding/alljoints(in:).md)
  Retrieves a dictionary of all joints in the observation or joint group.
### Getting the joint names
- [var availableJointNames: [Self.PoseJointName]](poseproviding/availablejointnames.md)
  The names of the available joints in the observation.
- [associatedtype PoseJointName : Decodable, Encodable, Hashable, RawRepresentable](poseproviding/posejointname.md)
  A type that represents a joint name.
### Getting the joint group names
- [var availableJointsGroupNames: [Self.PoseJointsGroupName]](poseproviding/availablejointsgroupnames.md)
  The names of the available joint groupings in the observation.
- [associatedtype PoseJointsGroupName : CaseIterable, RawRepresentable](poseproviding/posejointsgroupname.md)
  A type that represents a joint group name.

## Relationships

### Conforming Types
- [AnimalBodyPoseObservation](animalbodyposeobservation.md)
- [HumanBodyPoseObservation](humanbodyposeobservation.md)
- [HumanHandPoseObservation](humanhandposeobservation.md)

## See Also

- [struct DetectHumanBodyPoseRequest](detecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [struct DetectHumanHandPoseRequest](detecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [enum Chirality](chirality.md)
  The hand sidedness of a pose.
- [struct Joint](joint.md)
  A pose joint represented as a normalized point in an image, along with a label and a confidence value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/poseproviding)*