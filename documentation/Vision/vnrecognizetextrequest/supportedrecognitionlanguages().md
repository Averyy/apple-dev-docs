# supportedRecognitionLanguages()

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns the identifiers of the languages that the request supports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func supportedRecognitionLanguages() throws -> [String]
```

```objc
- (NSArray<NSString *> *) supportedRecognitionLanguagesAndReturnError:(NSError **) error;
```

#### Return Value

The language identifiers.

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
- [class func supportedRecognitionLanguages(for: VNRequestTextRecognitionLevel, revision: Int) throws -> [String]](./supportedrecognitionlanguages%28for,revision%29.md)
  Requests a list of languages that the specified revision recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/supportedrecognitionlanguages())*