# VNDetectHumanBodyPose3DRequest

**Framework**: Vision  
**Kind**: class

A request that detects points on human bodies in 3D space, relative to the camera.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectHumanBodyPose3DRequest
```

## Mentions

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)

#### Overview

This request generates a collection of [`VNHumanBodyPose3DObservation`](vnhumanbodypose3dobservation.md) objects that describe the position of each body the request detects. If the system allows it, the request uses [`AVDepthData`](https://developer.apple.com/documentation/AVFoundation/AVDepthData) information to improve the accuracy.

## Topics

### Initializing a Request
- [init()](vndetecthumanbodypose3drequest/init.md)
  Creates a new request with no completion handler.
- [init(completionHandler: VNRequestCompletionHandler?)](vndetecthumanbodypose3drequest/init(completionhandler:).md)
  Creates a new 3D body pose request with a completion handler.
### Determining Supported Joints
- [var supportedJointsGroupNames: [VNHumanBodyPose3DObservation.JointsGroupName]](vndetecthumanbodypose3drequest/supportedjointsgroupnames.md)
  Returns the joint names the request supports.
- [var supportedJointNames: [VNHumanBodyPose3DObservation.JointName]](vndetecthumanbodypose3drequest/supportedjointnames.md)
  Returns the joint group names the request supports.
### Accessing the Results
- [var results: [VNHumanBodyPose3DObservation]?](vndetecthumanbodypose3drequest/results.md)
  The 3D body pose the request observes.

## Relationships

### Inherits From
- [VNStatefulRequest](vnstatefulrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)
  Detect three-dimensional human body poses using the Vision framework.
- [Detecting human body poses in 3D with Vision](detecting-human-body-poses-in-3d-with-vision.md)
  Render skeletons of 3D body pose points in a scene overlaying the input image.
- [class VNHumanBodyPose3DObservation](vnhumanbodypose3dobservation.md)
  An observation that provides the 3D body points the request recognizes.
- [class VNRecognizedPoints3DObservation](vnrecognizedpoints3dobservation.md)
  An observation that provides the 3D points for a request.
- [class VNHumanBodyRecognizedPoint3D](vnhumanbodyrecognizedpoint3d.md)
  A recognized 3D point that includes a parent joint.
- [class VNPoint3D](vnpoint3d.md)
  An object that represents a 3D point in an image.
- [class VNRecognizedPoint3D](vnrecognizedpoint3d.md)
  A 3D point that includes an identifier to the point.
- [VNHumanBodyPose3DObservation.JointName](vnhumanbodypose3dobservation/jointname.md)
  The joint names for a 3D body pose.
- [VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname.md)
  The joint group names for a 3D body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodypose3drequest)*