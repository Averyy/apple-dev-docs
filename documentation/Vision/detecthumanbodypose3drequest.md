# DetectHumanBodyPose3DRequest

**Framework**: Vision  
**Kind**: class

A request that detects points on human bodies in 3D space, relative to the camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class DetectHumanBodyPose3DRequest
```

#### Overview

This request generates a collection of [`HumanBodyPose3DObservation`](humanbodypose3dobservation.md) objects that describe the position of each body the request detects. If the system allows it, the request uses [`AVDepthData`](https://developer.apple.com/documentation/AVFoundation/AVDepthData) information to improve the accuracy.

## Topics

### Creating a request
- [init(DetectHumanBodyPose3DRequest.Revision?, frameAnalysisSpacing: CMTime?)](detecthumanbodypose3drequest/init(_:frameanalysisspacing:).md)
  Creates a 3D human body pose request.
### Getting the revision
- [let revision: DetectHumanBodyPose3DRequest.Revision](detecthumanbodypose3drequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectHumanBodyPose3DRequest.Revision]](detecthumanbodypose3drequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectHumanBodyPose3DRequest.Revision](detecthumanbodypose3drequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var supportedJointNames: [HumanBodyPose3DObservation.JointName]](detecthumanbodypose3drequest/supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [HumanBodyPose3DObservation.JointsGroupName]](detecthumanbodypose3drequest/supportedjointsgroupnames.md)
  The joint group names the request supports.
### Performing a request
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
- [struct HumanBodyPose3DObservation](humanbodypose3dobservation.md)
  An observation that provides the 3D body points the request recognizes.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [StatefulRequest](statefulrequest.md)
- [VisionRequest](visionrequest.md)

## See Also

- [struct Joint3D](joint3d.md)
  An object that represents a body pose joint in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanbodypose3drequest)*