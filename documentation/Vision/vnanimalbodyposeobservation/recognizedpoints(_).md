# recognizedPoints(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns the points for a joint group name the observation recognizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(_ jointsGroupName: VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]
```

```objc
- (NSDictionary<NSString *,VNRecognizedPoint *> *) recognizedPointsForJointsGroupName:(VNAnimalBodyPoseObservationJointsGroupName) jointsGroupName error:(NSError **) error;
```

## Return Value

The dictionary of points the observation associates with the group name.

## Parameters

- `jointsGroupName`: The joint group of the points to retrieve.

## See Also

### Accessing Points
- [var availableJointNames: [VNAnimalBodyPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNAnimalBodyPoseObservation.JointName](./jointname.md)
  The joint names for an animal body pose.
- [var availableJointGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](./availablejointgroupnames.md)
  The available joint group names in the observation.
- [VNAnimalBodyPoseObservation.JointsGroupName](./jointsgroupname.md)
  The joint group names for an animal body pose.
- [func recognizedPoint(VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Returns the point for a joint name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/recognizedpoints(_:))*