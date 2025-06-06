# CIDiscBlur

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a disc blur filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIDiscBlur
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cidiscblur/3228214-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cidiscblur/3228215-radius.md)
  The radius of the blur, in pixels.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func discBlur() -> any CIFilter & CIDiscBlur](cifilter/3228311-discblur.md)
  Applies a circle-shaped blur to an area of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidiscblur)*