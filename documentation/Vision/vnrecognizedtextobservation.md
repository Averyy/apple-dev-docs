# VNRecognizedTextObservation

**Framework**: Vision  
**Kind**: class

A request that detects and recognizes regions of text in an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNRecognizedTextObservation
```

## Mentions

- [Recognizing Text in Images](recognizing-text-in-images.md)

#### Overview

This type of observation results from a [`VNRecognizeTextRequest`](vnrecognizetextrequest.md). It contains information about both the location and content of text and glyphs that Vision recognized in the input image.

## Topics

### Obtaining Recognized Text
- [func topCandidates(Int) -> [VNRecognizedText]](vnrecognizedtextobservation/topcandidates(_:).md)
  Requests the  top candidates for a recognized text string.
- [class VNRecognizedText](vnrecognizedtext.md)
  Text recognized in an image through a text recognition request.

## Relationships

### Inherits From
- [VNRectangleObservation](vnrectangleobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [Recognizing Text in Images](recognizing-text-in-images.md)
  Add text-recognition features to your app using the Vision framework.
- [Structuring Recognized Text on a Document](../visionkit/structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [Extracting phone numbers from text in images](extracting-phone-numbers-from-text-in-images.md)
  Analyze and filter phone numbers from text in live capture by using Vision.
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [class VNRecognizeTextRequest](vnrecognizetextrequest.md)
  An image-analysis request that finds and recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedtextobservation)*