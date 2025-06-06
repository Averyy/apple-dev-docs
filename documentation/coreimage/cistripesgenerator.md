# CIStripesGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a stripes generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIStripesGenerator
```

## Topics

### Instance Properties
- [var center: CGPoint](cistripesgenerator/3228761-center.md)
  The x and y position to use as the center of the stripe pattern.
- [var color0: CIColor](cistripesgenerator/3228762-color0.md)
  A color to use for the odd stripes.
- [var color1: CIColor](cistripesgenerator/3228763-color1.md)
  A color to use for the even stripes.
- [var sharpness: Float](cistripesgenerator/3228764-sharpness.md)
  The sharpness of the stripe pattern.
- [var width: Float](cistripesgenerator/3228765-width.md)
  The width of a stripe.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](cifilter/3228417-stripesgenerator.md)
  Generates a line of stripes as an image


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cistripesgenerator)*