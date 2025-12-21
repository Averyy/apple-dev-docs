# words

**Framework**: Vision  
**Kind**: property

An instance property that returns individual words in a text container.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var words: [RecognizedTextObservation]? { get }
```

#### Discussion

Chinese, Japanese, Korean, and Thai don’t recognize individual words.

## See Also

- [var detectedData: [DocumentObservation.Container.DataDetectorMatch]](documentobservation/container/text-swift.struct/detecteddata.md)
  Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.
- [var lines: [RecognizedTextObservation]](documentobservation/container/text-swift.struct/lines.md)
  The text grouped by line.
- [var transcript: String](documentobservation/container/text-swift.struct/transcript.md)
  The complete text as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/text-swift.struct/words)*