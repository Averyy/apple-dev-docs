# init(imagePoint:in:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a normalized point from a point in an image coordinate space.

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
init(imagePoint: CGPoint, in imageSize: CGSize)
```

## Parameters

- `imagePoint`: A point in the image coordinate space.
- `imageSize`: The size of the image.

## See Also

### Creating a normalized point
- [init(x: CGFloat, y: CGFloat)](./init%28x,y%29.md)
  Creates a point object with the specified coordinates.
- [init(normalizedPoint: CGPoint)](./init%28normalizedpoint%29.md)
  Creates a point object from the specified Core Graphics point.
- [init(imagePoint: CGPoint, in: CGSize, normalizedTo: NormalizedRect)](./init%28imagepoint,in,normalizedto%29.md)
  Creates a point normalized to a region of interest within an image.
- [static var zero: NormalizedPoint](./zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedpoint/init(imagepoint:in:))*