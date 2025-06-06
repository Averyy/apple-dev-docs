# CIColorPolynomial

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color polynomial filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorPolynomial
```

## Topics

### Instance Properties
- [var alphaCoefficients: CIVector](cicolorpolynomial/3228171-alphacoefficients.md)
  Polynomial coefficients for the alpha channel.
- [var blueCoefficients: CIVector](cicolorpolynomial/3228172-bluecoefficients.md)
  Polynomial coefficients for the blue channel.
- [var greenCoefficients: CIVector](cicolorpolynomial/3228173-greencoefficients.md)
  Polynomial coefficients for the green channel.
- [var inputImage: CIImage?](cicolorpolynomial/3228174-inputimage.md)
  The image to use as an input image.
- [var redCoefficients: CIVector](cicolorpolynomial/3228175-redcoefficients.md)
  Polynomial coefficients for the red channel.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorPolynomial() -> any CIFilter & CIColorPolynomial](cifilter/3228296-colorpolynomial.md)
  Alters an image’s colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorpolynomial)*