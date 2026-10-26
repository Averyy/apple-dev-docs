# colorMatrixFromYCbCrToDesiredRGB()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a color matrix that is appropriate for converting RGB values from YCbCr to an RGB value in the project’s working gamut.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func colorMatrixFromYCbCrToDesiredRGB() -> FxMatrix44!
```

```objc
- (FxMatrix44 *) colorMatrixFromYCbCrToDesiredRGB;
```

## Mentions

- [Managing color space and gamut in plug-ins](../../Professional-Video-Applications/managing-color-space-and-gamut-in-plug-ins.md)

#### Return Value

A 4x4 matrix for converting an RGB value into YCbCr.

## See Also

### Getting Color Gamut Information
- [func colorMatrixFromDesiredRGBToYCbCr() -> FxMatrix44!](./colormatrixfromdesiredrgbtoycbcr%28%29.md)
  Returns a color matrix that is appropriate for converting RGB values in the project’s working gamut into YCbCr values.
- [func colorPrimaries() -> FxColorPrimaries](./colorprimaries%28%29.md)
  Provides an enumerated type that describes the color primaries of the project’s working gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcolorgamutapi_v2/colormatrixfromycbcrtodesiredrgb())*