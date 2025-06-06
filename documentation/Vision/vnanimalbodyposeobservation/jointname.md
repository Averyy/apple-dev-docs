# VNAnimalBodyPoseObservation.JointName

**Framework**: Vision  
**Kind**: struct

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

## Topics

### Getting the Head Joint Names
- [static let leftEarTop: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/lefteartop.md)
  A joint name that represents the top of the left ear.
- [static let leftEarMiddle: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftearmiddle.md)
  A joint name that represents the middle of the left ear.
- [static let leftEarBottom: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftearbottom.md)
  A joint name that represents the bottom of the left ear.
- [static let leftEye: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/lefteye.md)
  A joint name that represents the left eye.
- [static let neck: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/neck.md)
  A joint name that represents the neck.
- [static let nose: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/nose.md)
  A joint name that represents the nose.
- [static let rightEye: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/righteye.md)
  A joint name that represents the right eye.
- [static let rightEarTop: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/righteartop.md)
  A joint name that represents the top of the right ear.
- [static let rightEarMiddle: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightearmiddle.md)
  A joint name that represents the middle of the right ear.
- [static let rightEarBottom: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightearbottom.md)
  A joint name that represents the bottom of the right ear.
### Getting the Leg Joint Names
- [static let leftBackElbow: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftbackelbow.md)
  A joint name that represents the back of the left elbow.
- [static let leftFrontElbow: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftfrontelbow.md)
  A joint name that represents the front of the left elbow.
- [static let rightFrontElbow: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightfrontelbow.md)
  A joint name that represents the front of the right elbow.
- [static let rightBackElbow: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightbackelbow.md)
  A joint name that represents the back of the right elbow.
- [static let leftBackKnee: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftbackknee.md)
  A joint name that represents the back of the left knee.
- [static let leftFrontKnee: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftfrontknee.md)
  A joint name that represents the front of the left knee.
- [static let rightBackKnee: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightbackknee.md)
  A joint name that represents the back of the right knee.
- [static let rightFrontKnee: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightfrontknee.md)
  A joint name that represents the front of the right knee.
- [static let leftBackPaw: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftbackpaw.md)
  A joint name that represents the back of the left paw.
- [static let leftFrontPaw: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/leftfrontpaw.md)
  A joint name that represents the front of the left paw.
- [static let rightBackPaw: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightbackpaw.md)
  A joint name that represents the back of the right paw.
- [static let rightFrontPaw: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/rightfrontpaw.md)
  A joint name that represents the front of the right paw.
### Getting the Tail Joint Names
- [static let tailTop: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/tailtop.md)
  A joint name that represents the top of the tail.
- [static let tailMiddle: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/tailmiddle.md)
  A joint name that represents the middle of the tail.
- [static let tailBottom: VNAnimalBodyPoseObservation.JointName](vnanimalbodyposeobservation/jointname/tailbottom.md)
  A joint name that represents the bottom of the tail.
### Creating a Joint Name
- [init(rawValue: VNRecognizedPointKey)](vnanimalbodyposeobservation/jointname/init(rawvalue:).md)
  Creates a joint name with the key you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](vnanimalbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](vnanimalbodyposeobservation/availablejointgroupnames.md)
  The available joint group names in the observation.
- [VNAnimalBodyPoseObservation.JointsGroupName](vnanimalbodyposeobservation/jointsgroupname.md)
  The joint group names for an animal body pose.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnanimalbodyposeobservation/recognizedpoint(_:).md)
  Returns the point for a joint name the observation recognizes.
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](vnanimalbodyposeobservation/recognizedpoints(_:).md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/jointname)*