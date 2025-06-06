# kFxPropertyKey_VariesWhenParamsAreStatic

**Framework**: Professional Video Applications  
**Kind**: var

A key that determines whether your rendering varies even when the parameters remain the same.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
var kFxPropertyKey_VariesWhenParamsAreStatic: String { get }
```

## Mentions

- [Building an FxPlug plug-in manually](../professional-video-applications/building-an-fxplug-plug-in-manually.md)

#### Discussion

The value for this key is a Boolean `NSNumber` indicating whether this effect changes its rendering even when the parameters don’t change. This can happen if your rendering is based on timing in addition to parameters, for example. Note that this property is only checked once when the filter is applied, so it should go in static properties rather than dynamic properties.

## See Also

- [var kFxPropertyKey_NeedsFullBuffer: String](kfxpropertykey_needsfullbuffer.md)
  A key that determines whether the plug-in needs the entire image to do its processing, and can’t tile its rendering.
- [var kFxPropertyKey_ChangesOutputSize: String](kfxpropertykey_changesoutputsize.md)
  A key that determines whether your filter has the ability to change the size of its output to be different than the size of its input.
- [var kFxPropertyKey_DesiredProcessingColorInfo: String](kfxpropertykey_desiredprocessingcolorinfo.md)
  A key that determines whether your plug-in renders in linear or gamma-corrected color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_varieswhenparamsarestatic)*