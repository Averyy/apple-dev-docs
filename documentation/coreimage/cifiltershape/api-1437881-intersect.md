# intersect(with:)

**Framework**: Core Image  
**Kind**: instm

Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func intersect(with s2: CIFilterShape) -> CIFilterShape
```

#### Return_value

The filter shape object that results from the intersection.

## Parameters

- `s2`: A filter shape object.

## See Also

- [func insetBy(x: Int32, y: Int32) -> CIFilterShape](cifiltershape/1437987-insetby.md)
  Modifies a filter shape object so that it is inset by the specified x and y values.
- [func intersect(with: CGRect) -> CIFilterShape](cifiltershape/1437806-intersect.md)
  Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [func transform(by: CGAffineTransform, interior: Bool) -> CIFilterShape](cifiltershape/1437808-transform.md)
  Creates a filter shape that results from applying a transform to the current filter shape.
- [func union(with: CIFilterShape) -> CIFilterShape](cifiltershape/1438227-union.md)
  Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [func union(with: CGRect) -> CIFilterShape](cifiltershape/1437601-union.md)
  Creates a filter shape that results from the union of the current filter shape and a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape/1437881-intersect)*