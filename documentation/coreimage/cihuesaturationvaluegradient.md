# CIHueSaturationValueGradient

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a hue-saturation-value gradient filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIHueSaturationValueGradient : CIFilterProtocol
```

## Topics

### Instance Properties
- [var colorSpace: CGColorSpace?](cihuesaturationvaluegradient/colorspace.md)
  The color space for the generated color wheel.
- [var dither: Float](cihuesaturationvaluegradient/dither.md)
  A Boolean value specifying whether the dither the generated output.
- [var radius: Float](cihuesaturationvaluegradient/radius.md)
  The distance from the center of the effect.
- [var softness: Float](cihuesaturationvaluegradient/softness.md)
  The softness of the generated color wheel.
- [var value: Float](cihuesaturationvaluegradient/value.md)
  The lightness of the hue-saturation gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](cifilter-swift.class/huesaturationvaluegradient.md)
  Generates a gradient representing a specified color space.
- [protocol CIGaussianGradient](cigaussiangradient.md)
  The properties you use to configure a Gaussian gradient filter.
- [protocol CILinearGradient](cilineargradient.md)
  The properties you use to configure a linear gradient filter.
- [protocol CIRadialGradient](ciradialgradient.md)
  The properties you use to configure a radial gradient filter.
- [protocol CISmoothLinearGradient](cismoothlineargradient.md)
  The properties you use to configure a smooth linear gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cihuesaturationvaluegradient)*