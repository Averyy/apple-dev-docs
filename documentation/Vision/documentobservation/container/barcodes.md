# barcodes

**Framework**: Vision  
**Kind**: property

The machine-readable codes found within the container.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var barcodes: [BarcodeObservation] { get }
```

#### Discussion

Vision recognizes 20 different barcode types; to see the specific codes you can use [`supportedBarcodeSymbologies`](recognizedocumentsrequest/supportedbarcodesymbologies.md). To see this value, set [`enabled`](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/enabled.md) within [`RecognizeDocumentsRequest.BarcodeDetectionOptions`](recognizedocumentsrequest/barcodedetectionoptions-swift.struct.md) to `true`.

## See Also

- [DocumentObservation.Container.DataDetectorMatch](documentobservation/container/datadetectormatch.md)
  Detected content in the document matched to a specific type of data, such as emails, phone numbers, addresses, and so on.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/barcodes)*