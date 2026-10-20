# supportedRecognitionLanguages(for:revision:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

Requests a list of languages that the specified revision recognizes.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.15+ - Deprecated in 12.0
- tvOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`supportedRecognitionLanguages()`](./supportedrecognitionlanguages%28%29.md) instead.

## Declaration

```swift
class func supportedRecognitionLanguages(for recognitionLevel: VNRequestTextRecognitionLevel, revision requestRevision: Int) throws -> [String]
```

```objc
+ (NSArray<NSString *> *) supportedRecognitionLanguagesForTextRecognitionLevel:(VNRequestTextRecognitionLevel) recognitionLevel revision:(NSUInteger) requestRevision error:(NSError **) error;
```

## Mentions

- [Recognizing Text in Images](../recognizing-text-in-images.md)

#### Return Value

An array of supported languages, listed as ISO language codes.

#### Discussion

A language supported in one recognition level may not be available in another recognition level.

## Parameters

- `recognitionLevel`: The level of recognition to prioritize. Set this level to [`VNRequestTextRecognitionLevel.fast`](../vnrequesttextrecognitionlevel/fast.md)to prioritize speed over accuracy, and to [`VNRequestTextRecognitionLevel.accurate`](../vnrequesttextrecognitionlevel/accurate.md) to prioritize accuracy at the expense of speed.
- `requestRevision`: The revision of the text recognition algorithm for the Vision framework to use.

## See Also

### Specifying the Language
- [var automaticallyDetectsLanguage: Bool](./automaticallydetectslanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var recognitionLanguages: [String]](./recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var usesLanguageCorrection: Bool](./useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [var customWords: [String]](./customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [func supportedRecognitionLanguages() throws -> [String]](./supportedrecognitionlanguages%28%29.md)
  Returns the identifiers of the languages that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:))*