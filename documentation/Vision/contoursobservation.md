# ContoursObservation

**Framework**: Vision  
**Kind**: struct

An object that represents the detected contours in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ContoursObservation
```

## Topics

### Creating an observation
- [init(VNContoursObservation)](contoursobservation/init(_:).md)
  Creates a contours observation.
### Inspecting an observation
- [var contourCount: Int](contoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](contoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [ContoursObservation.Contour]](contoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
### Getting the contours
- [ContoursObservation.Contour](contoursobservation/contour.md)
  An object that represents a detected contour in an image.
- [func contourAtIndex(Int) -> ContoursObservation.Contour?](contoursobservation/contouratindex(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func countourAtIndexPath(IndexPath) -> ContoursObservation.Contour?](contoursobservation/countouratindexpath(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation)*