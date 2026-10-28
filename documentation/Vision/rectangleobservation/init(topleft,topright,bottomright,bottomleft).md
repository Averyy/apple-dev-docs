# init(topLeft:topRight:bottomRight:bottomLeft:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a rectangle observation from its corner points.

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
init(topLeft: NormalizedPoint, topRight: NormalizedPoint, bottomRight: NormalizedPoint, bottomLeft: NormalizedPoint)
```

## Discussion

The framework normalizes the coordinates of the rectangle to the dimensions of the processed image, with the origin at the bottom-left corner of the image.

## See Also

### Creating an observation
- [init(VNRectangleObservation)](./init%28_%29.md)
  Creates a rectangle observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/rectangleobservation/init(topleft:topright:bottomright:bottomleft:))*