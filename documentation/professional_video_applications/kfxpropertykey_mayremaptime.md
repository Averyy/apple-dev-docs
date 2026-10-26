# kFxPropertyKey_MayRemapTime

**Framework**: Professional Video Applications  
**Kind**: var  
**Role**: Global Variable

A Boolean value, encoded as an `NSNumber` object, indicating whether or not this plug-in may try to sample its input image(s) at any time other than the output time.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
var kFxPropertyKey_MayRemapTime: String { get }
```

```c
#define kFxPropertyKey_MayRemapTime
```

## Mentions

- [Building an FxPlug plug-in manually](../Professional-Video-Applications/building-an-fxplug-plug-in-manually.md)

#### Discussion

The default value is [`true`](../Swift/true.md).

## See Also

### Constants
- [var kFxPropertyKey_DrawsInScreenSpace: String](./kfxpropertykey_drawsinscreenspace.md)
  Indicates that the filter or generator requires that its output to always be aligned with the camera’s film-back.
- [var kFxPropertyKey_PixelTransformSupport: String](./kfxpropertykey_pixeltransformsupport.md)
  A key in the `properties` dictionary in the `FXBaseEffect` Class that corresponds to an `NSNumber` containing one of the `FxImage` values. The default value is [`kFxPixelTransform_ScaleTranslate`](./kfxpixeltransform_scaletranslate.md)
- [var kFxPropertyKey_UsesNonmatchingTextureLayout: String](./kfxpropertykey_usesnonmatchingtexturelayout.md)
- [PluginManagerVersionNumber](./pluginmanagerversionnumber.md)
- [PluginManagerVersionString](./pluginmanagerversionstring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_mayremaptime)*