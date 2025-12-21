# DetectBarcodesRequest

**Framework**: Vision  
**Kind**: struct

A request that detects barcodes in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DetectBarcodesRequest
```

#### Overview

This request generates a collection of [`BarcodeObservation`](barcodeobservation.md) objects that describe each barcode the request detects.

## Topics

### Creating a request
- [init(DetectBarcodesRequest.Revision?)](detectbarcodesrequest/init(_:).md)
  Creates a barcode-detection request.
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
- [struct BarcodeObservation](barcodeobservation.md)
  An object that represents barcode information that an image-analysis request detects.
### Configuring a request
- [var symbologies: [BarcodeSymbology]](detectbarcodesrequest/symbologies.md)
  The barcode symbologies that the request detects in an image.
- [var supportedSymbologies: [BarcodeSymbology]](detectbarcodesrequest/supportedsymbologies.md)
  The collection of barcode symbologies that the request can recognize.
- [enum BarcodeSymbology](barcodesymbology.md)
  The barcode symbologies that the framework detects.
- [var coalescesCompositeSymbologies: Bool](detectbarcodesrequest/coalescescompositesymbologies.md)
  A Boolean value that indicates whether the request coalesces multiple codes into one.
### Getting the revision
- [let revision: DetectBarcodesRequest.Revision](detectbarcodesrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectBarcodesRequest.Revision]](detectbarcodesrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [DetectBarcodesRequest.Revision](detectbarcodesrequest/revision-swift.enum.md)
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

- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [Recognizing tables within a document](recognize-tables-within-a-document.md)
  Scan a document that contains a table and extract its content in a formatted way.
- [struct DetectDocumentSegmentationRequest](detectdocumentsegmentationrequest.md)
  A request that detects rectangular regions that contain text in the input image.
- [struct DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.
- [struct RecognizeDocumentsRequest](recognizedocumentsrequest.md)
  An image-analysis request to scan an image of a document and provide information about its structure.
- [struct RecognizeTextRequest](recognizetextrequest.md)
  An image-analysis request that recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectbarcodesrequest)*