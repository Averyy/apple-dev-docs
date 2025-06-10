# RecognizeDocumentsRequest

**Framework**: Vision  
**Kind**: struct

An image-analysis request to scan an image of a document and provide information about its structure.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct RecognizeDocumentsRequest
```

#### Overview

This request scans a document and extracts different groups of text and barcodes within the document image. Use this request to understand different types of structured texts like receipts, nutritional labels, textbook pages, forms, or other documents that you want to understand in further detail.

The request generates a [`DocumentObservation`](documentobservation.md) array, which allows you to access your chosen document’s structure grouped by words, lines, or paragraphs. You can also access tables and lists that appear in the document.

## Topics

### Creating a request
- [init(RecognizeDocumentsRequest.Revision?)](recognizedocumentsrequest/init(_:).md)
  Creates a document content recognition request.
### Getting the revision
- [let revision: RecognizeDocumentsRequest.Revision](recognizedocumentsrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [RecognizeDocumentsRequest.Revision]](recognizedocumentsrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [RecognizeDocumentsRequest.Revision](recognizedocumentsrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [RecognizeDocumentsRequest.BarcodeDetectionOptions](recognizedocumentsrequest/barcodedetectionoptions-swift.struct.md)
  A configuration object for detecting barcodes in a document.
- [RecognizeDocumentsRequest.TextRecognitionOptions](recognizedocumentsrequest/textrecognitionoptions-swift.struct.md)
  A configuration object for detected and recognized text within the document.
- [var barcodeDetectionOptions: RecognizeDocumentsRequest.BarcodeDetectionOptions](recognizedocumentsrequest/barcodedetectionoptions-swift.property.md)
  A configuration object for detecting barcodes in a document.
- [var textRecognitionOptions: RecognizeDocumentsRequest.TextRecognitionOptions](recognizedocumentsrequest/textrecognitionoptions-swift.property.md)
  A configuration object for detected and recognized text within the document.
- [var supportedBarcodeSymbologies: [BarcodeSymbology]](recognizedocumentsrequest/supportedbarcodesymbologies.md)
  The collection of barcode symbologies recognized by the request.
- [var supportedRecognitionLanguages: [Locale.Language]](recognizedocumentsrequest/supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.

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

- [Recognizing tables within a document](recognize-tables-within-a-document.md)
  Scan a document containing a contact table and extract the content within the table in a formatted way.
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [struct DocumentObservation](documentobservation.md)
  Information about the sections of content that an image-analysis request detects in a document.
- [struct DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.
- [struct RecognizeTextRequest](recognizetextrequest.md)
  An image-analysis request that recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest)*