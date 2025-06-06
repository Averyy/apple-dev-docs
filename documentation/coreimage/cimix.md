# CIMix

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a mix filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIMix
```

## Topics

### Instance Properties
- [var amount: Float](cimix/3228565-amount.md)
  The amount of the effect.
- [var backgroundImage: CIImage?](cimix/3228566-backgroundimage.md)
  The image to use as a background image.
- [var inputImage: CIImage?](cimix/3228567-inputimage.md)
  The image to use as a foreground image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func mix() -> any CIFilter & CIMix](cifilter/3228362-mix.md)
  Blends two images together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimix)*