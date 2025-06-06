# CIColorCubeWithColorSpace

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color cube with color space filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorCubeWithColorSpace
```

## Topics

### Instance Properties
- [var colorSpace: CGColorSpace?](cicolorcubewithcolorspace/3228138-colorspace.md)
  The working color space.
- [var cubeData: Data](cicolorcubewithcolorspace/3228139-cubedata.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](cicolorcubewithcolorspace/3228140-cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var inputImage: CIImage?](cicolorcubewithcolorspace/3228141-inputimage.md)
  The image to use as an input image.
- [var extrapolate: Bool](cicolorcubewithcolorspace/4401823-extrapolate.md)

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorCubeWithColorSpace() -> any CIFilter & CIColorCubeWithColorSpace](cifilter/3228288-colorcubewithcolorspace.md)
  Adjusts an image’s pixels using a three-dimensional color table in specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcubewithcolorspace)*