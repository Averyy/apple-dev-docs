# CIDither

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a dither filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIDither
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cidither/3228225-inputimage.md)
  The image to use as an input image.
- [var intensity: Float](cidither/3228226-intensity.md)
  The intensity of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func dither() -> any CIFilter & CIDither](cifilter/3228315-dither.md)
  Applies randomized noise to produce a processed look.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidither)*