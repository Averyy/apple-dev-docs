# inset(by:)

**Framework**: UIKit  
**Kind**: method

Creates a new modified shape by applying the provided inset to this shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
func inset(by amount: CGFloat) -> UIShape
```

#### Discussion

You can use negative values to add inner padding to a shape.

If it isn’t possible to inset this shape (for example, if it’s a custom path), this method doesn’t have any effect. For some shapes like rounded rectangles, this method can also modify the corner radii of the shape to ensure the resulting corners are concentric.

## See Also

- [func inset(by: UIEdgeInsets) -> UIShape](uishape-swift.struct/inset(by:)-5jxgl.md)
  Creates a new modified shape by applying the provided insets to this shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct/inset(by:)-7v5nk)*