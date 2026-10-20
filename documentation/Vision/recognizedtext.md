# RecognizedText

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

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
- [func boundingBox(for: Range<String.Index>) -> RectangleObservation?](./recognizedtext/boundingbox%28for%29.md)
  Calculates the bounding box around the characters in the range of a string.
### Inspecting the recognized text
- [var string: String](./recognizedtext/string.md)
  The top candidate for recognized text.
- [var confidence: Float](./recognizedtext/confidence.md)
  A normalized confidence score for the text recognition result.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the recognized text
- [func topCandidates(Int) -> [RecognizedText]](./recognizedtextobservation/topcandidates%28_%29.md)
  Requests the top candidates for a recognized text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtext)*