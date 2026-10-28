# minimumTextHeightFraction

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The minimum height, relative to the image height, of the text to recognize.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumTextHeightFraction: Float
```

## Discussion

Specify a floating-point number relative to the image height. For example, to limit recognition to text that’s half of the image height, use `0.5`. Increasing the size reduces memory consumption and expedites recognition with the tradeoff of ignoring text smaller than the minimum height. The default value is `1/32`, or `0.03125`.

## See Also

### Configuring a request
- [var automaticallyDetectsLanguage: Bool](./automaticallydetectslanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var usesLanguageCorrection: Bool](./useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [var supportedRecognitionLanguages: [Locale.Language]](./supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.
- [var customWords: [String]](./customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var recognitionLanguages: [Locale.Language]](./recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var recognitionLevel: RecognizeTextRequest.RecognitionLevel](./recognitionlevel-swift.property.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.
- [RecognizeTextRequest.RecognitionLevel](./recognitionlevel-swift.enum.md)
  Constants that identify the performance and accuracy of the text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizetextrequest/minimumtextheightfraction)*