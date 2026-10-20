# availableJointNames

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The names of the available joints in the observation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var availableJointNames: [VNHumanBodyPose3DObservation.JointName] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * availableJointNames;
```

## See Also

### Accessing Points
- [VNHumanBodyPose3DObservation.JointName](./jointname.md)
  The joint names for a 3D body pose.
- [var availableJointsGroupNames: [VNHumanBodyPose3DObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPose3DObservation.JointsGroupName](./jointsgroupname.md)
  The joint group names for a 3D body pose.
- [func recognizedPoint(VNHumanBodyPose3DObservation.JointName) throws -> VNHumanBodyRecognizedPoint3D](./recognizedpoint%28_%29.md)
  Returns the point for a joint name that the observation recognizes.
- [func recognizedPoints(VNHumanBodyPose3DObservation.JointsGroupName) throws -> [VNHumanBodyPose3DObservation.JointName : VNHumanBodyRecognizedPoint3D]](./recognizedpoints%28_%29.md)
  Returns a collection of points for the group name you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/availablejointnames)*