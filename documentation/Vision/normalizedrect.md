# NormalizedRect

**Framework**: Vision  
**Kind**: struct

The location and dimensions of a rectangle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct NormalizedRect
```

## Topics

### Creating a normalized rectangle
- [init(x: CGFloat, y: CGFloat, width: CGFloat, height: CGFloat)](normalizedrect/init(x:y:width:height:).md)
  Creates a rectangle with the specified coordinates.
- [init(imageRect: CGRect, in: CGSize)](normalizedrect/init(imagerect:in:).md)
  Creates a normalized rectangle from a rectangle in an image coordinate space.
- [init(imageRect: CGRect, in: CGSize, normalizedTo: NormalizedRect)](normalizedrect/init(imagerect:in:normalizedto:).md)
  Creates a rectangle normalized to a region of interest in an image from a rectangle in an image coordinate space.
- [init(normalizedRect: CGRect)](normalizedrect/init(normalizedrect:).md)
  Creates a rectangle from the specified Core Graphics rectangle.
- [static var fullImage: NormalizedRect](normalizedrect/fullimage.md)
  A normalized rectangle with an origin at zero and a width and height of one.
### Inspecting a normalized rectangle
- [let cgRect: CGRect](normalizedrect/cgrect.md)
  The normalized rectangle as a Core Graphics rectangle.
- [var origin: CGPoint](normalizedrect/origin.md)
  The lower left-hand corner of the rectangle.
- [var width: CGFloat](normalizedrect/width.md)
  The width of the rectangle.
- [var height: CGFloat](normalizedrect/height.md)
  The height of the rectangle.
### Converting rectangles
- [func toImageCoordinates(CGSize, origin: CoordinateOrigin) -> CGRect](normalizedrect/toimagecoordinates(_:origin:).md)
  Converts a rectangle in normalized coordinates into image coordinates.
- [func toImageCoordinates(from: NormalizedRect, imageSize: CGSize, origin: CoordinateOrigin) -> CGRect](normalizedrect/toimagecoordinates(from:imagesize:origin:).md)
  Converts a rectangle normalized to a region within an image into full image coordinates.
### Flipping a normalized rectangle
- [func verticallyFlipped() -> NormalizedRect](normalizedrect/verticallyflipped.md)
  Returns a normalized rectangle with the origin flipped between the top and bottom of the image.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct NormalizedPoint](normalizedpoint.md)
  A point in a 2D coordinate system.
- [struct NormalizedCircle](normalizedcircle.md)
  The center point and radius of a 2D circle.
- [enum CoordinateOrigin](coordinateorigin.md)
  The origin of a coordinate system relative to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedrect)*