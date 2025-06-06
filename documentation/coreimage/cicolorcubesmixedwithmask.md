# CIColorCubesMixedWithMask

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color cube mixed with mask filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorCubesMixedWithMask
```

## Topics

### Instance Properties
- [var colorSpace: CGColorSpace?](cicolorcubesmixedwithmask/3228143-colorspace.md)
  The working color space.
- [var cube0Data: Data](cicolorcubesmixedwithmask/3228144-cube0data.md)
  The cube texture data to use as a color lookup table.
- [var cube1Data: Data](cicolorcubesmixedwithmask/3228145-cube1data.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](cicolorcubesmixedwithmask/3228146-cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var inputImage: CIImage?](cicolorcubesmixedwithmask/3228147-inputimage.md)
  The image to use as an input image.
- [var maskImage: CIImage?](cicolorcubesmixedwithmask/3228148-maskimage.md)
  A masking image.
- [var extrapolate: Bool](cicolorcubesmixedwithmask/4401824-extrapolate.md)

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorCubesMixedWithMask() -> any CIFilter & CIColorCubesMixedWithMask](cifilter/3228289-colorcubesmixedwithmask.md)
  Alters an image’s pixels using a three-dimensional color tables and a mask image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcubesmixedwithmask)*