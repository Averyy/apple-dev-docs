# DetectHumanHandPoseRequest

**Framework**: Vision  
**Kind**: struct

A request that detects a human hand pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectHumanHandPoseRequest
```

#### Overview

This type of request produces a collection of [`HumanHandPoseObservation`](humanhandposeobservation.md) objects that describe the hand pose.

## Topics

### Creating a request
- [init(DetectHumanHandPoseRequest.Revision?)](detecthumanhandposerequest/init(_:).md)
  Creates a human hand pose detection request.
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
### Understanding the result
- [struct HumanHandPoseObservation](humanhandposeobservation.md)
  An observation that provides the hand points the analysis recognizes.
### Configuring a request
- [var maximumHandCount: Int](detecthumanhandposerequest/maximumhandcount.md)
  The maximum number of hands to detect in an image.
- [var supportedJointNames: [HumanHandPoseObservation.JointName]](detecthumanhandposerequest/supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [HumanHandPoseObservation.JointsGroupName]](detecthumanhandposerequest/supportedjointsgroupnames.md)
  The joint group names the request supports.
### Getting the revision
- [let revision: DetectHumanHandPoseRequest.Revision](detecthumanhandposerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectHumanHandPoseRequest.Revision]](detecthumanhandposerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectHumanHandPoseRequest.Revision](detecthumanhandposerequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionRequest](visionrequest.md)

## See Also

- [struct DetectAnimalBodyPoseRequest](detectanimalbodyposerequest.md)
  A request that detects an animal body pose.
- [class DetectHumanBodyPose3DRequest](detecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.
- [struct DetectHumanBodyPoseRequest](detecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [Supporting Pose Types](supporting-pose-types.md)
  Types you use when working with pose analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanhandposerequest)*