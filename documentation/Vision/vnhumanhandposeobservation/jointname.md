# VNHumanHandPoseObservation.JointName

**Framework**: Vision  
**Kind**: struct

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

## Topics

### Thumb
- [static let thumbTip: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/thumbtip.md)
  The tip of the thumb.
- [static let thumbIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/thumbip.md)
  The thumb’s interphalangeal (IP) joint.
- [static let thumbMP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/thumbmp.md)
  The thumb’s metacarpophalangeal (MP) joint.
- [static let thumbCMC: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/thumbcmc.md)
  The thumb’s carpometacarpal (CMC) joint.
### Index
- [static let indexTip: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/indextip.md)
  The tip of the index finger.
- [static let indexDIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/indexdip.md)
  The index finger’s distal interphalangeal (DIP) joint.
- [static let indexPIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/indexpip.md)
  The index finger’s proximal interphalangeal (PIP) joint.
- [static let indexMCP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/indexmcp.md)
  The index finger’s metacarpophalangeal (MCP) joint.
### Middle
- [static let middleTip: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/middletip.md)
  The tip of the middle finger.
- [static let middleDIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/middledip.md)
  The middle finger’s distal interphalangeal (DIP) joint.
- [static let middlePIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/middlepip.md)
  The middle finger’s proximal interphalangeal (PIP) joint.
- [static let middleMCP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/middlemcp.md)
  The middle finger’s metacarpophalangeal (MCP) joint.
### Ring
- [static let ringTip: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/ringtip.md)
  The tip of the ring finger.
- [static let ringDIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/ringdip.md)
  The ring finger’s distal interphalangeal (DIP) joint.
- [static let ringPIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/ringpip.md)
  The ring finger’s proximal interphalangeal (PIP) joint.
- [static let ringMCP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/ringmcp.md)
  The ring finger’s metacarpophalangeal (MCP) joint.
### Little
- [static let littleTip: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/littletip.md)
  The tip of the little finger.
- [static let littleDIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/littledip.md)
  The little finger’s distal interphalangeal (DIP) joint.
- [static let littlePIP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/littlepip.md)
  The little finger’s proximal interphalangeal (PIP) joint.
- [static let littleMCP: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/littlemcp.md)
  The little finger’s metacarpophalangeal (MCP) joint.
### Wrist
- [static let wrist: VNHumanHandPoseObservation.JointName](vnhumanhandposeobservation/jointname/wrist.md)
  The wrist.
### Initializers
- [init(rawValue: VNRecognizedPointKey)](vnhumanhandposeobservation/jointname/init(rawvalue:).md)
  Creates a joint name with a recognized point key.

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
- [var availableJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](vnhumanhandposeobservation/availablejointsgroupnames.md)
  The joint group names available in the observation.
- [VNHumanHandPoseObservation.JointsGroupName](vnhumanhandposeobservation/jointsgroupname.md)
  The supported joint group names for the hand pose.
- [func recognizedPoint(VNHumanHandPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanhandposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanHandPoseObservation.JointsGroupName) throws -> [VNHumanHandPoseObservation.JointName : VNRecognizedPoint]](vnhumanhandposeobservation/recognizedpoints(_:).md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanhandposeobservation/jointname)*