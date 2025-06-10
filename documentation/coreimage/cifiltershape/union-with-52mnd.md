# union(with:)

**Framework**: Core Image  
**Kind**: method

Creates a filter shape that results from the union of the current filter shape and another filter shape object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func union(with s2: CIFilterShape) -> CIFilterShape
```

#### Return Value

The filter shape object that results from the union.

## Parameters

- `s2`: A filter shape object.

## See Also

- [func insetBy(x: Int32, y: Int32) -> CIFilterShape](cifiltershape/insetby(x:y:).md)
  Modifies a filter shape object so that it is inset by the specified x and y values.
- [func intersect(with: CIFilterShape) -> CIFilterShape](cifiltershape/intersect(with:)-8iw.md)
  Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [func intersect(with: CGRect) -> CIFilterShape](cifiltershape/intersect(with:)-2o2n8.md)
  Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [func transform(by: CGAffineTransform, interior: Bool) -> CIFilterShape](cifiltershape/transform(by:interior:).md)
  Creates a filter shape that results from applying a transform to the current filter shape.
- [func union(with: CGRect) -> CIFilterShape](cifiltershape/union(with:)-75ebo.md)
  Creates a filter shape that results from the union of the current filter shape and a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape/union(with:)-52mnd)*