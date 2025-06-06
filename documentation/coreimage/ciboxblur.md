# CIBoxBlur

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a box blur filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIBoxBlur
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciboxblur/3228094-inputimage.md)
  The image to use as an input image.
- [var radius: Float](ciboxblur/3228095-radius.md)
  The radius of the blur, in pixels.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func boxBlur() -> any CIFilter & CIBoxBlur](cifilter/3228278-boxblur.md)
  Applies a square-shaped blur to an area of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciboxblur)*