# VNDetectHumanBodyPoseRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

A request that detects a human body pose.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectHumanBodyPoseRequest
```

```objc
@interface VNDetectHumanBodyPoseRequest : VNImageBasedRequest
```

## Mentions

- [Detecting Human Body Poses in Images](./detecting-human-body-poses-in-images.md)

## Overview

The framework provides the detected body pose as a [`VNHumanBodyPoseObservation`](./vnhumanbodyposeobservation.md).

## Topics

### Determining Supported Joints
- [var supportedJointNames: [VNHumanBodyPoseObservation.JointName]](./vndetecthumanbodyposerequest/supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointName]](./vndetecthumanbodyposerequest/supportedjointnames%28forrevision%29.md)
  Retrieves the supported joint names for a revision.
- [var supportedJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](./vndetecthumanbodyposerequest/supportedjointsgroupnames.md)
  Retrieves the supported joint group names.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointsGroupName]](./vndetecthumanbodyposerequest/supportedjointsgroupnames%28forrevision%29.md)
  Retrieves the supported joint group names for a revision.
- [- supportedJointNamesAndReturnError:](./vndetecthumanbodyposerequest/supportedjointnamesandreturnerror_.md)
  Retrieves the supported joint names.
- [- supportedJointsGroupNamesAndReturnError:](./vndetecthumanbodyposerequest/supportedjointsgroupnamesandreturnerror_.md)
  Retrieves the supported joint group names.
### Accessing the Results
- [var results: [VNHumanBodyPoseObservation]?](./vndetecthumanbodyposerequest/results.md)
  The observed body poses.
### Identifying Body Pose Revisions
- [var VNDetectHumanBodyPoseRequestRevision1: Int](./vndetecthumanbodyposerequestrevision1.md)
  A constant for specifying revision 1 of the body pose detection request.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Body and hand pose detection
- [Detecting Human Body Poses in Images](./detecting-human-body-poses-in-images.md)
  Add the capability to detect human body poses to your app using the Vision framework.
- [Detecting Hand Poses with Vision](./detecting-hand-poses-with-vision.md)
  Create a virtual drawing app by using Vision’s capability to detect hand poses.
- [class VNDetectHumanHandPoseRequest](./vndetecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [class VNRecognizedPointsObservation](./vnrecognizedpointsobservation.md)
  An observation that provides the points the analysis recognized.
- [class VNHumanBodyPoseObservation](./vnhumanbodyposeobservation.md)
  An observation that provides the body points the analysis recognized.
- [class VNHumanHandPoseObservation](./vnhumanhandposeobservation.md)
  An observation that provides the hand points the analysis recognized.
- [class VNPoint](./vnpoint.md)
  An immutable object that represents a single 2D point in an image.
- [class VNDetectedPoint](./vndetectedpoint.md)
  An object that represents a normalized point in an image, along with a confidence value.
- [class VNRecognizedPoint](./vnrecognizedpoint.md)
  An object that represents a normalized point in an image, along with an identifier label and a confidence value.
- [struct VNRecognizedPointKey](./vnrecognizedpointkey.md)
  The data type for all recognized point keys.
- [struct VNRecognizedPointGroupKey](./vnrecognizedpointgroupkey.md)
  The data type for all recognized-point group keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest)*