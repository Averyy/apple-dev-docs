# detectedData

**Framework**: Vision  
**Kind**: property

Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var detectedData: [DocumentObservation.Container.DataDetectorMatch] { get }
```

#### Discussion

This is a computed property that may be computationally expensive for large text regions.

## See Also

- [var lines: [RecognizedTextObservation]](documentobservation/container/text-swift.struct/lines.md)
  The text grouped by line.
- [var transcript: String](documentobservation/container/text-swift.struct/transcript.md)
  The complete text as a string.
- [var words: [RecognizedTextObservation]?](documentobservation/container/text-swift.struct/words.md)
  An instance property that returns individual words in a text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/text-swift.struct/detecteddata)*