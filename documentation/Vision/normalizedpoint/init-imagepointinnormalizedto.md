# init(imagePoint:in:normalizedTo:)

**Framework**: Vision  
**Kind**: init

Creates a point normalized to a region of interest within an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(imagePoint: CGPoint, in imageSize: CGSize, normalizedTo regionOfInterest: NormalizedRect)
```

## Parameters

- `imagePoint`: A point in the image coordinate space.
- `imageSize`: The size of the image.
- `regionOfInterest`: The region within the image to normalize the point to.

## See Also

- [init(x: CGFloat, y: CGFloat)](normalizedpoint/init(x:y:).md)
  Creates a point object with the specified coordinates.
- [init(normalizedPoint: CGPoint)](normalizedpoint/init(normalizedpoint:).md)
  Creates a point object from the specified Core Graphics point.
- [init(imagePoint: CGPoint, in: CGSize)](normalizedpoint/init(imagepoint:in:).md)
  Creates a normalized point from a point in an image coordinate space.
- [static var zero: NormalizedPoint](normalizedpoint/zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedpoint/init(imagepoint:in:normalizedto:))*