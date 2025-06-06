# VNRecognizeTextRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that finds and recognizes text in an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNRecognizeTextRequest
```

## Mentions

- [Recognizing Text in Images](recognizing-text-in-images.md)

#### Overview

By default, a text recognition request first locates all possible glyphs or characters in the input image, and then analyzes each string. To specify or limit the languages to find in the request, set the [`recognitionLanguages`](vnrecognizetextrequest/recognitionlanguages.md) property to an array that contains the names of the languages of text you want to recognize. Vision returns the result of this request in a [`VNRecognizedTextObservation`](vnrecognizedtextobservation.md) object.

## Topics

### Customizing Recognition Constraints
- [var minimumTextHeight: Float](vnrecognizetextrequest/minimumtextheight.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLevel: VNRequestTextRecognitionLevel](vnrecognizetextrequest/recognitionlevel.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.
- [enum VNRequestTextRecognitionLevel](vnrequesttextrecognitionlevel.md)
  Constants that identify the performance and accuracy of the text recognition.
### Accessing the Results
- [var results: [VNRecognizedTextObservation]?](vnrecognizetextrequest/results.md)
  The results of the text recognition request.
### Specifying the Language
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
- [class func supportedRecognitionLanguages(for: VNRequestTextRecognitionLevel, revision: Int) throws -> [String]](vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:).md)
  Requests a list of languages that the specified revision recognizes.
### Identifying Request Revisions
- [let VNRecognizeTextRequestRevision3: Int](vnrecognizetextrequestrevision3.md)
  A constant for specifying revision 3 of the text recognition request.
- [let VNRecognizeTextRequestRevision2: Int](vnrecognizetextrequestrevision2.md)
  A constant for specifying revision 2 of the text recognition request.
- [let VNRecognizeTextRequestRevision1: Int](vnrecognizetextrequestrevision1.md)
  A constant for specifying revision 1 of the text recognition request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [VNRequestProgressProviding](vnrequestprogressproviding.md)

## See Also

- [Recognizing Text in Images](recognizing-text-in-images.md)
  Add text-recognition features to your app using the Vision framework.
- [Structuring Recognized Text on a Document](../visionkit/structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [Extracting phone numbers from text in images](extracting-phone-numbers-from-text-in-images.md)
  Analyze and filter phone numbers from text in live capture by using Vision.
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [class VNRecognizedTextObservation](vnrecognizedtextobservation.md)
  A request that detects and recognizes regions of text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest)*