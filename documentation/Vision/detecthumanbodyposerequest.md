# DetectHumanBodyPoseRequest

**Framework**: Vision  
**Kind**: struct

A request that detects a human body pose.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectHumanBodyPoseRequest
```

#### Overview

This type of request produces a collection of [`HumanBodyPoseObservation`](humanbodyposeobservation.md) objects that describe the body pose.

## Topics

### Creating a request
- [init(DetectHumanBodyPoseRequest.Revision?)](detecthumanbodyposerequest/init(_:).md)
  Creates a human body pose request.
### Getting the revision
- [let revision: DetectHumanBodyPoseRequest.Revision](detecthumanbodyposerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectHumanBodyPoseRequest.Revision]](detecthumanbodyposerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectHumanBodyPoseRequest.Revision](detecthumanbodyposerequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var detectsHands: Bool](detecthumanbodyposerequest/detectshands.md)
  A Boolean value that detects hands of the body in the results, if they’re visible.
- [var supportedJointNames: [HumanBodyPoseObservation.JointName]](detecthumanbodyposerequest/supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [HumanBodyPoseObservation.JointsGroupName]](detecthumanbodyposerequest/supportedjointsgroupnames.md)
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
- [struct HumanBodyPoseObservation](humanbodyposeobservation.md)
  An observation that provides the body points the analysis recognizes.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [VisionRequest](visionrequest.md)

## See Also

- [struct DetectHumanHandPoseRequest](detecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [protocol PoseProviding](poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [enum Chirality](chirality.md)
  The hand sidedness of a pose.
- [struct Joint](joint.md)
  A pose joint represented as a normalized point in an image, along with a label and a confidence value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanbodyposerequest)*