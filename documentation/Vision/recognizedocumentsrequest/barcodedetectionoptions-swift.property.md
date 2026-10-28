# barcodeDetectionOptions

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

Configuration for detecting machine-readable codes in the document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var barcodeDetectionOptions: RecognizeDocumentsRequest.BarcodeDetectionOptions
```

## Discussion

Enable barcode detection and set what symbologies (eg. `.qrCode`) will be detected.

## See Also

### Configuring a request
- [RecognizeDocumentsRequest.BarcodeDetectionOptions](./barcodedetectionoptions-swift.struct.md)
  A configuration object for detecting barcodes in a document.
- [RecognizeDocumentsRequest.TextRecognitionOptions](./textrecognitionoptions-swift.struct.md)
  A configuration object for detected and recognized text within the document.
- [var textRecognitionOptions: RecognizeDocumentsRequest.TextRecognitionOptions](./textrecognitionoptions-swift.property.md)
  Configuration for recognizing text in the document.
- [var supportedBarcodeSymbologies: [BarcodeSymbology]](./supportedbarcodesymbologies.md)
  The collection of revisions the request supports.
- [var supportedRecognitionLanguages: [Locale.Language]](./supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/barcodedetectionoptions-swift.property)*