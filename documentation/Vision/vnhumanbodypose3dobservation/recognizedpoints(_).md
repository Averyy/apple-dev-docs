# recognizedPoints(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns a collection of points for the group name you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(_ jointsGroupName: VNHumanBodyPose3DObservation.JointsGroupName) throws -> [VNHumanBodyPose3DObservation.JointName : VNHumanBodyRecognizedPoint3D]
```

```objc
- (NSDictionary<NSString *,VNHumanBodyRecognizedPoint3D *> *) recognizedPointsForJointsGroupName:(VNHumanBodyPose3DObservationJointsGroupName) jointsGroupName error:(NSError **) error;
```

## Return Value

A collection of points.

## Parameters

- `jointsGroupName`: The name of the human body joints group.

## See Also

### Accessing Points
- [var availableJointNames: [VNHumanBodyPose3DObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPose3DObservation.JointName](./jointname.md)
  The joint names for a 3D body pose.
- [var availableJointsGroupNames: [VNHumanBodyPose3DObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPose3DObservation.JointsGroupName](./jointsgroupname.md)
  The joint group names for a 3D body pose.
- [func recognizedPoint(VNHumanBodyPose3DObservation.JointName) throws -> VNHumanBodyRecognizedPoint3D](./recognizedpoint%28_%29.md)
  Returns the point for a joint name that the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/recognizedpoints(_:))*