# CIAffineClamp

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure an affine clamp filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIAffineClamp
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciaffineclamp/3228054-inputimage.md)
  The image to use as an input image.
- [var transform: CGAffineTransform](ciaffineclamp/3228055-transform.md)
  The transform to apply to the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func affineClamp() -> any CIFilter & CIAffineClamp](cifilter/3228265-affineclamp.md)
  Performs a transform on the image and extends the image edges to infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciaffineclamp)*