# text

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

All the text found within the container.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var text: DocumentObservation.Container.Text { get }
```

## See Also

### Accessing specific content within a document
- [DocumentObservation.Container.DataDetectorMatch](./datadetectormatch.md)
  Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.
- [var barcodes: [BarcodeObservation]](./barcodes.md)
  The machine-readable codes found within the container.
- [var lists: [DocumentObservation.Container.List]](./lists.md)
  The lists found within the container.
- [var paragraphs: [DocumentObservation.Container.Text]](./paragraphs.md)
  The document’s extracted text, grouped into paragraphs within the container.
- [var tables: [DocumentObservation.Container.Table]](./tables.md)
  The tables found within the container.
- [var title: DocumentObservation.Container.Text?](./title.md)
  The title found within the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/text-swift.property)*