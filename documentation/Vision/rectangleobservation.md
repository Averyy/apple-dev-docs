# RectangleObservation

**Framework**: Vision  
**Kind**: struct

An object that represents the four vertices of a detected rectangle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct RectangleObservation
```

## Topics

### Creating an observation
- [init(VNRectangleObservation)](rectangleobservation/init(_:).md)
  Creates a rectangle observation.
- [init(topLeft: NormalizedPoint, topRight: NormalizedPoint, bottomRight: NormalizedPoint, bottomLeft: NormalizedPoint)](rectangleobservation/init(topleft:topright:bottomright:bottomleft:).md)
  Creates a rectangle observation from its corner points.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.

## Relationships

### Conforms To
- [BoundingBoxProviding](boundingboxproviding.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [QuadrilateralProviding](quadrilateralproviding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/rectangleobservation)*