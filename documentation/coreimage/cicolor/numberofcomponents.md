# numberOfComponents

**Framework**: Core Image  
**Kind**: property

Returns the color components of the color including alpha.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var numberOfComponents: Int { get }
```

#### Discussion

This number includes the alpha component if the color contains one.

Typically this number will be `4` for red, green, blue, and alpha. If the [`CIColor`](cicolor.md) was initialized with a `CGColor` then the number will be the same as calling `CGColorGetNumberOfComponents()`

## See Also

- [var colorSpace: CGColorSpace](cicolor/colorspace.md)
  Returns the `CGColorSpace` associated with the color
- [var components: UnsafePointer<CGFloat>](cicolor/components.md)
  Return a pointer to an array of `CGFloat` values including alpha.
- [var red: CGFloat](cicolor/red-swift.property.md)
  Returns the unpremultiplied red component of the color.
- [var green: CGFloat](cicolor/green-swift.property.md)
  Returns the unpremultiplied green component of the color.
- [var blue: CGFloat](cicolor/blue-swift.property.md)
  Returns the unpremultiplied blue component of the color.
- [var alpha: CGFloat](cicolor/alpha.md)
  Returns the alpha value of the color.
- [var stringRepresentation: String](cicolor/stringrepresentation.md)
  Returns a formatted string with the unpremultiplied color and alpha components of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/numberofcomponents)*