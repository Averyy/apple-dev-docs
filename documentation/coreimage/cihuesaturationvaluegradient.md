# CIHueSaturationValueGradient

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a hue-saturation-value gradient filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIHueSaturationValueGradient
```

## Topics

### Instance Properties
- [var colorSpace: CGColorSpace?](cihuesaturationvaluegradient/3228502-colorspace.md)
  The color space for the generated color wheel.
- [var dither: Float](cihuesaturationvaluegradient/3228503-dither.md)
  A Boolean value specifying whether the dither the generated output.
- [var radius: Float](cihuesaturationvaluegradient/3228504-radius.md)
  The distance from the center of the effect.
- [var softness: Float](cihuesaturationvaluegradient/3228505-softness.md)
  The softness of the generated color wheel.
- [var value: Float](cihuesaturationvaluegradient/3228506-value.md)
  The lightness of the hue-saturation gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func hueSaturationValueGradient() -> any CIFilter & CIHueSaturationValueGradient](cifilter/3228342-huesaturationvaluegradient.md)
  Generates a gradient representing a specified color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cihuesaturationvaluegradient)*