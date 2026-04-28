# init(normalizedPoint:)

**Framework**: Vision  
**Kind**: init

Creates a point object from the specified Core Graphics point.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(normalizedPoint: CGPoint)
```

## Parameters

- `normalizedPoint`: The Core Graphics point.

## See Also

- [init(x: CGFloat, y: CGFloat)](normalizedpoint/init(x:y:).md)
  Creates a point object with the specified coordinates.
- [init(imagePoint: CGPoint, in: CGSize)](normalizedpoint/init(imagepoint:in:).md)
  Creates a normalized point from a point in an image coordinate space.
- [init(imagePoint: CGPoint, in: CGSize, normalizedTo: NormalizedRect)](normalizedpoint/init(imagepoint:in:normalizedto:).md)
  Creates a point normalized to a region of interest within an image.
- [static var zero: NormalizedPoint](normalizedpoint/zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedpoint/init(normalizedpoint:))*