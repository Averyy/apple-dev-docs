# CIBokehBlur

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a bokeh blur filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIBokehBlur
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cibokehblur/3228088-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cibokehblur/3228089-radius.md)
  The radius of the blur, in pixels.
- [var ringAmount: Float](cibokehblur/3228090-ringamount.md)
  The amount of extra emphasis at the ring of the bokeh.
- [var ringSize: Float](cibokehblur/3228091-ringsize.md)
  The radius of the extra emphasis at the ring of the bokeh.
- [var softness: Float](cibokehblur/3228092-softness.md)
  The softness of the bokeh effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func bokehBlur() -> any CIFilter & CIBokehBlur](cifilter/3228277-bokehblur.md)
  Applies a bokeh effect to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibokehblur)*