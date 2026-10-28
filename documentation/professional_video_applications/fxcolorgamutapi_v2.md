# FxColorGamutAPI_v2

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol that handles plug-in queries to the host for the project’s color gamut.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxColorGamutAPI_v2
```

```objc
@protocol FxColorGamutAPI_v2
```

## Mentions

- [Managing color space and gamut in plug-ins](../Professional-Video-Applications/managing-color-space-and-gamut-in-plug-ins.md)

## Overview

The `FxColorGamutAPI` retrieves the matrices for converting between RGB (in the project’s color gamut) and YCbCr. Use this protocol when your plug-in converts to YCbCr or from color pixels to grayscale.

> **Note**:  This is version 2 of the Color Gamut API and does not require `FxTime`.

## Topics

### Getting Color Gamut Information
- [func colorMatrixFromDesiredRGBToYCbCr() -> FxMatrix44!](./fxcolorgamutapi_v2/colormatrixfromdesiredrgbtoycbcr%28%29.md)
  Returns a color matrix that is appropriate for converting RGB values in the project’s working gamut into YCbCr values.
- [func colorMatrixFromYCbCrToDesiredRGB() -> FxMatrix44!](./fxcolorgamutapi_v2/colormatrixfromycbcrtodesiredrgb%28%29.md)
  Returns a color matrix that is appropriate for converting RGB values from YCbCr to an RGB value in the project’s working gamut.
- [func colorPrimaries() -> FxColorPrimaries](./fxcolorgamutapi_v2/colorprimaries%28%29.md)
  Provides an enumerated type that describes the color primaries of the project’s working gamut.
### Constants
- [typealias FxColorPrimaries](./fxcolorprimaries.md)
  Constants used to describe a set of color primaries.

## See Also

### Color
- [Managing color space and gamut in plug-ins](../Professional-Video-Applications/managing-color-space-and-gamut-in-plug-ins.md)
  Control the appearance of your rendering by using the color gamut API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcolorgamutapi_v2)*