# init(normalizedRect:)

**Framework**: Vision  
**Kind**: init

Creates a rectangle from the specified Core Graphics rectangle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(normalizedRect: CGRect)
```

## Parameters

- `normalizedRect`: The normalized rect.

## See Also

- [init(x: CGFloat, y: CGFloat, width: CGFloat, height: CGFloat)](normalizedrect/init(x:y:width:height:).md)
  Creates a rectangle with the specified coordinates.
- [init(imageRect: CGRect, in: CGSize)](normalizedrect/init(imagerect:in:).md)
  Creates a normalized rectangle from a rectangle in an image coordinate space.
- [init(imageRect: CGRect, in: CGSize, normalizedTo: NormalizedRect)](normalizedrect/init(imagerect:in:normalizedto:).md)
  Creates a rectangle normalized to a region of interest in an image from a rectangle in an image coordinate space.
- [static var fullImage: NormalizedRect](normalizedrect/fullimage.md)
  A normalized rectangle with an origin at zero and a width and height of one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedrect/init(normalizedrect:))*