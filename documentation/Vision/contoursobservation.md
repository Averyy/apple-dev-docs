# ContoursObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents the detected contours in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct ContoursObservation
```

## Topics

### Creating an observation
- [init(VNContoursObservation)](./contoursobservation/init%28_%29.md)
  Creates a contours observation.
### Inspecting an observation
- [var contourCount: Int](./contoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](./contoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [ContoursObservation.Contour]](./contoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
### Getting the contours
- [ContoursObservation.Contour](./contoursobservation/contour.md)
  An object that represents a detected contour in an image.
- [func contourAtIndex(Int) -> ContoursObservation.Contour?](./contoursobservation/contouratindex%28_%29.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func countourAtIndexPath(IndexPath) -> ContoursObservation.Contour?](./contoursobservation/countouratindexpath%28_%29.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionObservation](./visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation)*