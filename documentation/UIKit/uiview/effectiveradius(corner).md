# effectiveRadius(corner:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func effectiveRadius(corner: UIRectCorner) -> CGFloat
```

```objc
- (CGFloat) effectiveRadiusForCorner:(UIRectCorner) corner;
```

#### Return Value

A `CGFloat` value for the effective radius, expressed in points.

#### Overview

When you call this method from [`layoutSubviews()`](./layoutsubviews%28%29.md), [`updateProperties()`](./updateproperties%28%29.md), or [`updateProperties()`](../uiviewcontroller/updateproperties%28%29.md), automatic invalidation occurs if the effective radius changes. If you provide more than one corner (for example, [`allCorners`](../uirectcorner/allcorners.md)), the returned radius represents the maximum effective radius of those corners.

## Parameters

- `corner`: The corner whose effective radius you want to calculate.

## See Also

### Configuring a view’s corners
- [var cornerConfiguration: UICornerConfiguration](./cornerconfiguration-7l0ja.md)
  A configuration that defines the corners of the view.
- [struct UICornerConfiguration](../uicornerconfiguration-swift.struct.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [struct UICornerRadius](../uicornerradius-swift.struct.md)
  A type that represents the radius the system uses to round a corner.
- [cornerConfiguration](./cornerconfiguration-3m8ya.md)
  A configuration that defines the corners of the view.
- [UICornerConfiguration](../uicornerconfiguration-c.class.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [UICornerRadius](../uicornerradius-c.class.md)
  A type that represents the radius the system uses to round a corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/effectiveradius(corner:))*