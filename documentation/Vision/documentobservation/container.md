# DocumentObservation.Container

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A region of content recognized in a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Container
```

## Topics

### Getting the sections in a document
- [DocumentObservation.Container.List](./container/list.md)
  A structure that represents a list of items within a document.
- [DocumentObservation.Container.Table](./container/table.md)
  A structure that represents a table within a document.
- [DocumentObservation.Container.Text](./container/text-swift.struct.md)
  A structure that represents a region of text in a document.
### Accessing specific content within a document
- [DocumentObservation.Container.DataDetectorMatch](./container/datadetectormatch.md)
  Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.
- [var barcodes: [BarcodeObservation]](./container/barcodes.md)
  The machine-readable codes found within the container.
- [var lists: [DocumentObservation.Container.List]](./container/lists.md)
  The lists found within the container.
- [var paragraphs: [DocumentObservation.Container.Text]](./container/paragraphs.md)
  The document’s extracted text, grouped into paragraphs within the container.
- [var tables: [DocumentObservation.Container.Table]](./container/tables.md)
  The tables found within the container.
- [var text: DocumentObservation.Container.Text](./container/text-swift.property.md)
  All the text found within the container.
- [var title: DocumentObservation.Container.Text?](./container/title.md)
  The title found within the container.

## Relationships

### Conforms To
- [BoundingRegionProviding](../boundingregionproviding.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container)*