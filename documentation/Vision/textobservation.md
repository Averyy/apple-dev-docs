# TextObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

Information about regions of text that an image-analysis request detects.

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
struct TextObservation
```

## Topics

### Creating an observation
- [init(VNTextObservation)](./textobservation/init%28_%29.md)
  Creates a text observation.
### Inspecting an observation
- [let characterBoxes: [RectangleObservation]?](./textobservation/characterboxes.md)
  An array of detected individual character bounding boxes.
- [struct RectangleObservation](./rectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/textobservation)*