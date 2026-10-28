# cornerConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A configuration that defines the corners of the view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, copy, nonnull) UICornerConfiguration * cornerConfiguration;
```

## Discussion

For more information on how to configure view corners, see [`UICornerConfiguration`](../uicornerconfiguration-c.class.md).

## See Also

### Configuring a view’s corners
- [UICornerConfiguration](../uicornerconfiguration-c.class.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [UICornerRadius](../uicornerradius-c.class.md)
  A type that represents the radius the system uses to round a corner.
- [func effectiveRadius(corner: UIRectCorner) -> CGFloat](./effectiveradius%28corner%29.md)
  Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/cornerconfiguration-3m8ya)*