# init(x:y:width:height:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a rectangle with the specified coordinates.

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
init(x: CGFloat, y: CGFloat, width: CGFloat, height: CGFloat)
```

## Parameters

- `x`: The x-coordinate of the rectangle’s lower-left corner.
- `y`: The y-coordinate of the rectangle’s lower-left corner.
- `width`: The width of the rectangle.
- `height`: The hight of the rectangle.

## See Also

### Creating a normalized rectangle
- [init(imageRect: CGRect, in: CGSize)](./init%28imagerect,in%29.md)
  Creates a normalized rectangle from a rectangle in an image coordinate space.
- [init(imageRect: CGRect, in: CGSize, normalizedTo: NormalizedRect)](./init%28imagerect,in,normalizedto%29.md)
  Creates a rectangle normalized to a region of interest in an image from a rectangle in an image coordinate space.
- [init(normalizedRect: CGRect)](./init%28normalizedrect%29.md)
  Creates a rectangle from the specified Core Graphics rectangle.
- [static var fullImage: NormalizedRect](./fullimage.md)
  A normalized rectangle with an origin at zero and a width and height of one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedrect/init(x:y:width:height:))*