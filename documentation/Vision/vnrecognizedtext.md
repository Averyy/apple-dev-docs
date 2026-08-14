# VNRecognizedText

**Framework**: Vision  
**Kind**: class

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

#### Overview

A single [`VNRecognizedTextObservation`](vnrecognizedtextobservation.md) can contain multiple recognized text objects—one for each candidate.

## Topics

### Creating a Recognized Text Instance
- [init?(coder: NSCoder)](vnrecognizedtext/init(coder:).md)
### Determining Recognized Text
- [var string: String](vnrecognizedtext/string.md)
  The top candidate for recognized text.
- [var confidence: VNConfidence](vnrecognizedtext/confidence.md)
  A normalized confidence score for the text recognition result.
### Locating Recognized Text
- [func boundingBox(for: Range<String.Index>) throws -> VNRectangleObservation?](vnrecognizedtext/boundingbox(for:).md)
  Calculates the bounding box around the characters in the range of a string.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [func topCandidates(Int) -> [VNRecognizedText]](vnrecognizedtextobservation/topcandidates(_:).md)
  Requests the *n* top candidates for a recognized text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedtext)*