# customWords

**Framework**: Vision  
**Kind**: property

An array of strings to supplement the recognized languages at the word-recognition stage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var customWords: [String]
```

#### Discussion

Custom words take precedence over the standard lexicon. The request ignores this value if [`useLanguageCorrection`](recognizedocumentsrequest/textrecognitionoptions-swift.struct/uselanguagecorrection.md) is `false`.

## See Also

- [var automaticallyDetectLanguage: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/automaticallydetectlanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var maximumCandidateCount: Int](recognizedocumentsrequest/textrecognitionoptions-swift.struct/maximumcandidatecount.md)
  The maximum number of text candidates to return.
- [var minimumTextHeightFraction: Float](recognizedocumentsrequest/textrecognitionoptions-swift.struct/minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](recognizedocumentsrequest/textrecognitionoptions-swift.struct/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var useLanguageCorrection: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/uselanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct/customwords)*