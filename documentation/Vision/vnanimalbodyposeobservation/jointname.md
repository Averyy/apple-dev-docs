# VNAnimalBodyPoseObservation.JointName

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

The joint names for an animal body pose.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct JointName
```

```c
typedef VNRecognizedPointKey VNAnimalBodyPoseObservationJointName;
```

## Topics

### Getting the Head Joint Names
- [static let leftEarTop: VNAnimalBodyPoseObservation.JointName](./jointname/lefteartop.md)
  A joint name that represents the top of the left ear.
- [static let leftEarMiddle: VNAnimalBodyPoseObservation.JointName](./jointname/leftearmiddle.md)
  A joint name that represents the middle of the left ear.
- [static let leftEarBottom: VNAnimalBodyPoseObservation.JointName](./jointname/leftearbottom.md)
  A joint name that represents the bottom of the left ear.
- [static let leftEye: VNAnimalBodyPoseObservation.JointName](./jointname/lefteye.md)
  A joint name that represents the left eye.
- [static let neck: VNAnimalBodyPoseObservation.JointName](./jointname/neck.md)
  A joint name that represents the neck.
- [static let nose: VNAnimalBodyPoseObservation.JointName](./jointname/nose.md)
  A joint name that represents the nose.
- [static let rightEye: VNAnimalBodyPoseObservation.JointName](./jointname/righteye.md)
  A joint name that represents the right eye.
- [static let rightEarTop: VNAnimalBodyPoseObservation.JointName](./jointname/righteartop.md)
  A joint name that represents the top of the right ear.
- [static let rightEarMiddle: VNAnimalBodyPoseObservation.JointName](./jointname/rightearmiddle.md)
  A joint name that represents the middle of the right ear.
- [static let rightEarBottom: VNAnimalBodyPoseObservation.JointName](./jointname/rightearbottom.md)
  A joint name that represents the bottom of the right ear.
### Getting the Leg Joint Names
- [static let leftBackElbow: VNAnimalBodyPoseObservation.JointName](./jointname/leftbackelbow.md)
  A joint name that represents the back of the left elbow.
- [static let leftFrontElbow: VNAnimalBodyPoseObservation.JointName](./jointname/leftfrontelbow.md)
  A joint name that represents the front of the left elbow.
- [static let rightFrontElbow: VNAnimalBodyPoseObservation.JointName](./jointname/rightfrontelbow.md)
  A joint name that represents the front of the right elbow.
- [static let rightBackElbow: VNAnimalBodyPoseObservation.JointName](./jointname/rightbackelbow.md)
  A joint name that represents the back of the right elbow.
- [static let leftBackKnee: VNAnimalBodyPoseObservation.JointName](./jointname/leftbackknee.md)
  A joint name that represents the back of the left knee.
- [static let leftFrontKnee: VNAnimalBodyPoseObservation.JointName](./jointname/leftfrontknee.md)
  A joint name that represents the front of the left knee.
- [static let rightBackKnee: VNAnimalBodyPoseObservation.JointName](./jointname/rightbackknee.md)
  A joint name that represents the back of the right knee.
- [static let rightFrontKnee: VNAnimalBodyPoseObservation.JointName](./jointname/rightfrontknee.md)
  A joint name that represents the front of the right knee.
- [static let leftBackPaw: VNAnimalBodyPoseObservation.JointName](./jointname/leftbackpaw.md)
  A joint name that represents the back of the left paw.
- [static let leftFrontPaw: VNAnimalBodyPoseObservation.JointName](./jointname/leftfrontpaw.md)
  A joint name that represents the front of the left paw.
- [static let rightBackPaw: VNAnimalBodyPoseObservation.JointName](./jointname/rightbackpaw.md)
  A joint name that represents the back of the right paw.
- [static let rightFrontPaw: VNAnimalBodyPoseObservation.JointName](./jointname/rightfrontpaw.md)
  A joint name that represents the front of the right paw.
### Getting the Tail Joint Names
- [static let tailTop: VNAnimalBodyPoseObservation.JointName](./jointname/tailtop.md)
  A joint name that represents the top of the tail.
- [static let tailMiddle: VNAnimalBodyPoseObservation.JointName](./jointname/tailmiddle.md)
  A joint name that represents the middle of the tail.
- [static let tailBottom: VNAnimalBodyPoseObservation.JointName](./jointname/tailbottom.md)
  A joint name that represents the bottom of the tail.
### Creating a Joint Name
- [init(rawValue: VNRecognizedPointKey)](./jointname/init%28rawvalue%29.md)
  Creates a joint name with the key you specify.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Points
- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](./availablejointgroupnames.md)
  The available joint group names in the observation.
- [VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname.md)
  The joint group names for an animal body pose.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Returns the point for a joint name the observation recognizes.
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/jointname)*