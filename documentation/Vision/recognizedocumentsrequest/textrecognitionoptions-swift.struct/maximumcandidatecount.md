# maximumCandidateCount

**Framework**: Vision  
**Kind**: property

The maximum number of text candidates to return.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var maximumCandidateCount: Int
```

#### Discussion

There are different variations of this candiate count, the default value is `3`, and the maximum value is `10`.

## See Also

- [var automaticallyDetectLanguage: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/automaticallydetectlanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var customWords: [String]](recognizedocumentsrequest/textrecognitionoptions-swift.struct/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var minimumTextHeightFraction: Float](recognizedocumentsrequest/textrecognitionoptions-swift.struct/minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](recognizedocumentsrequest/textrecognitionoptions-swift.struct/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var useLanguageCorrection: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/uselanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct/maximumcandidatecount)*