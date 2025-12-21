# heatMap

**Framework**: Vision  
**Kind**: property

A grayscale heat map of important areas across the image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let heatMap: PixelBufferObservation
```

#### Discussion

The heat map is a pixel buffer in a one-component floating-point pixel format.

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [let salientObjects: [RectangleObservation]](saliencyimageobservation/salientobjects.md)
  A collection of objects describing the distinct areas of the saliency heat map.
- [struct RectangleObservation](rectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/saliencyimageobservation/heatmap)*