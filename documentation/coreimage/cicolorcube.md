# CIColorCube

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color cube filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorCube
```

## Topics

### Instance Properties
- [var cubeData: Data](cicolorcube/3228134-cubedata.md)
  The cube texture data to use as a color lookup table.
- [var cubeDimension: Float](cicolorcube/3228135-cubedimension.md)
  The length, in texels, of each side of the cube texture.
- [var inputImage: CIImage?](cicolorcube/3228136-inputimage.md)
  The image to use as an input image.
- [var extrapolate: Bool](cicolorcube/4401822-extrapolate.md)

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorCube() -> any CIFilter & CIColorCube](cifilter/3228287-colorcube.md)
  Adjusts an image’s pixels using a three-dimensional color table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcube)*