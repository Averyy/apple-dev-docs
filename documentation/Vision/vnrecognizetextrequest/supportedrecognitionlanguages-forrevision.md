# supportedRecognitionLanguages(for:revision:)

**Framework**: Vision  
**Kind**: method

Requests a list of languages that the specified revision recognizes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func supportedRecognitionLanguages(for recognitionLevel: VNRequestTextRecognitionLevel, revision requestRevision: Int) throws -> [String]
```

## Mentions

- [Recognizing Text in Images](recognizing-text-in-images.md)

#### Return Value

An array of supported languages, listed as ISO language codes.

#### Discussion

A language supported in one recognition level may not be available in another recognition level.

## Parameters

- `recognitionLevel`: The level of recognition to prioritize. Set this level to  to prioritize speed over accuracy, and to   to prioritize accuracy at the expense of speed.
- `requestRevision`: The revision of the text recognition algorithm for the Vision framework to use.

## See Also

- [var automaticallyDetectsLanguage: Bool](vnrecognizetextrequest/automaticallydetectslanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var recognitionLanguages: [String]](vnrecognizetextrequest/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var usesLanguageCorrection: Bool](vnrecognizetextrequest/useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [var customWords: [String]](vnrecognizetextrequest/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [func supportedRecognitionLanguages() throws -> [String]](vnrecognizetextrequest/supportedrecognitionlanguages.md)
  Returns the identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:))*