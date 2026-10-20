# RecognizeTextRequest.RecognitionLevel

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Constants that identify the performance and accuracy of the text recognition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum RecognitionLevel
```

## Topics

### Getting the recognition levels
- [RecognizeTextRequest.RecognitionLevel.accurate](./recognitionlevel-swift.enum/accurate.md)
  Accurate text recognition takes more time to produce a more comprehensive result.
- [RecognizeTextRequest.RecognitionLevel.fast](./recognitionlevel-swift.enum/fast.md)
  Fast text recognition returns results more quickly at the expense of accuracy.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var minimumTextHeightFraction: Float](./minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](./recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var recognitionLevel: RecognizeTextRequest.RecognitionLevel](./recognitionlevel-swift.property.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizetextrequest/recognitionlevel-swift.enum)*