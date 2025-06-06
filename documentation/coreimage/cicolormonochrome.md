# CIColorMonochrome

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color monochrome filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorMonochrome
```

## Topics

### Instance Properties
- [var color: CIColor](cicolormonochrome/3228167-color.md)
  The monochrome color to apply to the image.
- [var inputImage: CIImage?](cicolormonochrome/3228168-inputimage.md)
  The image to use as an input image.
- [var intensity: Float](cicolormonochrome/3228169-intensity.md)
  The intensity of the monochrome effect. 

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorMonochrome() -> any CIFilter & CIColorMonochrome](cifilter/3228295-colormonochrome.md)
  Adjusts an image’s colors to shades of a single color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolormonochrome)*