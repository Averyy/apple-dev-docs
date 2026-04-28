# toImageCoordinates(from:imageSize:origin:)

**Framework**: Vision  
**Kind**: method

Converts a rectangle normalized to a region within an image into full image coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func toImageCoordinates(from regionOfInterest: NormalizedRect, imageSize: CGSize, origin: CoordinateOrigin = .lowerLeft) -> CGRect
```

## Parameters

- `regionOfInterest`: The region within an image you normalized the rect to.
- `imageSize`: The size of the image.
- `origin`: The origin.

## See Also

- [func toImageCoordinates(CGSize, origin: CoordinateOrigin) -> CGRect](normalizedrect/toimagecoordinates(_:origin:).md)
  Converts a rectangle in normalized coordinates into image coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedrect/toimagecoordinates(from:imagesize:origin:))*