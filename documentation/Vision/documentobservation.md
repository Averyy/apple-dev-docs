# DocumentObservation

**Framework**: Vision  
**Kind**: struct

Information about the sections of content that an image-analysis request detects in a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation)*