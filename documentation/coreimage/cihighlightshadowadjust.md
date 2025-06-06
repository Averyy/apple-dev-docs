# CIHighlightShadowAdjust

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a highlight-shadow adjust filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIHighlightShadowAdjust
```

## Topics

### Instance Properties
- [var highlightAmount: Float](cihighlightshadowadjust/3228494-highlightamount.md)
  The amount of adjustment to the highlights in the image.
- [var inputImage: CIImage?](cihighlightshadowadjust/3228495-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cihighlightshadowadjust/3228496-radius.md)
  The shadow highlight radius.
- [var shadowAmount: Float](cihighlightshadowadjust/3228497-shadowamount.md)
  The amount of adjustment to the shadows in the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func highlightShadowAdjust() -> any CIFilter & CIHighlightShadowAdjust](cifilter/3228339-highlightshadowadjust.md)
  Adjusts the highlights of colors to reduce shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cihighlightshadowadjust)*