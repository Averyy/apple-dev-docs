# TrackTranslationalImageRegistrationRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that you track over time to determine the affine transform necessary to align the content of two images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class TrackTranslationalImageRegistrationRequest
```

#### Overview

This request generates an [`ImageTranslationAlignmentObservation`](imagetranslationalignmentobservation.md) object that describes the transform data the request detects.

## Topics

### Creating a request
- [init(TrackTranslationalImageRegistrationRequest.Revision?, frameAnalysisSpacing: CMTime?)](tracktranslationalimageregistrationrequest/init(_:frameanalysisspacing:).md)
  Creates an image-alignment tracking request to determine the affine transform.
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
- [struct ImageTranslationAlignmentObservation](imagetranslationalignmentobservation.md)
  Affine transform information that an image-alignment request produces.
### Configuring a request
- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.
### Getting the revision
- [let revision: TrackTranslationalImageRegistrationRequest.Revision](tracktranslationalimageregistrationrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [TrackTranslationalImageRegistrationRequest.Revision]](tracktranslationalimageregistrationrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [TrackTranslationalImageRegistrationRequest.Revision](tracktranslationalimageregistrationrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StatefulRequest](statefulrequest.md)
- [TargetedRequest](targetedrequest.md)
- [VisionRequest](visionrequest.md)

## See Also

- [struct GenerateImageFeaturePrintRequest](generateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.
- [class TrackHomographicImageRegistrationRequest](trackhomographicimageregistrationrequest.md)
  An image-analysis request that you track over time to determine the perspective warp matrix necessary to align the content of two images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/tracktranslationalimageregistrationrequest)*