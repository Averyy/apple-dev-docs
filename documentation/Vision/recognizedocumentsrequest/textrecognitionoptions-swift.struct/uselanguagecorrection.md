# useLanguageCorrection

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request applies language correction during the recognition process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var useLanguageCorrection: Bool
```

## Discussion

When this value is `true`, Vision applies language correction during the recognition process. When set to `false`, this property returns the raw recognition results, which provides performance benefits but less accurate results.

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
- [var recognitionLanguages: [Locale.Language]](./recognitionlanguages.md)
  An array of languages to detect, in priority order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct/uselanguagecorrection)*