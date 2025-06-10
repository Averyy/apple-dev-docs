# RecognizeDocumentsRequest.BarcodeDetectionOptions

**Framework**: Vision  
**Kind**: struct

A configuration object for detecting barcodes in a document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct BarcodeDetectionOptions
```

## Topics

### Getting the symbology
- [var coalesceCompositeSymbologies: Bool](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/coalescecompositesymbologies.md)
  A Boolean value that indicates whether the request combines multiple codes.
- [var enabled: Bool](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/enabled.md)
  A Boolean value that indicates whether to detect barcodes in the document.
- [var symbologies: [BarcodeSymbology]](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/symbologies.md)
  The barcode symbologies that the request detects in an image.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RecognizeDocumentsRequest.TextRecognitionOptions](recognizedocumentsrequest/textrecognitionoptions-swift.struct.md)
  A configuration object for detected and recognized text within the document.
- [var barcodeDetectionOptions: RecognizeDocumentsRequest.BarcodeDetectionOptions](recognizedocumentsrequest/barcodedetectionoptions-swift.property.md)
  A configuration object for detecting barcodes in a document.
- [var textRecognitionOptions: RecognizeDocumentsRequest.TextRecognitionOptions](recognizedocumentsrequest/textrecognitionoptions-swift.property.md)
  A configuration object for detected and recognized text within the document.
- [var supportedBarcodeSymbologies: [BarcodeSymbology]](recognizedocumentsrequest/supportedbarcodesymbologies.md)
  The collection of barcode symbologies recognized by the request.
- [var supportedRecognitionLanguages: [Locale.Language]](recognizedocumentsrequest/supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/barcodedetectionoptions-swift.struct)*