# CIColorMatrix

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color matrix filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorMatrix
```

## Topics

### Instance Properties
- [var aVector: CIVector](cicolormatrix/3228160-avector.md)
  The amount of alpha to multiply the source color values by.
- [var bVector: CIVector](cicolormatrix/3228161-bvector.md)
  The amount of blue to multiply the source color values by.
- [var gVector: CIVector](cicolormatrix/3228162-gvector.md)
  The amount of green to multiply the source color values by.
- [var rVector: CIVector](cicolormatrix/3228163-rvector.md)
  The amount of red to multiply the source color values by.
- [var biasVector: CIVector](cicolormatrix/3228164-biasvector.md)
  A vector that’s added to each color component.
- [var inputImage: CIImage?](cicolormatrix/3228165-inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorMatrix() -> any CIFilter & CIColorMatrix](cifilter/3228294-colormatrix.md)
  Alters the colors in an image based on vectors provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolormatrix)*