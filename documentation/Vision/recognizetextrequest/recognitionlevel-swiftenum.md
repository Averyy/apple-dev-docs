# RecognizeTextRequest.RecognitionLevel

**Framework**: Vision  
**Kind**: enum

Constants that identify the performance and accuracy of the text recognition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum RecognitionLevel
```

## Topics

### Getting the recognition levels
- [RecognizeTextRequest.RecognitionLevel.accurate](recognizetextrequest/recognitionlevel-swift.enum/accurate.md)
  Accurate text recognition takes more time to produce a more comprehensive result.
- [RecognizeTextRequest.RecognitionLevel.fast](recognizetextrequest/recognitionlevel-swift.enum/fast.md)
  Fast text recognition returns results more quickly at the expense of accuracy.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var automaticallyDetectsLanguage: Bool](recognizetextrequest/automaticallydetectslanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var usesLanguageCorrection: Bool](recognizetextrequest/useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [var supportedRecognitionLanguages: [Locale.Language]](recognizetextrequest/supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.
- [var customWords: [String]](recognizetextrequest/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var minimumTextHeightFraction: Float](recognizetextrequest/minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](recognizetextrequest/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var recognitionLevel: RecognizeTextRequest.RecognitionLevel](recognizetextrequest/recognitionlevel-swift.property.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizetextrequest/recognitionlevel-swift.enum)*