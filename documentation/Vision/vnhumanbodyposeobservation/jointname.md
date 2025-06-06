# VNHumanBodyPoseObservation.JointName

**Framework**: Vision  
**Kind**: struct

The supported joint names for the body pose.

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

### Head
- [static let leftEar: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/leftear.md)
  The left ear.
- [static let leftEye: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/lefteye.md)
  The left eye.
- [static let rightEar: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/rightear.md)
  The right ear.
- [static let rightEye: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/righteye.md)
  The right eye.
- [static let neck: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/neck.md)
  The neck.
- [static let nose: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/nose.md)
  The nose.
### Arms
- [static let leftShoulder: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/leftshoulder.md)
  The left shoulder.
- [static let leftElbow: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/leftelbow.md)
  The left elbow.
- [static let leftWrist: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/leftwrist.md)
  The left wrist.
- [static let rightShoulder: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/rightshoulder.md)
  The right shoulder.
- [static let rightElbow: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/rightelbow.md)
  The right elbow.
- [static let rightWrist: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/rightwrist.md)
  The right wrist.
### Waist
- [static let root: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/root.md)
  The root (waist).
### Legs
- [static let leftHip: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/lefthip.md)
  The left hip.
- [static let leftKnee: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/leftknee.md)
  The left knee.
- [static let leftAnkle: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/leftankle.md)
  The left ankle.
- [static let rightHip: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/righthip.md)
  The right hip.
- [static let rightKnee: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/rightknee.md)
  The right knee.
- [static let rightAnkle: VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname/rightankle.md)
  The right ankle.
### Initializers
- [init(rawValue: VNRecognizedPointKey)](vnhumanbodyposeobservation/jointname/init(rawvalue:).md)
  Creates a joint name with a recognized point key.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var availableJointNames: [VNHumanBodyPoseObservation.JointName]](vnhumanbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](vnhumanbodyposeobservation/availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname.md)
  The supported joint group names for the body pose.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanbodyposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]](vnhumanbodyposeobservation/recognizedpoints(_:).md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation/jointname)*