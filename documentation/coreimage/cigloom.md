# CIGloom

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a gloom filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIGloom
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cigloom/3228477-inputimage.md)
  The image to use as an input image.
- [var intensity: Float](cigloom/3228478-intensity.md)
  The intensity of the effect.
- [var radius: Float](cigloom/3228479-radius.md)
  The radius, in pixels, of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func gloom() -> any CIFilter & CIGloom](cifilter/3228334-gloom.md)
  Adjusts an image’s color by applying a gloom filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cigloom)*