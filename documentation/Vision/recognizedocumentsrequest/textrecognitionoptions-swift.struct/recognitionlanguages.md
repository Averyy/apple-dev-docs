# recognitionLanguages

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

An array of languages to detect, in priority order.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var recognitionLanguages: [Locale.Language]
```

## Discussion

The order of the languages in the array defines the order in which the system uses languages during language processing and text recognition.

Specify the languages as two-letter ISO language codes.

## See Also

### Inspecting the recognized text
- [var automaticallyDetectLanguage: Bool](./automaticallydetectlanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var customWords: [String]](./customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var maximumCandidateCount: Int](./maximumcandidatecount.md)
  The maximum number of text candidates to return.
- [var minimumTextHeightFraction: Float](./minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var useLanguageCorrection: Bool](./uselanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct/recognitionlanguages)*