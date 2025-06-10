# init(red:green:blue:alpha:)

**Framework**: Core Image  
**Kind**: init

Initializes a Core Image color object with the specified red, green, blue, and alpha component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

#### Return Value

The resulting Core Image color.

## See Also

- [init(cgColor: CGColor)](cicolor/init(cgcolor:).md)
  Initializes a Core Image color object with a Core Graphics color.
- [convenience init(color: UIColor)](cicolor/init(color:).md)
  Initializes a Core Image color object using a UIKit (or AppKit) color object.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:alpha:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:alpha:))*