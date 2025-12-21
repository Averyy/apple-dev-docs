# CILinearGradient

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a linear gradient filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CILinearGradient : CIFilterProtocol
```

## Topics

### Instance Properties
- [var color0: CIColor](cilineargradient/color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](cilineargradient/color1.md)
  The second color to use in the gradient.
- [var point0: CGPoint](cilineargradient/point0.md)
  The starting position of the gradient.
- [var point1: CGPoint](cilineargradient/point1.md)
  The ending position of the gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func linearGradient() -> any CIFilter & CILinearGradient](cifilter-swift.class/lineargradient.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.
- [protocol CIGaussianGradient](cigaussiangradient.md)
  The properties you use to configure a Gaussian gradient filter.
- [protocol CIHueSaturationValueGradient](cihuesaturationvaluegradient.md)
  The properties you use to configure a hue-saturation-value gradient filter.
- [protocol CIRadialGradient](ciradialgradient.md)
  The properties you use to configure a radial gradient filter.
- [protocol CISmoothLinearGradient](cismoothlineargradient.md)
  The properties you use to configure a smooth linear gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineargradient)*