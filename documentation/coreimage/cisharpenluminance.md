# CISharpenLuminance

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a sharpen luminance filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CISharpenLuminance
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cisharpenluminance/3228709-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cisharpenluminance/3228710-radius.md)
  The distance from the center of the effect.
- [var sharpness: Float](cisharpenluminance/3228711-sharpness.md)
  The amount of sharpening to apply.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func sharpenLuminance() -> any CIFilter & CISharpenLuminance](cifilter/3228404-sharpenluminance.md)
  Applies a sharpening effect to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisharpenluminance)*