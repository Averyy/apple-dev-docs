# customWords

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

An array of strings to supplement the recognized languages at the word-recognition stage.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var customWords: [String] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSArray<NSString *> * customWords;
```

## Mentions

- [Recognizing Text in Images](../recognizing-text-in-images.md)

#### Discussion

Custom words take precedence over the standard lexicon. The request ignores this value if [`usesLanguageCorrection`](./useslanguagecorrection.md) is [`false`](../../Swift/false.md).

## See Also

### Specifying the Language
- [var automaticallyDetectsLanguage: Bool](./automaticallydetectslanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var recognitionLanguages: [String]](./recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var usesLanguageCorrection: Bool](./useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [func supportedRecognitionLanguages() throws -> [String]](./supportedrecognitionlanguages%28%29.md)
  Returns the identifiers of the languages that the request supports.
- [class func supportedRecognitionLanguages(for: VNRequestTextRecognitionLevel, revision: Int) throws -> [String]](./supportedrecognitionlanguages%28for,revision%29.md)
  Requests a list of languages that the specified revision recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/customwords)*