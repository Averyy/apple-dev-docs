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
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)

## See Also

- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/saliencyimageobservation)*