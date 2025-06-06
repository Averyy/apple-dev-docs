# VNHumanBodyPoseObservation.JointsGroupName

**Framework**: Vision  
**Kind**: struct

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

## Mentions

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)

## Topics

### Head
- [static let face: VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname/face.md)
  The face.
### Body
- [static let torso: VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname/torso.md)
  The torso.
### Arms
- [static let leftArm: VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname/leftarm.md)
  The left arm.
- [static let rightArm: VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname/rightarm.md)
  The right arm.
### Legs
- [static let leftLeg: VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname/leftleg.md)
  The left leg.
- [static let rightLeg: VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname/rightleg.md)
  The right leg.
### All
- [static let all: VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname/all.md)
  All body point groups.
### Initializers
- [init(rawValue: VNRecognizedPointGroupKey)](vnhumanbodyposeobservation/jointsgroupname/init(rawvalue:).md)
  Creates a joint group name with a recognized point group key.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var availableJointNames: [VNHumanBodyPoseObservation.JointName]](vnhumanbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname.md)
  The supported joint names for the body pose.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](vnhumanbodyposeobservation/availablejointsgroupnames.md)
  The available joint group names in the observation.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanbodyposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]](vnhumanbodyposeobservation/recognizedpoints(_:).md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation/jointsgroupname)*