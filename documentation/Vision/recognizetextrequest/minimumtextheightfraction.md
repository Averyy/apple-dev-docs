# minimumTextHeightFraction

**Framework**: Vision  
**Kind**: property

The minimum height, relative to the image height, of the text to recognize.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumTextHeightFraction: Float
```

#### Discussion

Specify a floating-point number relative to the image height. For example, to limit recognition to text that’s half of the image height, use `0.5`. Increasing the size reduces memory consumption and expedites recognition with the tradeoff of ignoring text smaller than the minimum height. The default value is `1/32`, or `0.03125`.

## See Also

- [var automaticallyDetectsLanguage: Bool](recognizetextrequest/automaticallydetectslanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var usesLanguageCorrection: Bool](recognizetextrequest/useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [var supportedRecognitionLanguages: [Locale.Language]](recognizetextrequest/supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.
- [var customWords: [String]](recognizetextrequest/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var recognitionLanguages: [Locale.Language]](recognizetextrequest/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var recognitionLevel: RecognizeTextRequest.RecognitionLevel](recognizetextrequest/recognitionlevel-swift.property.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.
- [RecognizeTextRequest.RecognitionLevel](recognizetextrequest/recognitionlevel-swift.enum.md)
  Constants that identify the performance and accuracy of the text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizetextrequest/minimumtextheightfraction)*