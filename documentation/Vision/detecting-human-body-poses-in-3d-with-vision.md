# Detecting human body poses in 3D with Vision

**Framework**: Vision

Render skeletons of 3D body pose points in a scene overlaying the input image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Xcode 15.0+

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 111241: [`Explore 3D body pose and person segmentation in Vision`](https://developer.apple.comhttps://developer.apple.com/wwdc23/111241/).

This sample code project is associated with WWDC23 session 111241: [`Explore 3D body pose and person segmentation in Vision`](https://developer.apple.comhttps://developer.apple.com/wwdc23/111241/).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode, ensure you’re using an iOS device with an A12 chip or later. The input image should have all limbs of the subject visible.

> **Note**: Due to a behavior change with `cameraOriginMatrix` API, if this sample project is run on a device on a build earlier than beta 3, camera position will be rotated 180 degrees.

Due to a behavior change with `cameraOriginMatrix` API, if this sample project is run on a device on a build earlier than beta 3, camera position will be rotated 180 degrees.

## See Also

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)
  Detect three-dimensional human body poses using the Vision framework.
- [class VNDetectHumanBodyPose3DRequest](vndetecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecting-human-body-poses-in-3d-with-vision)*