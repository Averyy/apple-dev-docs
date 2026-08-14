# RecognizedText

**Framework**: Vision  
**Kind**: struct

Text recognized in an image through a text recognition request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct RecognizedText
```

## Topics

### Getting the bounding box
- [func boundingBox(for: Range<String.Index>) -> RectangleObservation?](recognizedtext/boundingbox(for:).md)
  Calculates the bounding box around the characters in the range of a string.
### Inspecting the recognized text
- [var string: String](recognizedtext/string.md)
  The top candidate for recognized text.
- [var confidence: Float](recognizedtext/confidence.md)
  A normalized confidence score for the text recognition result.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func topCandidates(Int) -> [RecognizedText]](recognizedtextobservation/topcandidates(_:).md)
  Requests the top candidates for a recognized text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtext)*