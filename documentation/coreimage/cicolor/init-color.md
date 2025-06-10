# init(color:)

**Framework**: Core Image  
**Kind**: init

Initializes a Core Image color object using a UIKit (or AppKit) color object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS ?+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(color: UIColor)
```

#### Discussion

In iOS and tvOS, this initializer takes a [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) object and always returns a corresponding Core Image color object.

In macOS, this initializer takes an [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) object. some possible [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) configurations cannot be accurately represented as Core Image (or Core Graphics) colors—in such cases, this initializer returns `nil`.

## Parameters

- `color`: The initial color value, which can belong to any available color space.

## See Also

- [init(cgColor: CGColor)](cicolor/init(cgcolor:).md)
  Initializes a Core Image color object with a Core Graphics color.
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cicolor/init(red:green:blue:alpha:).md)
  Initializes a Core Image color object with the specified red, green, blue, and alpha component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:alpha:colorspace:).md)
  Initializes a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(color:))*