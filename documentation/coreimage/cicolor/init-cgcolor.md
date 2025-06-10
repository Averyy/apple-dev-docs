# init(cgColor:)

**Framework**: Core Image  
**Kind**: init

Initializes a Core Image color object with a Core Graphics color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init(cgColor color: CGColor)
```

#### Return Value

The resulting Core Image color.

#### Discussion

A [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor) object is the fundamental opaque data type used internally by Core Graphics to represent colors. For more information on Core Graphics color and color spaces, see [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

You can pass a [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor) object that represents any color space, including CMYK, but Core Image converts all color spaces to the Core Image working color space before it passes the color space to the filter kernel. The Core Image working color space uses three color components plus alpha.

## See Also

- [Color Management Overview](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/csintro/csintro_intro/csintro_intro.html#//apple_ref/doc/uid/TP30001148)
- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [convenience init(color: UIColor)](cicolor/init(color:).md)
  Initializes a Core Image color object using a UIKit (or AppKit) color object.
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cicolor/init(red:green:blue:alpha:).md)
  Initializes a Core Image color object with the specified red, green, blue, and alpha component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:alpha:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(cgcolor:))*