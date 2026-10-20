# availableJointGroupNames

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The available joint group names in the observation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * availableJointGroupNames;
```

## See Also

### Accessing Points
- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNAnimalBodyPoseObservation.JointName](./jointname.md)
  The joint names for an animal body pose.
- [VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname.md)
  The joint group names for an animal body pose.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Returns the point for a joint name the observation recognizes.
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/availablejointgroupnames)*