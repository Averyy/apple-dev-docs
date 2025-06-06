# CIColorControls

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color controls filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorControls
```

## Topics

### Instance Properties
- [var brightness: Float](cicolorcontrols/3228124-brightness.md)
  The amount of brightness to apply.
- [var contrast: Float](cicolorcontrols/3228125-contrast.md)
  The amount of contrast to apply.
- [var inputImage: CIImage?](cicolorcontrols/3228126-inputimage.md)
  The image to use as an input image.
- [var saturation: Float](cicolorcontrols/3228127-saturation.md)
  The amount of saturation to apply.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorControls() -> any CIFilter & CIColorControls](cifilter/3228285-colorcontrols.md)
  Alters the brightness, contrast, and saturation of an image’s colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcontrols)*