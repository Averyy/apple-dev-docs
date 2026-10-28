# VNRecognizedText

**Framework**: Vision  
**Kind**: class  
**Role**: Class

Text recognized in an image through a text recognition request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNRecognizedText
```

```objc
@interface VNRecognizedText : NSObject
```

## Overview

A single [`VNRecognizedTextObservation`](./vnrecognizedtextobservation.md) can contain multiple recognized text objects—one for each candidate.

## Topics

### Creating a Recognized Text Instance
- [init?(coder: NSCoder)](./vnrecognizedtext/init%28coder%29.md)
### Determining Recognized Text
- [var string: String](./vnrecognizedtext/string.md)
  The top candidate for recognized text.
- [var confidence: VNConfidence](./vnrecognizedtext/confidence.md)
  A normalized confidence score for the text recognition result.
### Locating Recognized Text
- [func boundingBox(for: Range<String.Index>) throws -> VNRectangleObservation?](./vnrecognizedtext/boundingbox%28for%29.md)
  Calculates the bounding box around the characters in the range of a string.
- [- boundingBoxForRange:error:](./vnrecognizedtext/boundingboxforrange_error_.md)
  Calculates the bounding box around the characters in the range of a string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Obtaining Recognized Text
- [func topCandidates(Int) -> [VNRecognizedText]](./vnrecognizedtextobservation/topcandidates%28_%29.md)
  Requests the *n* top candidates for a recognized text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedtext)*