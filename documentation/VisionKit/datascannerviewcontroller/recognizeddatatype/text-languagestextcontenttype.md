# text(languages:textContentType:)

**Framework**: VisionKit  
**Kind**: method

Creates a data type for text and information the scanner finds in text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func text(languages: [String] = [], textContentType: DataScannerViewController.TextContentType? = nil) -> DataScannerViewController.RecognizedDataType
```

## Mentions

- [Scanning data with the camera](scanning-data-with-the-camera.md)

#### Return Value

A text data type.

#### Discussion

Use this method to create a custom text data type. For example, if you know the content contains languages other than a person’s preferred languages, pass identifiers for those languages as the `languages` parameter. If you only want to scan for telephone numbers, pass [`DataScannerViewController.TextContentType.telephoneNumber`](datascannerviewcontroller/textcontenttype/telephonenumber.md) as the `textContentType` parameter.

To get the data scanner supported languages, use the [`supportedTextRecognitionLanguages`](datascannerviewcontroller/supportedtextrecognitionlanguages.md) property.

## Parameters

- `languages`: The identifiers for the languages that you want   prioritized in the order of language processing. To specify a   person’s preferred languages, pass an empty set. This parameter gives the scanner   a hint on which language processing models to use. The scanner still recognizes all   supported languages.
- `textContentType`: The specific type of semantic text to find. To   identify all content types, pass  .

## See Also

- [DataScannerViewController.TextContentType](datascannerviewcontroller/textcontenttype.md)
  Types of text that a data scanner recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/recognizeddatatype/text(languages:textcontenttype:))*