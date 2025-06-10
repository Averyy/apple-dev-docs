# init(string:)

**Framework**: Core Image  
**Kind**: init

Creates a color object using the RGBA color component values specified by a string.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(string representation: String)
```

#### Return Value

A Core Image color object that represents an RGB color in the color space specified by the Quartz 2D constant [`kCGColorSpaceGenericRGB`](https://developer.apple.com/documentation/CoreGraphics/kCGColorSpaceGenericRGB).

## Parameters

- `representation`: indicates an RGB color whose components are 50% red, 70% green, 30% blue, and 100% opaque (alpha value of  ). The string representation always has four components—red, green, blue, and alpha. The default value for the alpha component is  .

## See Also

- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)](cicolor/init(red:green:blue:).md)
  Creates a color object using the specified RGB color component values


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(string:))*