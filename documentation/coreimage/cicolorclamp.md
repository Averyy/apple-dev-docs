# CIColorClamp

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color clamp filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorClamp
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cicolorclamp/3228120-inputimage.md)
  The image to use as an input image.
- [var maxComponents: CIVector](cicolorclamp/3228121-maxcomponents.md)
  A vector containing the higher clamping values.
- [var minComponents: CIVector](cicolorclamp/3228122-mincomponents.md)
  A vector containing the lower clamping values.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorClamp() -> any CIFilter & CIColorClamp](cifilter/3228284-colorclamp.md)
  Alters the colors in an image based on color components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorclamp)*