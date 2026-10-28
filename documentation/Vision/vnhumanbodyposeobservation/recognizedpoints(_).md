# recognizedPoints(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Retrieves the recognized points associated with the joint group name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(_ jointsGroupName: VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]
```

```objc
- (NSDictionary<NSString *,VNRecognizedPoint *> *) recognizedPointsForJointsGroupName:(VNHumanBodyPoseObservationJointsGroupName) jointsGroupName error:(NSError **) error;
```

## Mentions

- [Detecting Human Body Poses in Images](../detecting-human-body-poses-in-images.md)

## Return Value

The array of points associated with the joint group name.

## Parameters

- `jointsGroupName`: The joint group name of the points to retrieve.

## See Also

### Accessing Points
- [var availableJointNames: [VNHumanBodyPoseObservation.JointName]](./availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPoseObservation.JointName](./jointname.md)
  The supported joint names for the body pose.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](./availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPoseObservation.JointsGroupName](./jointsgroupname.md)
  The supported joint group names for the body pose.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](./recognizedpoint%28_%29.md)
  Retrieves the recognized point for a joint name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation/recognizedpoints(_:))*