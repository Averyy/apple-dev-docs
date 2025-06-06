# CIMaskedVariableBlur

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a masked variable blur filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIMaskedVariableBlur
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cimaskedvariableblur/3228551-inputimage.md)
  The image to use as an input image.
- [var mask: CIImage?](cimaskedvariableblur/3228552-mask.md)
  A grayscale mask that defines the blur amount.
- [var radius: Float](cimaskedvariableblur/3228553-radius.md)
  The distance from the center of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func maskedVariableBlur() -> any CIFilter & CIMaskedVariableBlur](cifilter/3228355-maskedvariableblur.md)
  Blurs a specified portion of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimaskedvariableblur)*