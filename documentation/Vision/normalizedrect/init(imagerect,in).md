# init(imageRect:in:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a normalized rectangle from a rectangle in an image coordinate space.

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
init(imageRect: CGRect, in imageSize: CGSize)
```

## Parameters

- `imageRect`: A rectangle in the image coordinate space.
- `imageSize`: The size of the image.

## See Also

### Creating a normalized rectangle
- [init(x: CGFloat, y: CGFloat, width: CGFloat, height: CGFloat)](./init%28x,y,width,height%29.md)
  Creates a rectangle with the specified coordinates.
- [init(imageRect: CGRect, in: CGSize, normalizedTo: NormalizedRect)](./init%28imagerect,in,normalizedto%29.md)
  Creates a rectangle normalized to a region of interest in an image from a rectangle in an image coordinate space.
- [init(normalizedRect: CGRect)](./init%28normalizedrect%29.md)
  Creates a rectangle from the specified Core Graphics rectangle.
- [static var fullImage: NormalizedRect](./fullimage.md)
  A normalized rectangle with an origin at zero and a width and height of one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedrect/init(imagerect:in:))*