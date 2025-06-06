# VNRectangleObservation

**Framework**: Vision  
**Kind**: class

An object that represents the four vertices of a detected rectangle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNRectangleObservation
```

## Topics

### Creating an Observation
- [convenience init(requestRevision: Int, topLeft: CGPoint, topRight: CGPoint, bottomRight: CGPoint, bottomLeft: CGPoint)](vnrectangleobservation/init(requestrevision:topleft:topright:bottomright:bottomleft:).md)
  Creates a rectangle observation from its corner points.
- [convenience init(requestRevision: Int, topLeft: CGPoint, bottomLeft: CGPoint, bottomRight: CGPoint, topRight: CGPoint)](vnrectangleobservation/init(requestrevision:topleft:bottomleft:bottomright:topright:).md)
  Creates a rectangle observation from its corner points.
### Accessing the Coordinates
- [var bottomLeft: CGPoint](vnrectangleobservation/bottomleft.md)
  The coordinates of the lower-left corner of the observation bounding box.
- [var bottomRight: CGPoint](vnrectangleobservation/bottomright.md)
  The coordinates of the lower-right corner of the observation bounding box.
- [var topLeft: CGPoint](vnrectangleobservation/topleft.md)
  The coordinates of the upper-left corner of the observation bounding box.
- [var topRight: CGPoint](vnrectangleobservation/topright.md)
  The coordinates of the upper-right corner of the observation bounding box.

## Relationships

### Inherits From
- [VNDetectedObjectObservation](vndetectedobjectobservation.md)
### Inherited By
- [VNBarcodeObservation](vnbarcodeobservation.md)
- [VNRecognizedTextObservation](vnrecognizedtextobservation.md)
- [VNTextObservation](vntextobservation.md)
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

- [var results: [VNRectangleObservation]?](vndetectdocumentsegmentationrequest/results.md)
  The results of a document segmentation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrectangleobservation)*