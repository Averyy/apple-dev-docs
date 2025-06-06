# CIColorCurves

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color curves filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorCurves
```

## Topics

### Instance Properties
- [var colorSpace: CGColorSpace?](cicolorcurves/3228150-colorspace.md)
  The working color space.
- [var curvesData: Data](cicolorcurves/3228151-curvesdata.md)
  Color values that determine the color curves transform.
- [var curvesDomain: CIVector](cicolorcurves/3228152-curvesdomain.md)
  A two-element vector that defines the minimum and maximum values of the curve data.
- [var inputImage: CIImage?](cicolorcurves/3228153-inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorCurves() -> any CIFilter & CIColorCurves](cifilter/3228290-colorcurves.md)
  Adjusts an image’s color curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcurves)*