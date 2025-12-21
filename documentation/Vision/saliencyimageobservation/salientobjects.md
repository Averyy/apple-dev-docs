# salientObjects

**Framework**: Vision  
**Kind**: property

A collection of objects describing the distinct areas of the saliency heat map.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let salientObjects: [RectangleObservation]
```

#### Discussion

The objects in this array don’t follow any specific ordering. It’s up to your app to iterate across the observations and apply desired ordering.

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let heatMap: PixelBufferObservation](saliencyimageobservation/heatmap.md)
  A grayscale heat map of important areas across the image.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [struct RectangleObservation](rectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/saliencyimageobservation/salientobjects)*