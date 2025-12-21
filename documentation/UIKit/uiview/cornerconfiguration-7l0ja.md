# cornerConfiguration

**Framework**: UIKit  
**Kind**: property

A configuration that defines the corners of the view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var cornerConfiguration: UICornerConfiguration { get set }
```

#### Discussion

For more information on how to configure view corners, see [`UICornerConfiguration`](uicornerconfiguration-swift.struct.md).

## See Also

- [struct UICornerConfiguration](uicornerconfiguration-swift.struct.md)
  A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [struct UICornerRadius](uicornerradius-swift.struct.md)
  A type that represents the radius the system uses to round a corner.
- [func effectiveRadius(corner: UIRectCorner) -> CGFloat](uiview/effectiveradius(corner:).md)
  Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/cornerconfiguration-7l0ja)*