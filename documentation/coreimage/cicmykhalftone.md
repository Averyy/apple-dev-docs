# CICMYKHalftone

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a CMYK halftone filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CICMYKHalftone
```

## Topics

### Instance Properties
- [var angle: Float](cicmykhalftone/3228097-angle.md)
  The angle of the pattern.
- [var center: CGPoint](cicmykhalftone/3228098-center.md)
  The x and y position to use as the center of the halftone pattern.
- [var grayComponentReplacement: Float](cicmykhalftone/3228099-graycomponentreplacement.md)
  The gray component replacement value.
- [var inputImage: CIImage?](cicmykhalftone/3228100-inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cicmykhalftone/3228101-sharpness.md)
  The sharpness of the pattern.
- [var underColorRemoval: Float](cicmykhalftone/3228102-undercolorremoval.md)
  The under color removal value.
- [var width: Float](cicmykhalftone/3228103-width.md)
  The distance between dots in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func cmykHalftone() -> any CIFilter & CICMYKHalftone](cifilter/3228259-cmykhalftone.md)
  Adds a series of colorful dots to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicmykhalftone)*