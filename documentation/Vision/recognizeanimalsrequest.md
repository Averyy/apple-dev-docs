# RecognizeAnimalsRequest

**Framework**: Vision  
**Kind**: struct

A request that recognizes animals in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct RecognizeAnimalsRequest
```

#### Overview

This request generates a collection of [`RecognizedObjectObservation`](recognizedobjectobservation.md) objects that describe the animals the request detects.

## Topics

### Creating a request
- [init(RecognizeAnimalsRequest.Revision?)](recognizeanimalsrequest/init(_:).md)
  Creates an animal-recognition request.
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
- [struct RecognizedObjectObservation](recognizedobjectobservation.md)
  An observation with an array of classification labels that classify the recognized object.
### Configuring a request
- [var supportedAnimals: [RecognizeAnimalsRequest.Animal]](recognizeanimalsrequest/supportedanimals.md)
  The collection of animals that the request can detect.
- [RecognizeAnimalsRequest.Animal](recognizeanimalsrequest/animal.md)
  An identifier for a recognizable animal.
### Getting the revision
- [let revision: RecognizeAnimalsRequest.Revision](recognizeanimalsrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [RecognizeAnimalsRequest.Revision]](recognizeanimalsrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [RecognizeAnimalsRequest.Revision](recognizeanimalsrequest/revision-swift.enum.md)
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
- [struct ClassifyImageRequest](classifyimagerequest.md)
  A request to classify an image.
- [struct DetectHumanRectanglesRequest](detecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizeanimalsrequest)*