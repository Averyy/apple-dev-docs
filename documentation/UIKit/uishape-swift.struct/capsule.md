# capsule

**Framework**: UIKit  
**Kind**: property

Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
static var capsule: UIShape { get }
```

## See Also

- [static var rect: UIShape](uishape-swift.struct/rect.md)
  Creates a rectangular shape.
- [static var circle: UIShape](uishape-swift.struct/circle.md)
  Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.
- [static func rect(cornerRadius: CGFloat, cornerCurve: UICornerCurve, maskedCorners: UIRectCorner) -> UIShape](uishape-swift.struct/rect(cornerradius:cornercurve:maskedcorners:).md)
  Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [static func fixedRect(CGRect, cornerRadius: CGFloat, cornerCurve: UICornerCurve, maskedCorners: UIRectCorner) -> UIShape](uishape-swift.struct/fixedrect(_:cornerradius:cornercurve:maskedcorners:).md)
  Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [enum UICornerCurve](uicornercurve.md)
  The corner curve to apply to a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct/capsule)*