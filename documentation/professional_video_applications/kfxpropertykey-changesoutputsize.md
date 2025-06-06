# kFxPropertyKey_ChangesOutputSize

**Framework**: Professional Video Applications  
**Kind**: var

A key that determines whether your filter has the ability to change the size of its output to be different than the size of its input.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
var kFxPropertyKey_ChangesOutputSize: String { get }
```

#### Discussion

The value of this key is a Boolean `NSNumber` that indicates whether your filter returns an output that has a different size than the input. If not, return `NO` and your filter’s [`destinationImageRect(_:sourceImages:destinationImage:pluginState:at:)`](fxtileableeffect/destinationimagerect(_:sourceimages:destinationimage:pluginstate:at:).md) method will not be called.

## See Also

- [var kFxPropertyKey_NeedsFullBuffer: String](kfxpropertykey_needsfullbuffer.md)
  A key that determines whether the plug-in needs the entire image to do its processing, and can’t tile its rendering.
- [var kFxPropertyKey_VariesWhenParamsAreStatic: String](kfxpropertykey_varieswhenparamsarestatic.md)
  A key that determines whether your rendering varies even when the parameters remain the same.
- [var kFxPropertyKey_DesiredProcessingColorInfo: String](kfxpropertykey_desiredprocessingcolorinfo.md)
  A key that determines whether your plug-in renders in linear or gamma-corrected color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_changesoutputsize)*