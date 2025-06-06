# CIBloom

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a bloom filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIBloom
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cibloom/3228084-inputimage.md)
  The image to use as an input image.
- [var intensity: Float](cibloom/3228085-intensity.md)
  The intensity of the effect.
- [var radius: Float](cibloom/3228086-radius.md)
  The radius, in pixels, of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func bloom() -> any CIFilter & CIBloom](cifilter/3228276-bloom.md)
  Adjusts an image’s colors by applying a blur effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibloom)*