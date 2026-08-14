# TextObservation

**Framework**: Vision  
**Kind**: struct

Information about regions of text that an image-analysis request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+ (Beta)

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
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [QuadrilateralProviding](quadrilateralproviding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/textobservation)*