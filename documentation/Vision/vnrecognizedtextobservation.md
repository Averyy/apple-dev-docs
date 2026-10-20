# VNRecognizedTextObservation

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNRecognizedTextObservation : VNRectangleObservation
```

## Mentions

- [Recognizing Text in Images](./recognizing-text-in-images.md)

#### Overview

This type of observation results from a [`VNRecognizeTextRequest`](./vnrecognizetextrequest.md). It contains information about both the location and content of text and glyphs that Vision recognized in the input image.

## Topics

### Obtaining Recognized Text
- [func topCandidates(Int) -> [VNRecognizedText]](./vnrecognizedtextobservation/topcandidates%28_%29.md)
  Requests the *n* top candidates for a recognized text string.
- [class VNRecognizedText](./vnrecognizedtext.md)
  Text recognized in an image through a text recognition request.

## Relationships

### Inherits From
- [VNRectangleObservation](./vnrectangleobservation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [VNRequestRevisionProviding](./vnrequestrevisionproviding.md)

## See Also

### Text recognition
- [Recognizing Text in Images](./recognizing-text-in-images.md)
  Add text-recognition features to your app using the Vision framework.
- [Structuring recognized text on a document](../VisionKit/structuring-recognized-text-on-a-document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [Extracting phone numbers from text in images](./extracting-phone-numbers-from-text-in-images.md)
  Analyze and filter phone numbers from text in live capture by using Vision.
- [Locating and displaying recognized text](./locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [class VNRecognizeTextRequest](./vnrecognizetextrequest.md)
  An image-analysis request that finds and recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedtextobservation)*