# CIColorCrossPolynomial

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color cross-polynomial filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorCrossPolynomial
```

## Topics

### Instance Properties
- [var blueCoefficients: CIVector](cicolorcrosspolynomial/3228129-bluecoefficients.md)
  Polynomial coefficients for the blue channel.
- [var greenCoefficients: CIVector](cicolorcrosspolynomial/3228130-greencoefficients.md)
  Polynomial coefficients for the green channel.
- [var inputImage: CIImage?](cicolorcrosspolynomial/3228131-inputimage.md)
  The image to use as an input image.
- [var redCoefficients: CIVector](cicolorcrosspolynomial/3228132-redcoefficients.md)
  Polynomial coefficients for the red channel.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorCrossPolynomial() -> any CIFilter & CIColorCrossPolynomial](cifilter/3228286-colorcrosspolynomial.md)
  Adjusts an image’s color by applying polynomial cross-products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcrosspolynomial)*