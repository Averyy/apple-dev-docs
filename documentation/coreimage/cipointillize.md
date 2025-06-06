# CIPointillize

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a pointillize filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPointillize
```

## Topics

### Instance Properties
- [var center: CGPoint](cipointillize/3228678-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cipointillize/3228679-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cipointillize/3228680-radius.md)
  The radius of the circles in the resulting pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func pointillize() -> any CIFilter & CIPointillize](cifilter/3228394-pointillize.md)
  Applies a pointillize effect to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipointillize)*