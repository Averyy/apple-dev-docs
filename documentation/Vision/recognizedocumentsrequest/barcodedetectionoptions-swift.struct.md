# RecognizeDocumentsRequest.BarcodeDetectionOptions

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A configuration object for detecting barcodes in a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct BarcodeDetectionOptions
```

## Topics

### Getting the symbology
- [var coalesceCompositeSymbologies: Bool](./barcodedetectionoptions-swift.struct/coalescecompositesymbologies.md)
  A Boolean value that indicates whether the request combines multiple codes.
- [var enabled: Bool](./barcodedetectionoptions-swift.struct/enabled.md)
  Boolean value that indicates whether to detect barcodes in the document.
- [var symbologies: [BarcodeSymbology]](./barcodedetectionoptions-swift.struct/symbologies.md)
  The barcode symbologies that the request detects in an image.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring a request
- [RecognizeDocumentsRequest.TextRecognitionOptions](./textrecognitionoptions-swift.struct.md)
  A configuration object for detected and recognized text within the document.
- [var barcodeDetectionOptions: RecognizeDocumentsRequest.BarcodeDetectionOptions](./barcodedetectionoptions-swift.property.md)
  Configuration for detecting machine-readable codes in the document.
- [var textRecognitionOptions: RecognizeDocumentsRequest.TextRecognitionOptions](./textrecognitionoptions-swift.property.md)
  Configuration for recognizing text in the document.
- [var supportedBarcodeSymbologies: [BarcodeSymbology]](./supportedbarcodesymbologies.md)
  The collection of revisions the request supports.
- [var supportedRecognitionLanguages: [Locale.Language]](./supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/barcodedetectionoptions-swift.struct)*