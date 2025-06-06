# kFxPropertyKey_DesiredProcessingColorInfo

**Framework**: Professional Video Applications  
**Kind**: var

A key that determines whether your plug-in renders in linear or gamma-corrected color space.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
var kFxPropertyKey_DesiredProcessingColorInfo: String { get }
```

## Mentions

- [Managing color space and gamut in plug-ins](../professional-video-applications/managing-color-space-and-gamut-in-plug-ins.md)

#### Discussion

The value for this key is an `NSUInteger` indicating the color space that the plug-in will process in. This color space is expressed as an [`FxImageColorInfo`](fximagecolorinfo.md) constant. If a plug-in includes this property, all inputs are in the specified color space, and the output must also be in this color space.

## See Also

- [var kFxPropertyKey_NeedsFullBuffer: String](kfxpropertykey_needsfullbuffer.md)
  A key that determines whether the plug-in needs the entire image to do its processing, and can’t tile its rendering.
- [var kFxPropertyKey_VariesWhenParamsAreStatic: String](kfxpropertykey_varieswhenparamsarestatic.md)
  A key that determines whether your rendering varies even when the parameters remain the same.
- [var kFxPropertyKey_ChangesOutputSize: String](kfxpropertykey_changesoutputsize.md)
  A key that determines whether your filter has the ability to change the size of its output to be different than the size of its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_desiredprocessingcolorinfo)*