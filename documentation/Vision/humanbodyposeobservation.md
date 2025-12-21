# HumanBodyPoseObservation

**Framework**: Vision  
**Kind**: struct

An observation that provides the body points the analysis recognizes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct HumanBodyPoseObservation
```

## Topics

### Creating an observation
- [init(VNHumanBodyPoseObservation)](humanbodyposeobservation/init(_:).md)
  Creates a human body pose observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let leftHand: HumanHandPoseObservation?](humanbodyposeobservation/lefthand.md)
  The observed left hand.
- [let rightHand: HumanHandPoseObservation?](humanbodyposeobservation/righthand.md)
  The observed right hand.
- [struct HumanHandPoseObservation](humanhandposeobservation.md)
  An observation that provides the hand points the analysis recognizes.
- [var keypoints: MLMultiArray](humanbodyposeobservation/keypoints.md)
  A multi-array compatible with Core ML that contains normalized point coordinates and confidence scores.
### Getting the joints
- [HumanBodyPoseObservation.JointsGroupName](humanbodyposeobservation/jointsgroupname.md)
  The joint group names available in the observation.
- [HumanBodyPoseObservation.JointName](humanbodyposeobservation/jointname.md)
  The supported joint names for the body pose.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [PoseProviding](poseproviding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodyposeobservation)*