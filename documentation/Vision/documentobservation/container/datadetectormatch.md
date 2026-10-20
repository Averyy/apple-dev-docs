# DocumentObservation.Container.DataDetectorMatch

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DataDetectorMatch
```

## Topics

### Getting the detected data
- [var match: DataDetector.Match](./datadetectormatch/match.md)
  The details of the data detected.

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

### Accessing specific content within a document
- [var barcodes: [BarcodeObservation]](./barcodes.md)
  The machine-readable codes found within the container.
- [var lists: [DocumentObservation.Container.List]](./lists.md)
  The lists found within the container.
- [var paragraphs: [DocumentObservation.Container.Text]](./paragraphs.md)
  The document’s extracted text, grouped into paragraphs within the container.
- [var tables: [DocumentObservation.Container.Table]](./tables.md)
  The tables found within the container.
- [var text: DocumentObservation.Container.Text](./text-swift.property.md)
  All the text found within the container.
- [var title: DocumentObservation.Container.Text?](./title.md)
  The title found within the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/datadetectormatch)*