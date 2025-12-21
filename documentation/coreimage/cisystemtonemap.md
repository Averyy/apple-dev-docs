# CISystemToneMap

**Framework**: Core Image  
**Kind**: protocol

The protocol for the System Tone Map filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CISystemToneMap : CIFilterProtocol
```

#### Overview

Apply a global tone curve to an image that reduces colors of the input image to a desired dynamic range consistent with other frameworks.

## Topics

### Instance Properties
- [var displayHeadroom: Float](cisystemtonemap/displayheadroom.md)
  Specifies the current headroom of the intended display.
- [var inputImage: CIImage?](cisystemtonemap/inputimage.md)
  Specifies input image with content headroom and average light level properties.
- [var preferredDynamicRange: CIDynamicRangeOption?](cisystemtonemap/preferreddynamicrange.md)
  Specifies the preferred dynamic range behavior of the tone mapping. The value should be kCIDynamicRangeStandard, kCIDynamicRangeConstrainedHigh, kCIDynamicRangeHigh or nil.  If nil then it will behave as kCIDynamicRangeHigh.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

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
- [protocol CITemperatureAndTint](citemperatureandtint.md)
  The properties you use to configure a temperature and tint filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisystemtonemap)*