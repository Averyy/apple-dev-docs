# barcodeDetectionOptions

**Framework**: Vision  
**Kind**: property

Configuration for detecting machine-readable codes in the document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var barcodeDetectionOptions: RecognizeDocumentsRequest.BarcodeDetectionOptions
```

#### Discussion

Enable barcode detection and set what symbologies (eg. `.qrCode`) will be detected.

## See Also

- [RecognizeDocumentsRequest.BarcodeDetectionOptions](recognizedocumentsrequest/barcodedetectionoptions-swift.struct.md)
  A configuration object for detecting barcodes in a document.
- [RecognizeDocumentsRequest.TextRecognitionOptions](recognizedocumentsrequest/textrecognitionoptions-swift.struct.md)
  A configuration object for detected and recognized text within the document.
- [var textRecognitionOptions: RecognizeDocumentsRequest.TextRecognitionOptions](recognizedocumentsrequest/textrecognitionoptions-swift.property.md)
  Configuration for recognizing text in the document.
- [var supportedBarcodeSymbologies: [BarcodeSymbology]](recognizedocumentsrequest/supportedbarcodesymbologies.md)
  The collection of revisions the request supports.
- [var supportedRecognitionLanguages: [Locale.Language]](recognizedocumentsrequest/supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/barcodedetectionoptions-swift.property)*