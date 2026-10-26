# kFxPropertyKey_DrawsInScreenSpace

**Framework**: Professional Video Applications  
**Kind**: var  
**Role**: Global Variable

Indicates that the filter or generator requires that its output to always be aligned with the camera’s film-back.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
var kFxPropertyKey_DrawsInScreenSpace: String { get }
```

```c
#define kFxPropertyKey_DrawsInScreenSpace
```

#### Discussion

This property indicates that the drawing space behaves as if the layer its applied to is always directly in front of the camera, even if the camera moves. This is a Boolean value encoded as an `NSNumber` object.

## See Also

### Constants
- [var kFxPropertyKey_MayRemapTime: String](./kfxpropertykey_mayremaptime.md)
  A Boolean value, encoded as an `NSNumber` object, indicating whether or not this plug-in may try to sample its input image(s) at any time other than the output time.
- [var kFxPropertyKey_PixelTransformSupport: String](./kfxpropertykey_pixeltransformsupport.md)
  A key in the `properties` dictionary in the `FXBaseEffect` Class that corresponds to an `NSNumber` containing one of the `FxImage` values. The default value is [`kFxPixelTransform_ScaleTranslate`](./kfxpixeltransform_scaletranslate.md)
- [var kFxPropertyKey_UsesNonmatchingTextureLayout: String](./kfxpropertykey_usesnonmatchingtexturelayout.md)
- [PluginManagerVersionNumber](./pluginmanagerversionnumber.md)
- [PluginManagerVersionString](./pluginmanagerversionstring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_drawsinscreenspace)*