# SaliencyImageObservation

**Framework**: Vision  
**Kind**: struct

An observation that contains a grayscale heat map of important areas across an image.

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
struct SaliencyImageObservation
```

## Topics

### Creating an observation
- [init?(VNSaliencyImageObservation)](saliencyimageobservation/init(_:).md)
  Creates a saliency image observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let heatMap: PixelBufferObservation](saliencyimageobservation/heatmap.md)
  A grayscale heat map of important areas across the image.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [let salientObjects: [RectangleObservation]](saliencyimageobservation/salientobjects.md)
  A collection of objects describing the distinct areas of the saliency heat map.
- [struct RectangleObservation](rectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/saliencyimageobservation)*