# TextObservation

**Framework**: Vision  
**Kind**: struct

Information about regions of text that an image-analysis request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct TextObservation
```

## Topics

### Creating an observation
- [init(VNTextObservation)](textobservation/init(_:).md)
  Creates a text observation.
### Inspecting an observation
- [let characterBoxes: [RectangleObservation]?](textobservation/characterboxes.md)
  An array of detected individual character bounding boxes.
- [struct RectangleObservation](rectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/textobservation)*