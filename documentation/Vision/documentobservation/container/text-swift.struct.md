# DocumentObservation.Container.Text

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A structure that represents a region of text in a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Text
```

## Topics

### Accessing the text
- [var detectedData: [DocumentObservation.Container.DataDetectorMatch]](./text-swift.struct/detecteddata.md)
  Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.
- [var lines: [RecognizedTextObservation]](./text-swift.struct/lines.md)
  The text grouped by line.
- [var transcript: String](./text-swift.struct/transcript.md)
  The complete text as a string.
- [var words: [RecognizedTextObservation]?](./text-swift.struct/words.md)
  An instance property that returns individual words in a text container.
### Inspecting the text
- [var boundingRegion: NormalizedRegion](./text-swift.struct/boundingregion.md)
  A polygon that defines the boundary of text.
- [var textAlignment: DocumentObservation.Container.Text.Alignment?](./text-swift.struct/textalignment.md)
  The alignment of the text within its container.
- [DocumentObservation.Container.Text.Alignment](./text-swift.struct/alignment.md)
  The different text alignment types within a container.
### Getting the bounding region
- [func boundingRegion(for: Range<String.Index>) -> NormalizedRegion?](./text-swift.struct/boundingregion%28for%29.md)
  Calculates a bounding region around the range of characters within a string.

## Relationships

### Conforms To
- [BoundingRegionProviding](../../boundingregionproviding.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the sections in a document
- [DocumentObservation.Container.List](./list.md)
  A structure that represents a list of items within a document.
- [DocumentObservation.Container.Table](./table.md)
  A structure that represents a table within a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/text-swift.struct)*