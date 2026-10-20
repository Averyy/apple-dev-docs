# kVTCompressionPropertyKey_TransferFunction

**Framework**: Video Toolbox  
**Kind**: var

The transfer function for compressed content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_TransferFunction: CFString
```

#### Discussion

If the video encoder enforces specific colorimetry, this property will be read-only ([`VTSessionSetProperty(_:key:value:)`](vtsessionsetproperty(_:key:value:).md) will return [`kVTPropertyReadOnlyErr`](kvtpropertyreadonlyerr.md)). The value is set on the format description for output sample buffers.

## See Also

- [let kVTCompressionPropertyKey_AlphaChannelMode: CFString](kvtcompressionpropertykey_alphachannelmode.md)
- [let kVTCompressionPropertyKey_ColorPrimaries: CFString](kvtcompressionpropertykey_colorprimaries.md)
  The color primaries for compressed content.
- [let kVTCompressionPropertyKey_ContentLightLevelInfo: CFString](kvtcompressionpropertykey_contentlightlevelinfo.md)
- [let kVTCompressionPropertyKey_GammaLevel: CFString](kvtcompressionpropertykey_gammalevel.md)
- [let kVTCompressionPropertyKey_ICCProfile: CFString](kvtcompressionpropertykey_iccprofile.md)
  The ICC profile for compressed content.
- [let kVTCompressionPropertyKey_MasteringDisplayColorVolume: CFString](kvtcompressionpropertykey_masteringdisplaycolorvolume.md)
- [let kVTCompressionPropertyKey_YCbCrMatrix: CFString](kvtcompressionpropertykey_ycbcrmatrix.md)
  The YCbCr matrix for compressed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_transferfunction)*