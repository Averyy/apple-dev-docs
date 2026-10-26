# VNDetectHumanBodyPose3DRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNDetectHumanBodyPose3DRequest : VNStatefulRequest
```

## Mentions

- [Identifying 3D human body poses in images](./identifying-3d-human-body-poses-in-images.md)

#### Overview

This request generates a collection of [`VNHumanBodyPose3DObservation`](./vnhumanbodypose3dobservation.md) objects that describe the position of each body the request detects. If the system allows it, the request uses [`AVDepthData`](../AVFoundation/avdepthdata.md) information to improve the accuracy.

## Topics

### Initializing a Request
- [init()](./vndetecthumanbodypose3drequest/init%28%29.md)
  Creates a new request with no completion handler.
- [init(completionHandler: VNRequestCompletionHandler?)](./vndetecthumanbodypose3drequest/init%28completionhandler%29.md)
  Creates a new 3D body pose request with a completion handler.
### Determining Supported Joints
- [var supportedJointsGroupNames: [VNHumanBodyPose3DObservation.JointsGroupName]](./vndetecthumanbodypose3drequest/supportedjointsgroupnames.md)
  Returns the joint names the request supports.
- [var supportedJointNames: [VNHumanBodyPose3DObservation.JointName]](./vndetecthumanbodypose3drequest/supportedjointnames.md)
  Returns the joint group names the request supports.
- [- supportedJointNamesAndReturnError:](./vndetecthumanbodypose3drequest/supportedjointnamesandreturnerror_.md)
  Returns the joint names the request supports.
- [- supportedJointsGroupNamesAndReturnError:](./vndetecthumanbodypose3drequest/supportedjointsgroupnamesandreturnerror_.md)
  Returns the joint group names the request supports.
### Accessing the Results
- [var results: [VNHumanBodyPose3DObservation]?](./vndetecthumanbodypose3drequest/results.md)
  The 3D body pose the request observes.

## Relationships

### Inherits From
- [VNStatefulRequest](./vnstatefulrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### 3D body pose detection
- [Identifying 3D human body poses in images](./identifying-3d-human-body-poses-in-images.md)
  Detect three-dimensional human body poses using the Vision framework.
- [Detecting human body poses in 3D with Vision](./detecting-human-body-poses-in-3d-with-vision.md)
  Render skeletons of 3D body pose points in a scene overlaying the input image.
- [class VNHumanBodyPose3DObservation](./vnhumanbodypose3dobservation.md)
  An observation that provides the 3D body points the request recognizes.
- [class VNRecognizedPoints3DObservation](./vnrecognizedpoints3dobservation.md)
  An observation that provides the 3D points for a request.
- [class VNHumanBodyRecognizedPoint3D](./vnhumanbodyrecognizedpoint3d.md)
  A recognized 3D point that includes a parent joint.
- [class VNPoint3D](./vnpoint3d.md)
  An object that represents a 3D point in an image.
- [class VNRecognizedPoint3D](./vnrecognizedpoint3d.md)
  A 3D point that includes an identifier to the point.
- [VNHumanBodyPose3DObservation.JointName](./vnhumanbodypose3dobservation/jointname.md)
  The joint names for a 3D body pose.
- [VNHumanBodyPose3DObservation.JointsGroupName](./vnhumanbodypose3dobservation/jointsgroupname.md)
  The joint group names for a 3D body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodypose3drequest)*