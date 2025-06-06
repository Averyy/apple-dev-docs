# VNHumanBodyPoseObservation

**Framework**: Vision  
**Kind**: class

An observation that provides the body points the analysis recognized.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNHumanBodyPoseObservation
```

## Mentions

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)

## Topics

### Accessing Points
- [var availableJointNames: [VNHumanBodyPoseObservation.JointName]](vnhumanbodyposeobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [VNHumanBodyPoseObservation.JointName](vnhumanbodyposeobservation/jointname.md)
  The supported joint names for the body pose.
- [var availableJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](vnhumanbodyposeobservation/availablejointsgroupnames.md)
  The available joint group names in the observation.
- [VNHumanBodyPoseObservation.JointsGroupName](vnhumanbodyposeobservation/jointsgroupname.md)
  The supported joint group names for the body pose.
- [func recognizedPoint(VNHumanBodyPoseObservation.JointName) throws -> VNRecognizedPoint](vnhumanbodyposeobservation/recognizedpoint(_:).md)
  Retrieves the recognized point for a joint name.
- [func recognizedPoints(VNHumanBodyPoseObservation.JointsGroupName) throws -> [VNHumanBodyPoseObservation.JointName : VNRecognizedPoint]](vnhumanbodyposeobservation/recognizedpoints(_:).md)
  Retrieves the recognized points associated with the joint group name.

## Relationships

### Inherits From
- [VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)
  Add the capability to detect human body poses to your app using the Vision framework.
- [Detecting Hand Poses with Vision](detecting-hand-poses-with-vision.md)
  Create a virtual drawing app by using Vision’s capability to detect hand poses.
- [class VNDetectHumanBodyPoseRequest](vndetecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [class VNDetectHumanHandPoseRequest](vndetecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [class VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
  An observation that provides the points the analysis recognized.
- [class VNHumanHandPoseObservation](vnhumanhandposeobservation.md)
  An observation that provides the hand points the analysis recognized.
- [class VNPoint](vnpoint.md)
  An immutable object that represents a single 2D point in an image.
- [class VNDetectedPoint](vndetectedpoint.md)
  An object that represents a normalized point in an image, along with a confidence value.
- [class VNRecognizedPoint](vnrecognizedpoint.md)
  An object that represents a normalized point in an image, along with an identifier label and a confidence value.
- [struct VNRecognizedPointKey](vnrecognizedpointkey.md)
  The data type for all recognized point keys.
- [struct VNRecognizedPointGroupKey](vnrecognizedpointgroupkey.md)
  The data type for all recognized-point group keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation)*