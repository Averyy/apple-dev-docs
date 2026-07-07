# DetectAnimalBodyPoseRequest

**Framework**: Vision  
**Kind**: struct

A request that detects an animal body pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectAnimalBodyPoseRequest
```

#### Overview

This request generates a collection of [`AnimalBodyPoseObservation`](animalbodyposeobservation.md) objects that describe the position of each animal the request detects.

## Topics

### Creating a request
- [init(DetectAnimalBodyPoseRequest.Revision?)](detectanimalbodyposerequest/init(_:).md)
  Creates an animal body pose-detection request.
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
- [struct AnimalBodyPoseObservation](animalbodyposeobservation.md)
  An observation that provides the animal body points the analysis recognizes.
### Configuring a request
- [var supportedJointNames: [AnimalBodyPoseObservation.JointName]](detectanimalbodyposerequest/supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [AnimalBodyPoseObservation.JointsGroupName]](detectanimalbodyposerequest/supportedjointsgroupnames.md)
  The joint group names the request supports.
### Getting the revision
- [let revision: DetectAnimalBodyPoseRequest.Revision](detectanimalbodyposerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectAnimalBodyPoseRequest.Revision]](detectanimalbodyposerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectAnimalBodyPoseRequest.Revision](detectanimalbodyposerequest/revision-swift.enum.md)
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

- [class DetectHumanBodyPose3DRequest](detecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.
- [struct DetectHumanBodyPoseRequest](detecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [struct DetectHumanHandPoseRequest](detecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [Supporting Pose Types](supporting-pose-types.md)
  Types you use when working with pose analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectanimalbodyposerequest)*