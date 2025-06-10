# stringRepresentation

**Framework**: Core Image  
**Kind**: property

A formatted string that specifies the components of the color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var stringRepresentation: String { get }
```

#### Discussion

The string representation always has four components—red, green, blue, and alpha. The default value for the alpha component is `1.0`. For example, this string:

`@"0.5 0.7 0.3 1.0"`

indicates an RGB color whose components are 50% red, 70% green, 30% blue, and 100% opaque (alpha value of `1.0`).

## See Also

- [var colorSpace: CGColorSpace](cicolor/colorspace.md)
  The Quartz 2D color space associated with the color.
- [var components: UnsafePointer<CGFloat>](cicolor/components.md)
  The color components of the color.
- [var numberOfComponents: Int](cicolor/numberofcomponents.md)
  Returns the number of color components in the color.
- [var red: CGFloat](cicolor/red-swift.property.md)
  The unpremultiplied red component of the color.
- [var green: CGFloat](cicolor/green-swift.property.md)
  The unpremultiplied green component of the color.
- [var blue: CGFloat](cicolor/blue-swift.property.md)
  The unpremultiplied blue component of the color.
- [var alpha: CGFloat](cicolor/alpha.md)
  The alpha value of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/stringrepresentation)*