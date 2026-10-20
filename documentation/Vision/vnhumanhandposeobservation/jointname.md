# VNHumanHandPoseObservation.JointName

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

The supported joint names for the hand pose.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct JointName
```

```c
typedef VNRecognizedPointKey VNHumanHandPoseObservationJointName;
```

## Topics

### Thumb
- [static let thumbTip: VNHumanHandPoseObservation.JointName](./jointname/thumbtip.md)
  The tip of the thumb.
- [static let thumbIP: VNHumanHandPoseObservation.JointName](./jointname/thumbip.md)
  The thumb’s interphalangeal (IP) joint.
- [static let thumbMP: VNHumanHandPoseObservation.JointName](./jointname/thumbmp.md)
  The thumb’s metacarpophalangeal (MP) joint.
- [static let thumbCMC: VNHumanHandPoseObservation.JointName](./jointname/thumbcmc.md)
  The thumb’s carpometacarpal (CMC) joint.
### Index
- [static let indexTip: VNHumanHandPoseObservation.JointName](./jointname/indextip.md)
  The tip of the index finger.
- [static let indexDIP: VNHumanHandPoseObservation.JointName](./jointname/indexdip.md)
  The index finger’s distal interphalangeal (DIP) joint.
- [static let indexPIP: VNHumanHandPoseObservation.JointName](./jointname/indexpip.md)
  The index finger’s proximal interphalangeal (PIP) joint.
- [static let indexMCP: VNHumanHandPoseObservation.JointName](./jointname/indexmcp.md)
  The index finger’s metacarpophalangeal (MCP) joint.
### Middle
- [static let middleTip: VNHumanHandPoseObservation.JointName](./jointname/middletip.md)
  The tip of the middle finger.
- [static let middleDIP: VNHumanHandPoseObservation.JointName](./jointname/middledip.md)
  The middle finger’s distal interphalangeal (DIP) joint.
- [static let middlePIP: VNHumanHandPoseObservation.JointName](./jointname/middlepip.md)
  The middle finger’s proximal interphalangeal (PIP) joint.
- [static let middleMCP: VNHumanHandPoseObservation.JointName](./jointname/middlemcp.md)
  The middle finger’s metacarpophalangeal (MCP) joint.
### Ring
- [static let ringTip: VNHumanHandPoseObservation.JointName](./jointname/ringtip.md)
  The tip of the ring finger.
- [static let ringDIP: VNHumanHandPoseObservation.JointName](./jointname/ringdip.md)
  The ring finger’s distal interphalangeal (DIP) joint.
- [static let ringPIP: VNHumanHandPoseObservation.JointName](./jointname/ringpip.md)
  The ring finger’s proximal interphalangeal (PIP) joint.
- [static let ringMCP: VNHumanHandPoseObservation.JointName](./jointname/ringmcp.md)
  The ring finger’s metacarpophalangeal (MCP) joint.
### Little
- [static let littleTip: VNHumanHandPoseObservation.JointName](./jointname/littletip.md)
  The tip of the little finger.
- [static let littleDIP: VNHumanHandPoseObservation.JointName](./jointname/littledip.md)
  The little finger’s distal interphalangeal (DIP) joint.
- [static let littlePIP: VNHumanHandPoseObservation.JointName](./jointname/littlepip.md)
  The little finger’s proximal interphalangeal (PIP) joint.
- [static let littleMCP: VNHumanHandPoseObservation.JointName](./jointname/littlemcp.md)
  The little finger’s metacarpophalangeal (MCP) joint.
### Wrist
- [static let wrist: VNHumanHandPoseObservation.JointName](./jointname/wrist.md)
  The wrist.
### Initializers
- [init(rawValue: VNRecognizedPointKey)](./jointname/init%28rawvalue%29.md)
  Creates a joint name with a recognized point key.

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
- [var availableJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The joint group names available in the observation.
- [VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname.md)
  The supported joint group names for the hand pose.
- [func recognizedPoint(VNHumanHandPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanHandPoseObservation.JointsGroupName) throws -> [VNHumanHandPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanhandposeobservation/jointname)*