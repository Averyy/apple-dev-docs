# init(red:green:blue:)

**Framework**: Core Image  
**Kind**: init

Creates a color object using the specified RGB color component values

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)
```

#### Return Value

A Core Image color object that represents an RGB color in the color space specified by the Quartz 2D constant [`kCGColorSpaceGenericRGB`](https://developer.apple.com/documentation/CoreGraphics/kCGColorSpaceGenericRGB).

## See Also

- [convenience init(string: String)](cicolor/init(string:).md)
  Creates a color object using the RGBA color component values specified by a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(red:green:blue:))*