# init(x:y:width:height:)

**Framework**: Vision  
**Kind**: init

Creates a rectangle with the specified coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

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

- [init(imageRect: CGRect, in: CGSize)](normalizedrect/init(imagerect:in:).md)
  Creates a normalized rectangle from a rectangle in an image coordinate space.
- [init(imageRect: CGRect, in: CGSize, normalizedTo: NormalizedRect)](normalizedrect/init(imagerect:in:normalizedto:).md)
  Creates a rectangle normalized to a region of interest in an image from a rectangle in an image coordinate space.
- [init(normalizedRect: CGRect)](normalizedrect/init(normalizedrect:).md)
  Creates a rectangle from the specified Core Graphics rectangle.
- [static var fullImage: NormalizedRect](normalizedrect/fullimage.md)
  A normalized rectangle with an origin at zero and a width and height of one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedrect/init(x:y:width:height:))*