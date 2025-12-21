# RecognizeDocumentsRequest.TextRecognitionOptions

**Framework**: Vision  
**Kind**: struct

A configuration object for detected and recognized text within the document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct TextRecognitionOptions
```

## Topics

### Inspecting the recognized text
- [var automaticallyDetectLanguage: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/automaticallydetectlanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var customWords: [String]](recognizedocumentsrequest/textrecognitionoptions-swift.struct/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var maximumCandidateCount: Int](recognizedocumentsrequest/textrecognitionoptions-swift.struct/maximumcandidatecount.md)
  The maximum number of text candidates to return.
- [var minimumTextHeightFraction: Float](recognizedocumentsrequest/textrecognitionoptions-swift.struct/minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](recognizedocumentsrequest/textrecognitionoptions-swift.struct/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var useLanguageCorrection: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/uselanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RecognizeDocumentsRequest.BarcodeDetectionOptions](recognizedocumentsrequest/barcodedetectionoptions-swift.struct.md)
  A configuration object for detecting barcodes in a document.
- [var barcodeDetectionOptions: RecognizeDocumentsRequest.BarcodeDetectionOptions](recognizedocumentsrequest/barcodedetectionoptions-swift.property.md)
  Configuration for detecting machine-readable codes in the document.
- [var textRecognitionOptions: RecognizeDocumentsRequest.TextRecognitionOptions](recognizedocumentsrequest/textrecognitionoptions-swift.property.md)
  Configuration for recognizing text in the document.
- [var supportedBarcodeSymbologies: [BarcodeSymbology]](recognizedocumentsrequest/supportedbarcodesymbologies.md)
  The collection of revisions the request supports.
- [var supportedRecognitionLanguages: [Locale.Language]](recognizedocumentsrequest/supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct)*