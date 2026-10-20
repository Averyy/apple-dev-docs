# VNHumanBodyPoseObservation.JointName

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

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

```c
typedef VNRecognizedPointKey VNHumanBodyPoseObservationJointName;
```

## Topics

### Head
- [static let leftEar: VNHumanBodyPoseObservation.JointName](./jointname/leftear.md)
  The left ear.
- [static let leftEye: VNHumanBodyPoseObservation.JointName](./jointname/lefteye.md)
  The left eye.
- [static let rightEar: VNHumanBodyPoseObservation.JointName](./jointname/rightear.md)
  The right ear.
- [static let rightEye: VNHumanBodyPoseObservation.JointName](./jointname/righteye.md)
  The right eye.
- [static let neck: VNHumanBodyPoseObservation.JointName](./jointname/neck.md)
  The neck.
- [static let nose: VNHumanBodyPoseObservation.JointName](./jointname/nose.md)
  The nose.
### Arms
- [static let leftShoulder: VNHumanBodyPoseObservation.JointName](./jointname/leftshoulder.md)
  The left shoulder.
- [static let leftElbow: VNHumanBodyPoseObservation.JointName](./jointname/leftelbow.md)
  The left elbow.
- [static let leftWrist: VNHumanBodyPoseObservation.JointName](./jointname/leftwrist.md)
  The left wrist.
- [static let rightShoulder: VNHumanBodyPoseObservation.JointName](./jointname/rightshoulder.md)
  The right shoulder.
- [static let rightElbow: VNHumanBodyPoseObservation.JointName](./jointname/rightelbow.md)
  The right elbow.
- [static let rightWrist: VNHumanBodyPoseObservation.JointName](./jointname/rightwrist.md)
  The right wrist.
### Waist
- [static let root: VNHumanBodyPoseObservation.JointName](./jointname/root.md)
  The root (waist).
### Legs
- [static let leftHip: VNHumanBodyPoseObservation.JointName](./jointname/lefthip.md)
  The left hip.
- [static let leftKnee: VNHumanBodyPoseObservation.JointName](./jointname/leftknee.md)
  The left knee.
- [static let leftAnkle: VNHumanBodyPoseObservation.JointName](./jointname/leftankle.md)
  The left ankle.
- [static let rightHip: VNHumanBodyPoseObservation.JointName](./jointname/righthip.md)
  The right hip.
- [static let rightKnee: VNHumanBodyPoseObservation.JointName](./jointname/rightknee.md)
  The right knee.
- [static let rightAnkle: VNHumanBodyPoseObservation.JointName](./jointname/rightankle.md)
  The right ankle.
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

### Accessing Points
- [var availableJointNames: [VNHumanBodyPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname.md)
  The supported joint group names for the body pose.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation/jointname)*