# VNHumanBodyPoseObservation.JointsGroupName

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

The supported joint group names for the body pose.

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
typedef VNRecognizedPointGroupKey VNHumanBodyPoseObservationJointsGroupName;
```

## Mentions

- [Detecting Human Body Poses in Images](../detecting-human-body-poses-in-images.md)

## Topics

### Head
- [static let face: VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname/face.md)
  The face.
### Body
- [static let torso: VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname/torso.md)
  The torso.
### Arms
- [static let leftArm: VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname/leftarm.md)
  The left arm.
- [static let rightArm: VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname/rightarm.md)
  The right arm.
### Legs
- [static let leftLeg: VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname/leftleg.md)
  The left leg.
- [static let rightLeg: VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname/rightleg.md)
  The right leg.
### All
- [static let all: VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname/all.md)
  All body point groups.
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

### Accessing Points
- [var availableJointNames: [VNHumanBodyPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPoseObservation.JointName](./jointname.md)
  The supported joint names for the body pose.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The available joint group names in the observation.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation/jointsgroupname)*