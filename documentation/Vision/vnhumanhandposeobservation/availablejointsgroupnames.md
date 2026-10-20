# availableJointsGroupNames

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The joint group names available in the observation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var availableJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * availableJointsGroupNames;
```

## See Also

### Retrieving Points
- [var availableJointNames: [VNHumanHandPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanHandPoseObservation.JointName](./jointname.md)
  The supported joint names for the hand pose.
- [VNHumanHandPoseObservation.JointsGroupName](./jointsgroupname.md)
  The supported joint group names for the hand pose.
- [func recognizedPoint(VNHumanHandPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanHandPoseObservation.JointsGroupName) throws -> [VNHumanHandPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Retrieves the recognized points associated with the joint group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanhandposeobservation/availablejointsgroupnames)*