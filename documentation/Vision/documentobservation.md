# DocumentObservation

**Framework**: Vision  
**Kind**: struct

Information about the sections of content that an image-analysis request detects in a document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DocumentObservation
```

#### Overview

The observation allows you to access a document’s content and group it within different sections. An observation is the result of using a [`RecognizeDocumentsRequest`](recognizedocumentsrequest.md) to process an image of a document and detects the content within that document using a container. Each container provides access to any text, lists, barcodes, or any other detected data that appears within the region of the container.

## Topics

### Inspecting an observation
- [let uuid: UUID](documentobservation/uuid.md)
  A unique alphanumeric value that the framework assigns to the observation.
- [let confidence: Float](documentobservation/confidence.md)
  The level of confidence in the observation’s accuracy.
- [let document: DocumentObservation.Container](documentobservation/document.md)
  The contents of the document.
- [let timeRange: CMTimeRange?](documentobservation/timerange.md)
  Time in a video frame where the observation was detected.
### Getting the recognized text
- [DocumentObservation.Container](documentobservation/container.md)
  A region of content recognized in a document.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)

## See Also

- [Recognizing tables within a document](recognize-tables-within-a-document.md)
  Scan a document containing a contact table and extract the content within the table in a formatted way.
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [struct RecognizeDocumentsRequest](recognizedocumentsrequest.md)
  An image-analysis request to scan an image of a document and provide information about its structure.
- [struct DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.
- [struct RecognizeTextRequest](recognizetextrequest.md)
  An image-analysis request that recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation)*