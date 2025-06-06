# colorWithCGColor:

**Framework**: Core Image  
**Kind**: clm

Creates a color object from a Quartz color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
+ (instancetype)colorWithCGColor:(CGColorRef)c;
```

#### Return_value

A Core Image color object that represents a Quartz color.

#### Discussion

A [`CGColor`](https://developer.apple.com/documentation/coregraphics/cgcolor) object is the fundamental opaque data type used internally by Quartz to represent colors. For more information on Quartz 2D color and color spaces, see [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

You can pass a [`CGColor`](https://developer.apple.com/documentation/coregraphics/cgcolor) object that represents any color space, including CMYK. However, Core Image converts all color spaces to the Core Image working color space before it passes the color to the filter kernel. The Core Image working color space uses three color components plus alpha. 

## Parameters

- `c`: A  Quartz color (  object) created using a Quartz color creation function such as  .

## See Also

- [+ colorWithRed:green:blue:](cicolor/1437941-colorwithred.md)
  Creates a color object using the specified RGB color component values
- [+ colorWithRed:green:blue:alpha:](cicolor/1502111-colorwithred.md)
  Creates a color object using the specified RGBA color component values.
- [+ colorWithString:](cicolor/1438059-colorwithstring.md)
  Creates a color object using the RGBA color component values specified by a string.
- [+ colorWithRed:green:blue:colorSpace:](cicolor/1643579-colorwithred.md)
  Initializes a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [+ colorWithRed:green:blue:alpha:colorSpace:](cicolor/1643575-colorwithred.md)
  Creates a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/1502106-colorwithcgcolor)*