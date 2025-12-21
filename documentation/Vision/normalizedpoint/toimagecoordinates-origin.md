# toImageCoordinates(_:origin:)

**Framework**: Vision  
**Kind**: method

Converts a point in normalized coordinates into image coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func toImageCoordinates(_ imageSize: CGSize, origin: CoordinateOrigin = .lowerLeft) -> CGPoint
```

## Parameters

- `imageSize`: The size of the image.
- `origin`: The origin.

## See Also

- [func toImageCoordinates(from: NormalizedRect, imageSize: CGSize, origin: CoordinateOrigin) -> CGPoint](normalizedpoint/toimagecoordinates(from:imagesize:origin:).md)
  Converts a point normalized to a region within an image into full image coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedpoint/toimagecoordinates(_:origin:))*