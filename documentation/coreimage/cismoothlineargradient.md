# CISmoothLinearGradient

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a smooth linear gradient filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CISmoothLinearGradient : CIFilterProtocol
```

## Topics

### Instance Properties
- [var color0: CIColor](cismoothlineargradient/color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](cismoothlineargradient/color1.md)
  The second color to use in the gradient.
- [var point0: CGPoint](cismoothlineargradient/point0.md)
  The starting position of the gradient.
- [var point1: CGPoint](cismoothlineargradient/point1.md)
  The ending position of the gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](cifilter-swift.class/smoothlineargradient.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.
- [protocol CIGaussianGradient](cigaussiangradient.md)
  The properties you use to configure a Gaussian gradient filter.
- [protocol CIHueSaturationValueGradient](cihuesaturationvaluegradient.md)
  The properties you use to configure a hue-saturation-value gradient filter.
- [protocol CILinearGradient](cilineargradient.md)
  The properties you use to configure a linear gradient filter.
- [protocol CIRadialGradient](ciradialgradient.md)
  The properties you use to configure a radial gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cismoothlineargradient)*