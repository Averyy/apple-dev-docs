# GeneratePersonSegmentationRequest

**Framework**: Vision  
**Kind**: class

A request that produces a matte image for a person it finds in the input image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class GeneratePersonSegmentationRequest
```

#### Overview

Perform this request to detect and generate an image mask for a person in an image. The request returns the resulting image mask in an instance of [`PixelBufferObservation`](pixelbufferobservation.md).

## Topics

### Creating a request
- [init(GeneratePersonSegmentationRequest.Revision?, frameAnalysisSpacing: CMTime?)](generatepersonsegmentationrequest/init(_:frameanalysisspacing:).md)
  Creates a person-segmentation request.
### Getting the revision
- [let revision: GeneratePersonSegmentationRequest.Revision](generatepersonsegmentationrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [GeneratePersonSegmentationRequest.Revision]](generatepersonsegmentationrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [GeneratePersonSegmentationRequest.Revision](generatepersonsegmentationrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var qualityLevel: GeneratePersonSegmentationRequest.QualityLevel](generatepersonsegmentationrequest/qualitylevel-swift.property.md)
  A value that indicates how the request balances accuracy and performance.
- [GeneratePersonSegmentationRequest.QualityLevel](generatepersonsegmentationrequest/qualitylevel-swift.enum.md)
  Constants that define the levels of quality for a person-segmentation request.
- [var outputPixelFormatType: OSType](generatepersonsegmentationrequest/outputpixelformattype.md)
  The desired pixel format of the observation.
- [var supportedOutputPixelFormats: [OSType]](generatepersonsegmentationrequest/supportedoutputpixelformats.md)
  The collection of supported pixel format types.
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
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.

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

- [struct GeneratePersonInstanceMaskRequest](generatepersoninstancemaskrequest.md)
  A request that produces a mask of individual people it finds in the input image.
- [struct DetectDocumentSegmentationRequest](detectdocumentsegmentationrequest.md)
  A request that detects rectangular regions that contain text in the input image.
- [protocol StatefulRequest](statefulrequest.md)
  The protocol for a type that builds evidence of a condition over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generatepersonsegmentationrequest)*