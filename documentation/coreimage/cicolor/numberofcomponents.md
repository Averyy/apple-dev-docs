# numberOfComponents

**Framework**: Core Image  
**Kind**: property

Returns the number of color components in the color.

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

## See Also

- [var colorSpace: CGColorSpace](cicolor/colorspace.md)
  The Quartz 2D color space associated with the color.
- [var components: UnsafePointer<CGFloat>](cicolor/components.md)
  The color components of the color.
- [var red: CGFloat](cicolor/red-swift.property.md)
  The unpremultiplied red component of the color.
- [var green: CGFloat](cicolor/green-swift.property.md)
  The unpremultiplied green component of the color.
- [var blue: CGFloat](cicolor/blue-swift.property.md)
  The unpremultiplied blue component of the color.
- [var alpha: CGFloat](cicolor/alpha.md)
  The alpha value of the color.
- [var stringRepresentation: String](cicolor/stringrepresentation.md)
  A formatted string that specifies the components of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/numberofcomponents)*