# DetectAnimalBodyPoseRequest

**Framework**: Vision  
**Kind**: struct

A request that detects an animal body pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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
### Getting the revision
- [let revision: DetectAnimalBodyPoseRequest.Revision](detectanimalbodyposerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectAnimalBodyPoseRequest.Revision]](detectanimalbodyposerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectAnimalBodyPoseRequest.Revision](detectanimalbodyposerequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var supportedJointNames: [AnimalBodyPoseObservation.JointName]](detectanimalbodyposerequest/supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [AnimalBodyPoseObservation.JointsGroupName]](detectanimalbodyposerequest/supportedjointsgroupnames.md)
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
- [struct AnimalBodyPoseObservation](animalbodyposeobservation.md)
  An observation that provides the animal body points the analysis recognizes.

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

- [struct RecognizeAnimalsRequest](recognizeanimalsrequest.md)
  A request that recognizes animals in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectanimalbodyposerequest)*