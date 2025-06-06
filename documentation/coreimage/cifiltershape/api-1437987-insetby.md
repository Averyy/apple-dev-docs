# insetBy(x:y:)

**Framework**: Core Image  
**Kind**: instm

Modifies a filter shape object so that it is inset by the specified x and y values.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func insetBy(x dx: Int32, y dy: Int32) -> CIFilterShape
```

## Parameters

- `dx`: A value that specifies an inset in the x direction.
- `dy`: A value that specifies an inset in the y direction.

## See Also

- [func intersect(with: CIFilterShape) -> CIFilterShape](cifiltershape/1437881-intersect.md)
  Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [func intersect(with: CGRect) -> CIFilterShape](cifiltershape/1437806-intersect.md)
  Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [func transform(by: CGAffineTransform, interior: Bool) -> CIFilterShape](cifiltershape/1437808-transform.md)
  Creates a filter shape that results from applying a transform to the current filter shape.
- [func union(with: CIFilterShape) -> CIFilterShape](cifiltershape/1438227-union.md)
  Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [func union(with: CGRect) -> CIFilterShape](cifiltershape/1437601-union.md)
  Creates a filter shape that results from the union of the current filter shape and a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape/1437987-insetby)*