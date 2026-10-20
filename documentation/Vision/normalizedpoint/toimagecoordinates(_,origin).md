# toImageCoordinates(_:origin:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Converts a point in normalized coordinates into image coordinates.

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
func toImageCoordinates(_ imageSize: CGSize, origin: CoordinateOrigin = .lowerLeft) -> CGPoint
```

## Parameters

- `imageSize`: The size of the image.
- `origin`: The origin.

## See Also

### Converting points
- [func toImageCoordinates(from: NormalizedRect, imageSize: CGSize, origin: CoordinateOrigin) -> CGPoint](./toimagecoordinates%28from,imagesize,origin%29.md)
  Converts a point normalized to a region within an image into full image coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedpoint/toimagecoordinates(_:origin:))*