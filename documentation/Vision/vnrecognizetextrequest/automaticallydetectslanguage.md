# automaticallyDetectsLanguage

**Framework**: Vision  
**Kind**: property

A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var automaticallyDetectsLanguage: Bool { get set }
```

## See Also

- [var recognitionLanguages: [String]](vnrecognizetextrequest/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var usesLanguageCorrection: Bool](vnrecognizetextrequest/useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [var customWords: [String]](vnrecognizetextrequest/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [func supportedRecognitionLanguages() throws -> [String]](vnrecognizetextrequest/supportedrecognitionlanguages.md)
  Returns the identifiers of the languages that the request supports.
- [class func supportedRecognitionLanguages(for: VNRequestTextRecognitionLevel, revision: Int) throws -> [String]](vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:).md)
  Requests a list of languages that the specified revision recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/automaticallydetectslanguage)*