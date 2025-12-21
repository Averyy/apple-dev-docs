# ClassifyImageRequest

**Framework**: Vision  
**Kind**: struct

A request to classify an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ClassifyImageRequest
```

#### Overview

This type of request produces a collection of [`ClassificationObservation`](classificationobservation.md) objects that describe an image. Access the possible classifications through the [`supportedIdentifiers`](classifyimagerequest/supportedidentifiers.md) property.

```swift
if let imageURL = Bundle.main.url(forResource: "ClassificationImage",
                                      withExtension: "jpg") {
    do {
        let request = ClassifyImageRequest()
        let results = try await request.perform(on: imageURL)
        for classification in results {
            print("Classified \(classification.identifier)")
        }
    } catch {
        print("Encountered an error when performing the request: \(error.localizedDescription)")
    }
}
```

## Topics

### Creating a request
- [init(ClassifyImageRequest.Revision?)](classifyimagerequest/init(_:).md)
  Creates an image-classifier request.
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
- [struct ClassificationObservation](classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
### Configuring a request
- [var cropAndScaleAction: ImageCropAndScaleAction](classifyimagerequest/cropandscaleaction.md)
  An optional setting that tells the algorithm how to scale an input image before generating the result.
- [enum ImageCropAndScaleAction](imagecropandscaleaction.md)
  A scale to apply to an input image before performing a request.
- [var supportedIdentifiers: [String]](classifyimagerequest/supportedidentifiers.md)
  The classification identifiers the request supports.
### Getting the revision
- [let revision: ClassifyImageRequest.Revision](classifyimagerequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [ClassifyImageRequest.Revision]](classifyimagerequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [ClassifyImageRequest.Revision](classifyimagerequest/revision-swift.enum.md)
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

- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [struct DetectHumanRectanglesRequest](detecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.
- [struct RecognizeAnimalsRequest](recognizeanimalsrequest.md)
  A request that recognizes animals in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/classifyimagerequest)*