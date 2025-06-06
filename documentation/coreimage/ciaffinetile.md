# CIAffineTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure an affine tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIAffineTile
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciaffinetile/3228057-inputimage.md)
  The image to use as an input image.
- [var transform: CGAffineTransform](ciaffinetile/3228058-transform.md)
  The transform to apply to the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func affineTile() -> any CIFilter & CIAffineTile](cifilter/3228266-affinetile.md)
  Performs a transform on the image and tiles the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciaffinetile)*