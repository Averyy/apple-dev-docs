# colorPrimaries()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an enumerated type that describes the color primaries of the project’s working gamut.

**Availability**:
- FxPlug 4.2.6+

## Declaration

```swift
func colorPrimaries() -> FxColorPrimaries
```

```objc
- (FxColorPrimaries) colorPrimaries;
```

## Mentions

- [Managing color space and gamut in plug-ins](../../Professional-Video-Applications/managing-color-space-and-gamut-in-plug-ins.md)

#### Return Value

An [`FxColorPrimaries`](../fxcolorprimaries.md) value that describes the project’s working gamut.

## See Also

### Getting Color Gamut Information
- [func colorMatrixFromDesiredRGBToYCbCr() -> FxMatrix44!](./colormatrixfromdesiredrgbtoycbcr%28%29.md)
  Returns a color matrix that is appropriate for converting RGB values in the project’s working gamut into YCbCr values.
- [func colorMatrixFromYCbCrToDesiredRGB() -> FxMatrix44!](./colormatrixfromycbcrtodesiredrgb%28%29.md)
  Returns a color matrix that is appropriate for converting RGB values from YCbCr to an RGB value in the project’s working gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcolorgamutapi_v2/colorprimaries())*