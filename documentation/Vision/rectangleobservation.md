# RectangleObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents the four vertices of a detected rectangle.

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
struct RectangleObservation
```

## Topics

### Creating an observation
- [init(VNRectangleObservation)](./rectangleobservation/init%28_%29.md)
  Creates a rectangle observation.
- [init(topLeft: NormalizedPoint, topRight: NormalizedPoint, bottomRight: NormalizedPoint, bottomLeft: NormalizedPoint)](./rectangleobservation/init%28topleft,topright,bottomright,bottomleft%29.md)
  Creates a rectangle observation from its corner points.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.

## Relationships

### Conforms To
- [BoundingBoxProviding](./boundingboxproviding.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [QuadrilateralProviding](./quadrilateralproviding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionObservation](./visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/rectangleobservation)*