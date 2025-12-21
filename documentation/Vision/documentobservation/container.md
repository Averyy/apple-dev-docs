# DocumentObservation.Container

**Framework**: Vision  
**Kind**: struct

A region of content recognized in a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Container
```

## Topics

### Getting the sections in a document
- [DocumentObservation.Container.List](documentobservation/container/list.md)
  A structure that represents a list of items within a document.
- [DocumentObservation.Container.Table](documentobservation/container/table.md)
  A structure that represents a table within a document.
- [DocumentObservation.Container.Text](documentobservation/container/text-swift.struct.md)
  A structure that represents a region of text in a document.
### Accessing specific content within a document
- [DocumentObservation.Container.DataDetectorMatch](documentobservation/container/datadetectormatch.md)
  Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.
- [var barcodes: [BarcodeObservation]](documentobservation/container/barcodes.md)
  The machine-readable codes found within the container.
- [var lists: [DocumentObservation.Container.List]](documentobservation/container/lists.md)
  The lists found within the container.
- [var paragraphs: [DocumentObservation.Container.Text]](documentobservation/container/paragraphs.md)
  The document’s extracted text, grouped into paragraphs within the container.
- [var tables: [DocumentObservation.Container.Table]](documentobservation/container/tables.md)
  The tables found within the container.
- [var text: DocumentObservation.Container.Text](documentobservation/container/text-swift.property.md)
  All the text found within the container.
- [var title: DocumentObservation.Container.Text?](documentobservation/container/title.md)
  The title found within the container.

## Relationships

### Conforms To
- [BoundingRegionProviding](boundingregionproviding.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container)*