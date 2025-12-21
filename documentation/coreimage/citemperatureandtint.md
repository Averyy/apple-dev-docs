# CITemperatureAndTint

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a temperature and tint filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CITemperatureAndTint : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](citemperatureandtint/inputimage.md)
  The image to use as an input image.
- [var neutral: CIVector](citemperatureandtint/neutral.md)
  A vector containing the source white point defined by color temperature and tint.
- [var targetNeutral: CIVector](citemperatureandtint/targetneutral.md)
  A vector containing the desired white point defined by color temperature and tint.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter-swift.class/temperatureandtint.md)
  Alters an image’s temperature and tint.
- [protocol CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [protocol CIColorClamp](cicolorclamp.md)
  The properties you use to configure a color clamp filter.
- [protocol CIColorControls](cicolorcontrols.md)
  The properties you use to configure a color controls filter.
- [protocol CIColorMatrix](cicolormatrix.md)
  The properties you use to configure a color matrix filter.
- [protocol CIColorPolynomial](cicolorpolynomial.md)
  The properties you use to configure a color polynomial filter.
- [protocol CIColorThreshold](cicolorthreshold.md)
- [protocol CIColorThresholdOtsu](cicolorthresholdotsu.md)
- [protocol CIDepthToDisparity](cidepthtodisparity.md)
  The properties you use to configure a depth-to-disparity filter.
- [protocol CIDisparityToDepth](cidisparitytodepth.md)
  The properties you use to configure a disparity-to-depth filter.
- [protocol CIExposureAdjust](ciexposureadjust.md)
  The properties you use to configure an exposure adjust filter.
- [protocol CIGammaAdjust](cigammaadjust.md)
  The properties you use to configure a gamma adjust filter.
- [protocol CIHueAdjust](cihueadjust.md)
  The properties you use to configure a hue adjust filter.
- [protocol CILinearToSRGBToneCurve](cilineartosrgbtonecurve.md)
  The properties you use to configure a linear-to-sRGB filter.
- [protocol CISRGBToneCurveToLinear](cisrgbtonecurvetolinear.md)
  The properties you use to configure an sRGB-to-linear filter.
- [protocol CISystemToneMap](cisystemtonemap.md)
  The protocol for the System Tone Map filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citemperatureandtint)*