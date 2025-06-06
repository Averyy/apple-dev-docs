# UIShape

**Framework**: UIKit  
**Kind**: struct

An abstract representation of a shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
struct UIShape
```

#### Overview

A [`UIShape`](uishape-swift.struct.md) can represent different types of shapes, including:

- A simple shape like a rectangle or circle that resolves into a concrete shape according to context (like size and position)
- A Bézier path
- A dynamic shape that resolves using a custom closure

You typically use a [`UIShape`](uishape-swift.struct.md) with APIs like [`UIHoverStyle`](uihoverstyle.md) to represent the shape of an effect.

## Topics

### Creating a hover shape
- [static var rect: UIShape](uishape-swift.struct/rect.md)
  Creates a rectangular shape.
- [static var capsule: UIShape](uishape-swift.struct/capsule.md)
  Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [static var circle: UIShape](uishape-swift.struct/circle.md)
  Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [static func rect(cornerRadius: CGFloat, cornerCurve: UICornerCurve, maskedCorners: UIRectCorner) -> UIShape](uishape-swift.struct/rect(cornerradius:cornercurve:maskedcorners:).md)
  Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [static func fixedRect(CGRect, cornerRadius: CGFloat, cornerCurve: UICornerCurve, maskedCorners: UIRectCorner) -> UIShape](uishape-swift.struct/fixedrect(_:cornerradius:cornercurve:maskedcorners:).md)
  Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [enum UICornerCurve](uicornercurve.md)
  The corner curve to apply to a view.
### Creating a hover shape from a custom path
- [static func path(UIBezierPath) -> UIShape](uishape-swift.struct/path(_:).md)
  Creates a shape with a custom Bézier path.
### Creating a dynamic hover shape
- [init(some UIShapeProvider)](uishape-swift.struct/init(_:).md)
  Creates a dynamic shape that resolves using the provided resolver closure and resolution context.
- [protocol UIShapeProvider](uishapeprovider-60loj.md)
  An interface for a type that provides a custom shape by resolving it dynamically based on a context.
- [UIShape.ResolutionContext](uishape-swift.struct/resolutioncontext.md)
  The context for resolving a dynamic shape.
- [UIShape.Resolved](uishape-swift.struct/resolved.md)
  A shape that has completely resolved based on a context.
### Creating a shape by applying insets
- [func inset(by: UIEdgeInsets) -> UIShape](uishape-swift.struct/inset(by:)-5jxgl.md)
  Creates a new modified shape by applying the provided insets to this shape.
- [func inset(by: CGFloat) -> UIShape](uishape-swift.struct/inset(by:)-7v5nk.md)
  Creates a new modified shape by applying the provided inset to this shape.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [UIShapeProvider](uishapeprovider-60loj.md)

## See Also

- [var shape: UIShape?](uihoverstyle/shape-21npk.md)
  The shape to use for the hover effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct)*