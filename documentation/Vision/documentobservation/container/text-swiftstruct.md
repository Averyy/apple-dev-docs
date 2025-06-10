# DocumentObservation.Container.Text

**Framework**: Vision  
**Kind**: struct

A structure that represents a region of text in a document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Text
```

## Topics

### Accessing the text
- [var detectedData: [DocumentObservation.Container.DataDetectorMatch]](documentobservation/container/text-swift.struct/detecteddata.md)
  Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.
- [var lines: [RecognizedTextObservation]](documentobservation/container/text-swift.struct/lines.md)
  The text grouped by line.
- [var transcript: String](documentobservation/container/text-swift.struct/transcript.md)
  The complete text as a string.
- [var words: [RecognizedTextObservation]?](documentobservation/container/text-swift.struct/words.md)
  An instance property that returns individual words in a text container.
### Inspecting the text
- [var boundingRegion: NormalizedRegion](documentobservation/container/text-swift.struct/boundingregion.md)
  A polygon that defines the boundary of text.
- [var textAlignment: DocumentObservation.Container.Text.Alignment?](documentobservation/container/text-swift.struct/textalignment.md)
  The alignment of the text within its container.
- [DocumentObservation.Container.Text.Alignment](documentobservation/container/text-swift.struct/alignment.md)
  The different text alignment types within a container.
### Getting the bounding region
- [func boundingRegion(for: Range<String.Index>) -> NormalizedRegion?](documentobservation/container/text-swift.struct/boundingregion(for:).md)
  Calculates a bounding region around the range of characters within a string.

## Relationships

### Conforms To
- [BoundingRegionProviding](boundingregionproviding.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DocumentObservation.Container.List](documentobservation/container/list.md)
  A structure that represents a list of items within a document.
- [DocumentObservation.Container.Table](documentobservation/container/table.md)
  A structure that represents a table within a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/text-swift.struct)*