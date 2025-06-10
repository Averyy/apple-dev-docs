# transform(by:interior:)

**Framework**: Core Image  
**Kind**: method

Creates a filter shape that results from applying a transform to the current filter shape.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func transform(by m: CGAffineTransform, interior flag: Bool) -> CIFilterShape
```

#### Return Value

The transformed filter shape object.

## Parameters

- `m`: A transform.
- `flag`:   specifies that the new filter shape object can contain all the pixels in the transformed shape (and possibly some that are outside the transformed shape).   specifies that the new filter shape object can contain  a subset of the pixels in the transformed shape (but none of those outside the transformed shape).

## See Also

- [func insetBy(x: Int32, y: Int32) -> CIFilterShape](cifiltershape/insetby(x:y:).md)
  Modifies a filter shape object so that it is inset by the specified x and y values.
- [func intersect(with: CIFilterShape) -> CIFilterShape](cifiltershape/intersect(with:)-8iw.md)
  Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [func intersect(with: CGRect) -> CIFilterShape](cifiltershape/intersect(with:)-2o2n8.md)
  Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [func union(with: CIFilterShape) -> CIFilterShape](cifiltershape/union(with:)-52mnd.md)
  Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [func union(with: CGRect) -> CIFilterShape](cifiltershape/union(with:)-75ebo.md)
  Creates a filter shape that results from the union of the current filter shape and a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape/transform(by:interior:))*