# CIBlendWithMask

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a blend with mask filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIBlendWithMask
```

## Topics

### Instance Properties
- [var backgroundImage: CIImage?](ciblendwithmask/3228080-backgroundimage.md)
  The image to use as a background image.
- [var inputImage: CIImage?](ciblendwithmask/3228081-inputimage.md)
  The image to use as a foreground image.
- [var maskImage: CIImage?](ciblendwithmask/3228082-maskimage.md)
  A grayscale mask that defines the blend.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func blendWithMask() -> any CIFilter & CIBlendWithMask](cifilter/3228274-blendwithmask.md)
  Blends two images by using a mask image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendwithmask)*