# RecognizeDocumentsRequest.TextRecognitionOptions

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A configuration object for detected and recognized text within the document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct TextRecognitionOptions
```

## Topics

### Inspecting the recognized text
- [var automaticallyDetectLanguage: Bool](./textrecognitionoptions-swift.struct/automaticallydetectlanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var customWords: [String]](./textrecognitionoptions-swift.struct/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var maximumCandidateCount: Int](./textrecognitionoptions-swift.struct/maximumcandidatecount.md)
  The maximum number of text candidates to return.
- [var minimumTextHeightFraction: Float](./textrecognitionoptions-swift.struct/minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](./textrecognitionoptions-swift.struct/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var useLanguageCorrection: Bool](./textrecognitionoptions-swift.struct/uselanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.

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
- [RecognizeDocumentsRequest.BarcodeDetectionOptions](./barcodedetectionoptions-swift.struct.md)
  A configuration object for detecting barcodes in a document.
- [var barcodeDetectionOptions: RecognizeDocumentsRequest.BarcodeDetectionOptions](./barcodedetectionoptions-swift.property.md)
  Configuration for detecting machine-readable codes in the document.
- [var textRecognitionOptions: RecognizeDocumentsRequest.TextRecognitionOptions](./textrecognitionoptions-swift.property.md)
  Configuration for recognizing text in the document.
- [var supportedBarcodeSymbologies: [BarcodeSymbology]](./supportedbarcodesymbologies.md)
  The collection of revisions the request supports.
- [var supportedRecognitionLanguages: [Locale.Language]](./supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct)*