# VNDetectTextRectanglesRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNDetectTextRectanglesRequest : VNImageBasedRequest
```

#### Overview

This request returns detected text characters as rectangular bounding boxes with origin and size.

## Topics

### Configuring a Request
- [var reportCharacterBoxes: Bool](./vndetecttextrectanglesrequest/reportcharacterboxes.md)
  A Boolean value that indicates whether the request detects character bounding boxes.
### Accessing the Results
- [var results: [VNTextObservation]?](./vndetecttextrectanglesrequest/results.md)
  The results of the request to detect text rectangles.
### Identifying Request Revisions
- [var VNDetectTextRectanglesRequestRevision1: Int](./vndetecttextrectanglesrequestrevision1.md)
  A constant for specifying revision 1 of the text rectangles detection request.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text detection
- [class VNTextObservation](./vntextobservation.md)
  Information about regions of text that an image-analysis request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttextrectanglesrequest)*