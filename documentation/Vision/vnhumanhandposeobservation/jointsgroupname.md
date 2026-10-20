# VNHumanHandPoseObservation.JointsGroupName

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

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

```c
typedef VNRecognizedPointGroupKey VNHumanHandPoseObservationJointsGroupName;
```

## Topics

### Group Names
- [static let thumb: VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname/thumb.md)
  The thumb.
- [static let indexFinger: VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname/indexfinger.md)
  The index finger.
- [static let littleFinger: VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname/littlefinger.md)
  The little finger.
- [static let middleFinger: VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname/middlefinger.md)
  The middle finger.
- [static let ringFinger: VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname/ringfinger.md)
  The ring finger.
- [static let all: VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname/all.md)
  All hand group names.
### Initializers
- [init(rawValue: VNRecognizedPointGroupKey)](./jointsgroupname/init%28rawvalue%29.md)
  Creates a joint group name with a recognized point group key.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving Points
- [var availableJointNames: [VNHumanHandPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanHandPoseObservation.JointName](./jointname.md)
  The supported joint names for the hand pose.
- [var availableJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The joint group names available in the observation.
- [func recognizedPoint(VNHumanHandPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanHandPoseObservation.JointsGroupName) throws -> [VNHumanHandPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanhandposeobservation/jointsgroupname)*