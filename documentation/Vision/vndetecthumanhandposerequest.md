# VNDetectHumanHandPoseRequest

**Framework**: Vision  
**Kind**: class

A request that detects a human hand pose.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectHumanHandPoseRequest
```

#### Overview

The framework provides the detected hand pose as a `VNIdentifiedPointsObservation`.

## Topics

### Configuring the Request
- [var maximumHandCount: Int](vndetecthumanhandposerequest/maximumhandcount.md)
  The maximum number of hands to detect in an image.
### Determining Supported Joints
- [var supportedJointNames: [VNHumanHandPoseObservation.JointName]](vndetecthumanhandposerequest/supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointName]](vndetecthumanhandposerequest/supportedjointnames(forrevision:).md)
  Retrieves the supported joint names for a revision.
- [var supportedJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](vndetecthumanhandposerequest/supportedjointsgroupnames.md)
  Retrieves the supported joint group names.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointsGroupName]](vndetecthumanhandposerequest/supportedjointsgroupnames(forrevision:).md)
  Retrieves the supported joint group names for a revision.
### Accessing the Results
- [var results: [VNHumanHandPoseObservation]?](vndetecthumanhandposerequest/results.md)
  The observed hand poses.
### Identifying Hand Pose Revisions
- [let VNDetectHumanHandPoseRequestRevision1: Int](vndetecthumanhandposerequestrevision1.md)
  A constant for specifying revision 1 of the hand pose detection request.

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

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)
  Add the capability to detect human body poses to your app using the Vision framework.
- [Detecting Hand Poses with Vision](detecting-hand-poses-with-vision.md)
  Create a virtual drawing app by using Vision’s capability to detect hand poses.
- [class VNDetectHumanBodyPoseRequest](vndetecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [class VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
  An observation that provides the points the analysis recognized.
- [class VNHumanBodyPoseObservation](vnhumanbodyposeobservation.md)
  An observation that provides the body points the analysis recognized.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest)*