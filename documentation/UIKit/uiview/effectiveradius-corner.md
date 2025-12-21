# effectiveRadius(corner:)

**Framework**: UIKit  
**Kind**: method

Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func effectiveRadius(corner: UIRectCorner) -> CGFloat
```

#### Return Value

A `CGFloat` value for the effective radius, expressed in points.

#### Overview

When you call this method from [`layoutSubviews()`](uiview/layoutsubviews().md), [`updateProperties()`](uiview/updateproperties().md), or [`updateProperties()`](uiviewcontroller/updateproperties().md), automatic invalidation occurs if the effective radius changes. If you provide more than one corner (for example, [`allCorners`](uirectcorner/allcorners.md)), the returned radius represents the maximum effective radius of those corners.

## Parameters

- `corner`: The corner whose effective radius you want to calculate.

## See Also

- [var cornerConfiguration: UICornerConfiguration](uiview/cornerconfiguration-7l0ja.md)
  A configuration that defines the corners of the view.
- [struct UICornerConfiguration](uicornerconfiguration-swift.struct.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [struct UICornerRadius](uicornerradius-swift.struct.md)
  A type that represents the radius the system uses to round a corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/effectiveradius(corner:))*