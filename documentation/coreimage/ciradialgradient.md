# CIRadialGradient

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a radial gradient filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIRadialGradient : CIFilterProtocol
```

## Topics

### Instance Properties
- [var center: CGPoint](ciradialgradient/center.md)
  The center of the effect as x and y coordinates.
- [var color0: CIColor](ciradialgradient/color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](ciradialgradient/color1.md)
  The second color to use in the gradient.
- [var radius0: Float](ciradialgradient/radius0.md)
  The radius of the starting circle to use in the gradient.
- [var radius1: Float](ciradialgradient/radius1.md)
  The radius of the ending circle to use in the gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func radialGradient() -> any CIFilter & CIRadialGradient](cifilter-swift.class/radialgradient.md)
  Generates a gradient that varies radially between two circles having the same center.
- [protocol CIGaussianGradient](cigaussiangradient.md)
  The properties you use to configure a Gaussian gradient filter.
- [protocol CIHueSaturationValueGradient](cihuesaturationvaluegradient.md)
  The properties you use to configure a hue-saturation-value gradient filter.
- [protocol CILinearGradient](cilineargradient.md)
  The properties you use to configure a linear gradient filter.
- [protocol CISmoothLinearGradient](cismoothlineargradient.md)
  The properties you use to configure a smooth linear gradient filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciradialgradient)*