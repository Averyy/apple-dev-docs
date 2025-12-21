# CIGaussianGradient

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a Gaussian gradient filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIGaussianGradient : CIFilterProtocol
```

## Topics

### Instance Properties
- [var center: CGPoint](cigaussiangradient/center.md)
  The center of the effect as x and y coordinates.
- [var color0: CIColor](cigaussiangradient/color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](cigaussiangradient/color1.md)
  The second color to use in the gradient.
- [var radius: Float](cigaussiangradient/radius.md)
  The radius of the Gaussian distribution.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](cifilter-swift.class/gaussiangradient.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.
- [protocol CIHueSaturationValueGradient](cihuesaturationvaluegradient.md)
  The properties you use to configure a hue-saturation-value gradient filter.
- [protocol CILinearGradient](cilineargradient.md)
  The properties you use to configure a linear gradient filter.
- [protocol CIRadialGradient](ciradialgradient.md)
  The properties you use to configure a radial gradient filter.
- [protocol CISmoothLinearGradient](cismoothlineargradient.md)
  The properties you use to configure a smooth linear gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cigaussiangradient)*