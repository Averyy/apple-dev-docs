# colorWithRed:green:blue:

**Framework**: Core Image  
**Kind**: clm

Creates a color object using the specified RGB color component values

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
+ (instancetype)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b;
```

#### Return_value

A Core Image color object that represents an RGB color in the color space specified by the Quartz 2D constant [`kCGColorSpaceGenericRGB`](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericrgb).

## Parameters

- `r`: The value of the red component.
- `g`: The value of the green component.
- `b`: The value of the blue component.

## See Also

- [+ colorWithCGColor:](cicolor/1502106-colorwithcgcolor.md)
  Creates a color object from a Quartz color.
- [+ colorWithRed:green:blue:alpha:](cicolor/1502111-colorwithred.md)
  Creates a color object using the specified RGBA color component values.
- [+ colorWithString:](cicolor/1438059-colorwithstring.md)
  Creates a color object using the RGBA color component values specified by a string.
- [+ colorWithRed:green:blue:colorSpace:](cicolor/1643579-colorwithred.md)
  Initializes a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [+ colorWithRed:green:blue:alpha:colorSpace:](cicolor/1643575-colorwithred.md)
  Creates a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/1437941-colorwithred)*