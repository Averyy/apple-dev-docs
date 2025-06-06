# kFxPropertyKey_NeedsFullBuffer

**Framework**: Professional Video Applications  
**Kind**: var

A key that determines whether the plug-in needs the entire image to do its processing, and can’t tile its rendering.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
var kFxPropertyKey_NeedsFullBuffer: String { get }
```

## Mentions

- [Building an FxPlug plug-in manually](../professional-video-applications/building-an-fxplug-plug-in-manually.md)
- [Working with tiled images](../professional-video-applications/working-with-tiled-images.md)

#### Discussion

This value of this key is a Boolean `NSNumber` indicating whether this plug-in needs the entire image to do its processing. Note that setting this value to `YES` incurs a significant performance penalty and makes your plug-in unable to render large input images. The default value is `NO`.

## See Also

- [var kFxPropertyKey_VariesWhenParamsAreStatic: String](kfxpropertykey_varieswhenparamsarestatic.md)
  A key that determines whether your rendering varies even when the parameters remain the same.
- [var kFxPropertyKey_ChangesOutputSize: String](kfxpropertykey_changesoutputsize.md)
  A key that determines whether your filter has the ability to change the size of its output to be different than the size of its input.
- [var kFxPropertyKey_DesiredProcessingColorInfo: String](kfxpropertykey_desiredprocessingcolorinfo.md)
  A key that determines whether your plug-in renders in linear or gamma-corrected color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_needsfullbuffer)*