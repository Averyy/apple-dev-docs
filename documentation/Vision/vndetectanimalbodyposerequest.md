# VNDetectAnimalBodyPoseRequest

**Framework**: Vision  
**Kind**: class

A request that detects an animal body pose.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectAnimalBodyPoseRequest
```

## Topics

### Determining Supported Joints
- [var supportedJointNames: [VNAnimalBodyPoseObservation.JointName]](vndetectanimalbodyposerequest/supportedjointnames.md)
  Retrieves the joint names the request supports.
- [var supportedJointsGroupNames: [VNAnimalBodyPoseObservation.JointsGroupName]](vndetectanimalbodyposerequest/supportedjointsgroupnames.md)
  Retrieves the joint group names the request supports.
### Accessing the Results
- [var results: [VNAnimalBodyPoseObservation]?](vndetectanimalbodyposerequest/results.md)
  The animal body pose the request observes.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Detecting animal body poses with Vision](detecting-animal-body-poses-with-vision.md)
  Draw the skeleton of an animal by using Vision’s capability to detect animal body poses.
- [class VNAnimalBodyPoseObservation](vnanimalbodyposeobservation.md)
  An observation that provides the animal body points the analysis recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectanimalbodyposerequest)*