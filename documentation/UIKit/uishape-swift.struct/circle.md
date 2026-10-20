# circle

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Creates a circular shape, with a radius equal to half the length of the frame rectangle’s smallest edge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
static var circle: UIShape { get }
```

## See Also

### Creating a hover shape
- [static var rect: UIShape](./rect.md)
  Creates a rectangular shape.
- [static var capsule: UIShape](./capsule.md)
  Creates a capsule shape, a rounded rectangle with a corner radius equal to half the length of the rectangle’s smallest edge.
- [static func rect(cornerRadius: CGFloat, cornerCurve: UICornerCurve, maskedCorners: UIRectCorner) -> UIShape](./rect%28cornerradius,cornercurve,maskedcorners%29.md)
  Creates a rectangular shape with rounded corners, using the provided corner radius, corner curve, and rectangle corners.
- [static func fixedRect(CGRect, cornerRadius: CGFloat, cornerCurve: UICornerCurve, maskedCorners: UIRectCorner) -> UIShape](./fixedrect%28_,cornerradius,cornercurve,maskedcorners%29.md)
  Creates a fixed rectangular shape that uses the provided rectangle as its shape, regardless of the frame that contains it.
- [enum UICornerCurve](../uicornercurve.md)
  The corner curve to apply to a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct/circle)*