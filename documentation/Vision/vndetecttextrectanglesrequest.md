# VNDetectTextRectanglesRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that finds regions of visible text in an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectTextRectanglesRequest
```

#### Overview

This request returns detected text characters as rectangular bounding boxes with origin and size.

## Topics

### Configuring a Request
- [var reportCharacterBoxes: Bool](vndetecttextrectanglesrequest/reportcharacterboxes.md)
  A Boolean value that indicates whether the request detects character bounding boxes.
### Accessing the Results
- [var results: [VNTextObservation]?](vndetecttextrectanglesrequest/results.md)
  The results of the request to detect text rectangles.
### Identifying Request Revisions
- [let VNDetectTextRectanglesRequestRevision1: Int](vndetecttextrectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the text rectangles detection request.

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

## See Also

- [class VNTextObservation](vntextobservation.md)
  Information about regions of text that an image-analysis request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttextrectanglesrequest)*