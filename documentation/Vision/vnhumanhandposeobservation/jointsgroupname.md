# VNHumanHandPoseObservation.JointsGroupName

**Framework**: Vision  
**Kind**: struct

The supported joint group names for the hand pose.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct JointsGroupName
```

## Topics

### Group Names
- [static let thumb: VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname/thumb.md)
  The thumb.
- [static let indexFinger: VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname/indexfinger.md)
  The index finger.
- [static let littleFinger: VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname/littlefinger.md)
  The little finger.
- [static let middleFinger: VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname/middlefinger.md)
  The middle finger.
- [static let ringFinger: VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname/ringfinger.md)
  The ring finger.
- [static let all: VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname/all.md)
  All hand group names.
### Initializers
- [init(rawValue: VNRecognizedPointGroupKey)](vnhumanhandposeobservation/jointsgroupname/init(rawvalue:).md)
  Creates a joint group name with a recognized point group key.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var availableJointNames: [VNHumanHandPoseObservation.JointName]](vnhumanhandposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname.md)
  The supported joint names for the hand pose.
- [var availableJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](vnhumanhandposeobservation/availablejointsgroupnames.md)
  The joint group names available in the observation.
- [func recognizedPoint(VNHumanHandPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanhandposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanHandPoseObservation.JointsGroupName) throws -> [VNHumanHandPoseObservation.JointName : VNRecognizedPoint]](vnhumanhandposeobservation/recognizedpoints(_:).md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanhandposeobservation/jointsgroupname)*