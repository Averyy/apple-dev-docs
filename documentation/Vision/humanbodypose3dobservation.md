# HumanBodyPose3DObservation

**Framework**: Vision  
**Kind**: struct

An observation that provides the 3D body points the request recognizes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct HumanBodyPose3DObservation
```

## Topics

### Creating an observation
- [init(VNHumanBodyPose3DObservation)](humanbodypose3dobservation/init(_:).md)
  Creates a 3D human body pose observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let bodyHeight: Measurement<UnitLength>](humanbodypose3dobservation/bodyheight.md)
  The estimated human body height, in meters.
- [let cameraOriginMatrix: simd_float4x4](humanbodypose3dobservation/cameraoriginmatrix.md)
  A transform from the skeleton hip to the camera.
- [HumanBodyPose3DObservation.EstimationTechnique](humanbodypose3dobservation/estimationtechnique.md)
  Constants that identify body height estimation techniques.
- [let heightEstimationTechnique: HumanBodyPose3DObservation.EstimationTechnique](humanbodypose3dobservation/heightestimationtechnique.md)
  The technique the framework uses to estimate body height.
### Getting the joints
- [func allJoints(in: HumanBodyPose3DObservation.JointsGroupName?) -> [HumanBodyPose3DObservation.JointName : Joint3D]](humanbodypose3dobservation/alljoints(in:).md)
  Retrieves a dictionary of all joints in a joint group.
- [var availableJointsGroupNames: [HumanBodyPose3DObservation.JointsGroupName]](humanbodypose3dobservation/availablejointsgroupnames.md)
  The names of the available joint groupings in the observation.
- [HumanBodyPose3DObservation.JointsGroupName](humanbodypose3dobservation/jointsgroupname.md)
  The supported joint group names for the body pose.
- [func joint(for: HumanBodyPose3DObservation.JointName) -> Joint3D?](humanbodypose3dobservation/joint(for:).md)
  Retrieves a joint for a given joint name.
- [var availableJointNames: [HumanBodyPose3DObservation.JointName]](humanbodypose3dobservation/availablejointnames.md)
  The names of the available joints in the observation.
- [HumanBodyPose3DObservation.JointName](humanbodypose3dobservation/jointname.md)
  The supported joint names for the body pose.
### Getting the joint name
- [func parentJointName(for: HumanBodyPose3DObservation.JointName) -> HumanBodyPose3DObservation.JointName](humanbodypose3dobservation/parentjointname(for:).md)
  Returns the parent joint of the joint name you specify.
### Getting the camera position
- [func cameraRelativePosition(for: HumanBodyPose3DObservation.JointName) -> simd_float4x4](humanbodypose3dobservation/camerarelativeposition(for:).md)
  Returns a position relative to the camera for the body joint you specify.
### Getting the joint position
- [func pointInImage(for: HumanBodyPose3DObservation.JointName) -> NormalizedPoint](humanbodypose3dobservation/pointinimage(for:).md)
  Returns a 2D point for the joint name you specify, relative to the input image.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)

## See Also

- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation)*