# recognizedPoint(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns the point for a joint name the observation recognizes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoint(_ jointName: VNAnimalBodyPoseObservation.JointName) throws -> VNRecognizedPoint
```

```objc
- (VNRecognizedPoint *) recognizedPointForJointName:(VNAnimalBodyPoseObservationJointName) jointName error:(NSError **) error;
```

## Return Value

The point for the joint name.

## Parameters

- `jointName`: The joint name to retrieve.

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
- [func recognizedPoints(VNAnimalBodyPoseObservation.JointsGroupName) throws -> [VNAnimalBodyPoseObservation.JointName : VNRecognizedPoint]](./recognizedpoints%28_%29.md)
  Returns the points for a joint group name the observation recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalbodyposeobservation/recognizedpoint(_:))*