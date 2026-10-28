# maximumCandidateCount

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The maximum number of text candidates to return.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maximumCandidateCount: Int
```

## Discussion

There are different variations of this candiate count, the default value is `3`, and the maximum value is `10`.

## See Also

### Inspecting the recognized text
- [var automaticallyDetectLanguage: Bool](./automaticallydetectlanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var customWords: [String]](./customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var minimumTextHeightFraction: Float](./minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](./recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var useLanguageCorrection: Bool](./uselanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/textrecognitionoptions-swift.struct/maximumcandidatecount)*