# CIMorphologyMinimum

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a morphology minimum filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIMorphologyMinimum
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cimorphologyminimum/3228580-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cimorphologyminimum/3228581-radius.md)
  The radius of the circular morphological structuring element.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func morphologyMinimum() -> any CIFilter & CIMorphologyMinimum](cifilter/3228366-morphologyminimum.md)
  Blurs a circular area by reducing contrasting pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimorphologyminimum)*