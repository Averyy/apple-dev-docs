# CIColor

**Framework**: Core Image  
**Kind**: class

The component values defining a color in a specific color space.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIColor
```

## Mentions

- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)

#### Overview

You use `CIColor` objects in conjunction with other Core Image classes, such as  [`CIFilter`](cifilter-swift.class.md), [`CIContext`](cicontext.md), and [`CIImage`](ciimage.md), to take advantage of the built-in Core Image filters when processing images.

A color space defines a one-, two-, three-, or four-dimensional environment whose color components represent intensity values. A color component is also referred to as a . An RGB color space, for example, is a three-dimensional color space whose stimuli are the red, green, and blue intensities that make up a given color. Regardless of the color space, in Core Image, color values range from `0.0` to `1.0`, with `0.0` representing an absence of that component (0 percent) and `1.0` representing 100 percent.

Colors also have an alpha component, which represents the opacity of the color, with `0.0` meaning completely transparent and `1.0` meaning completely opaque. If a color does not have an explicit alpha component, Core Image paints the color as if the alpha component equals `1.0`. You always provide unpremultiplied color components to Core Image, and Core Image then provides unpremultiplied color components to you. Core Image premultiplies each color component with the alpha value in order to optimize calculations. For more information on premultiplied alpha values, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Topics

### Initializing Color Objects
- [init(cgColor: CGColor)](cicolor/init(cgcolor:).md)
  Initializes a Core Image color object with a Core Graphics color.
- [convenience init(color: UIColor)](cicolor/init(color:).md)
  Initializes a Core Image color object using a UIKit (or AppKit) color object.
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cicolor/init(red:green:blue:alpha:).md)
  Initializes a Core Image color object with the specified red, green, blue, and alpha component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:alpha:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.
### Creating Color Objects
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)](cicolor/init(red:green:blue:).md)
  Creates a color object using the specified RGB color component values
- [convenience init(string: String)](cicolor/init(string:).md)
  Creates a color object using the RGBA color component values specified by a string.
### Getting Color Components
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
- [var stringRepresentation: String](cicolor/stringrepresentation.md)
  A formatted string that specifies the components of the color.
### Creating a CIColor Object with Preset Components
- [class var black: CIColor](cicolor/black.md)
  Returns a color object whose RGB values are all `0.0` and whose alpha value is `1.0`.
- [class var blue: CIColor](cicolor/blue-swift.type.property.md)
  Returns a color object whose RGB values are `0.0`, `0.0`, and `1.0` and whose alpha value is `1.0`.
- [class var clear: CIColor](cicolor/clear.md)
  Returns a color object whose RGB and alpha values are all `0.0`.
- [class var cyan: CIColor](cicolor/cyan.md)
  Returns a color object whose RGB values are `0.0`, `1.0`, and `1.0` and whose alpha value is `1.0`.
- [class var gray: CIColor](cicolor/gray.md)
  Returns a color object whose RGB values are all `0.5` and whose alpha value is `1.0`.
- [class var green: CIColor](cicolor/green-swift.type.property.md)
  Returns a color object whose RGB values are `0.0`, `1.0`, and `0.0` and whose alpha value is `1.0`.
- [class var magenta: CIColor](cicolor/magenta.md)
  Returns a color object whose RGB values are `1.0`, `0.0`, and `1.0` and whose alpha value is `1.0`.
- [class var red: CIColor](cicolor/red-swift.type.property.md)
  Returns a color object whose RGB values are `1.0`, `0.0`, and `0.0` and whose alpha value is `1.0`.
- [class var white: CIColor](cicolor/white.md)
  Returns a color object whose RGB values are all `1.0` and whose alpha value is `1.0`.
- [class var yellow: CIColor](cicolor/yellow.md)
  Returns a color object whose RGB values are `1.0`, `1.0`, and `0.0` and whose alpha value is `1.0`.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CIFilter](cifilter-swift.class.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIVector](civector.md)
  A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor)*