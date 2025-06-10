# minimumTextHeightFraction

**Framework**: Vision  
**Kind**: property

The minimum height, relative to the image height, of the text to recognize.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var minimumTextHeightFraction: Float
```

#### Discussion

Specify a floating-point number relative to the image height. For example, to limit recognition to text that’s half of the image height, use `0.5`. Increasing the size reduces memory consumption and expedites recognition with the tradeoff of ignoring text smaller than the minimum height. The default value is `1/32`, or `0.03125`.

## See Also

- [var automaticallyDetectLanguage: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/automaticallydetectlanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var customWords: [String]](recognizedocumentsrequest/textrecognitionoptions-swift.struct/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var maximumCandidateCount: Int](recognizedocumentsrequest/textrecognitionoptions-swift.struct/maximumcandidatecount.md)
  The maximum number of text candidates to return.
- [var recognitionLanguages: [Locale.Language]](recognizedocumentsrequest/textrecognitionoptions-swift.struct/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var useLanguageCorrection: Bool](recognizedocumentsrequest/textrecognitionoptions-swift.struct/uselanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct/minimumtextheightfraction)*