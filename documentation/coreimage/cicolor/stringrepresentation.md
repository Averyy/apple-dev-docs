# stringRepresentation

**Framework**: Core Image  
**Kind**: property

Returns a formatted string with the unpremultiplied color and alpha components of the color.

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

The string representation always has four components: red, green, blue, and alpha.

Some example string representations of colors:

| `CIColor` | `stringRepresentation` |
| --- | --- |
| `[CIColor colorWithRed:0.2 green:0.4 blue:0.6]` | `"0.2 0.4 0.6 1.0"` |
| `/CIColor/yellowColor` | `"1.0 1.0 0.0 1.0"` |

To create a [`CIColor`](cicolor.md) instance from a string representation, use the [`init(string:)`](cicolor/init(string:).md) method.

If the [`CIColor`](cicolor.md) was initialized with a `CGColor` in a non-RGB `CGColorSpace` then it will be converted to sRGB to get the red, green, and blue components.

This property is not KVO-safe because it returns a new `NSString` instance each time. The value of the `NSString` will be the same each time it is called.

## See Also

- [var colorSpace: CGColorSpace](cicolor/colorspace.md)
  Returns the `CGColorSpace` associated with the color
- [var components: UnsafePointer<CGFloat>](cicolor/components.md)
  Return a pointer to an array of `CGFloat` values including alpha.
- [var numberOfComponents: Int](cicolor/numberofcomponents.md)
  Returns the color components of the color including alpha.
- [var red: CGFloat](cicolor/red-swift.property.md)
  Returns the unpremultiplied red component of the color.
- [var green: CGFloat](cicolor/green-swift.property.md)
  Returns the unpremultiplied green component of the color.
- [var blue: CGFloat](cicolor/blue-swift.property.md)
  Returns the unpremultiplied blue component of the color.
- [var alpha: CGFloat](cicolor/alpha.md)
  Returns the alpha value of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/stringrepresentation)*