# HumanHandPoseObservation

**Framework**: Vision  
**Kind**: struct

An observation that provides the hand points the analysis recognizes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct HumanHandPoseObservation
```

## Topics

### Creating an observation
- [init(VNHumanHandPoseObservation)](humanhandposeobservation/init(_:).md)
  Creates a human hand pose observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let chirality: HumanHandPoseObservation.Chirality?](humanhandposeobservation/chirality-swift.property.md)
  The chirality, or handedness, of a pose.
- [HumanHandPoseObservation.Chirality](humanhandposeobservation/chirality-swift.enum.md)
  The hand sidedness of a pose.
- [var keypoints: MLMultiArray](humanhandposeobservation/keypoints.md)
  The keypoints for the observation.
### Getting the joints
- [HumanHandPoseObservation.JointsGroupName](humanhandposeobservation/jointsgroupname.md)
  The joint group names available in the observation.
- [HumanHandPoseObservation.JointName](humanhandposeobservation/jointname.md)
  The supported joint names for the hand pose.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [PoseProviding](poseproviding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanhandposeobservation)*