# colorWithRed:green:blue:alpha:colorSpace:

**Framework**: Core Image  
**Kind**: clm

Creates a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
+ (instancetype)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b alpha:(CGFloat)a colorSpace:(CGColorSpaceRef)colorSpace;
```

#### Return_value

The resulting Core Image color.

## Parameters

- `r`: The unpremultiplied red component of the color.
- `g`: The unpremultiplied green component of the color.
- `b`: The unpremultiplied blue component of the color.
- `a`: The alpha (opacity) component of the color.
- `colorSpace`: The color space in which to create the new color. This color space must conform to the   color space model. 

## See Also

- [+ colorWithCGColor:](cicolor/1502106-colorwithcgcolor.md)
  Creates a color object from a Quartz color.
- [+ colorWithRed:green:blue:](cicolor/1437941-colorwithred.md)
  Creates a color object using the specified RGB color component values
- [+ colorWithRed:green:blue:alpha:](cicolor/1502111-colorwithred.md)
  Creates a color object using the specified RGBA color component values.
- [+ colorWithString:](cicolor/1438059-colorwithstring.md)
  Creates a color object using the RGBA color component values specified by a string.
- [+ colorWithRed:green:blue:colorSpace:](cicolor/1643579-colorwithred.md)
  Initializes a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/1643575-colorwithred)*