# CIShadedMaterial

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a shaded material filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIShadedMaterial
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cishadedmaterial/3228705-inputimage.md)
  The image to use as an input image.
- [var scale: Float](cishadedmaterial/3228706-scale.md)
  The scale of the effect.
- [var shadingImage: CIImage?](cishadedmaterial/3228707-shadingimage.md)
  The image to use as the height field.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func shadedMaterial() -> any CIFilter & CIShadedMaterial](cifilter/3228403-shadedmaterial.md)
  Creates a shaded image from a height-field image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cishadedmaterial)*