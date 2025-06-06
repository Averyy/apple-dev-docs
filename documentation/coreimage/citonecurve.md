# CIToneCurve

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a tone curve filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIToneCurve
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](citonecurve/3228792-inputimage.md)
  The image to use as an input image.
- [var point0: CGPoint](citonecurve/3228793-point0.md)
  A vector containing the position of the first point of the tone curve.
- [var point1: CGPoint](citonecurve/3228794-point1.md)
  A vector containing the position of the second point of the tone curve.
- [var point2: CGPoint](citonecurve/3228795-point2.md)
  A vector containing the position of the third point of the tone curve.
- [var point3: CGPoint](citonecurve/3228796-point3.md)
  A vector containing the position of the fourth point of the tone curve.
- [var point4: CGPoint](citonecurve/3228797-point4.md)
  A vector containing the position of the fifth point of the tone curve.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func toneCurve() -> any CIFilter & CIToneCurve](cifilter/3228424-tonecurve.md)
  Alters an image’s tone curve according to a series of data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citonecurve)*