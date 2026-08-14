# VNTextObservation

**Framework**: Vision  
**Kind**: class

Information about regions of text that an image-analysis request detects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNTextObservation
```

#### Overview

This type of observation results from a [`VNDetectTextRectanglesRequest`](vndetecttextrectanglesrequest.md). It expresses the location of each detected character by its bounding box.

## Topics

### Finding Individual Characters
- [var characterBoxes: [VNRectangleObservation]?](vntextobservation/characterboxes.md)
  An array of detected individual character bounding boxes.

## Relationships

### Inherits From
- [VNRectangleObservation](vnrectangleobservation.md)
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

- [class VNDetectTextRectanglesRequest](vndetecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntextobservation)*