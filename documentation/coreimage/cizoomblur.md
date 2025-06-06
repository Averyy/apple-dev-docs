# CIZoomBlur

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a zoom blur filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIZoomBlur
```

## Topics

### Instance Properties
- [var amount: Float](cizoomblur/3228841-amount.md)
   The zoom-in amount.
- [var center: CGPoint](cizoomblur/3228842-center.md)
  The center of the effect, as x and y coordinates.
- [var inputImage: CIImage?](cizoomblur/3228843-inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func zoomBlur() -> any CIFilter & CIZoomBlur](cifilter/3228434-zoomblur.md)
  Creates a zoom blur centered around a single point on the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cizoomblur)*