# pointsInImage(imageSize:)

**Framework**: Vision  
**Kind**: method

Returns an array containing landmark points in the coordinate space of the specified image size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 10.13+
- tvOS 11.0+

## Declaration

```swift
@nonobjc
func pointsInImage(imageSize: CGSize) -> [CGPoint]
```

#### Return Value

An array containing a [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) for each landmark the system detects in the image, expressed in the coordinate space of the specified image size.

## Parameters

- `imageSize`: The pixel dimensions of the image in which to present landmark points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d/pointsinimage(imagesize:))*