# kVTCompressionPropertyKey_AspectRatio16x9

**Framework**: Videotoolbox  
**Kind**: var

A Boolean value indicating whether the DV video stream should have the 16x9 flag set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_AspectRatio16x9: CFString
```

#### Discussion

This property is supported by the DV25/50 family of encoders.

When false, the picture aspect ratio is 4:3. When true, the picture aspect ratio is 16:9. Either way, a fixed aspect ratio is used (the specific value depends on whether the format is NTSC or PAL).

## See Also

- [let kVTCompressionPropertyKey_CleanAperture: CFString](kvtcompressionpropertykey_cleanaperture.md)
  The clean aperture for encoded frames.
- [let kVTCompressionPropertyKey_FieldCount: CFString](kvtcompressionpropertykey_fieldcount.md)
  The field count indicating whether the frames should be encoded progressive (1) or interlaced (2).
- [let kVTCompressionPropertyKey_FieldDetail: CFString](kvtcompressionpropertykey_fielddetail.md)
  Field ordering for encoded interlaced frames.
- [let kVTCompressionPropertyKey_PixelAspectRatio: CFString](kvtcompressionpropertykey_pixelaspectratio.md)
  The pixel aspect ratio for encoded frames.
- [let kVTCompressionPropertyKey_ProgressiveScan: CFString](kvtcompressionpropertykey_progressivescan.md)
  A Boolean value indicating whether the DV video stream should have the progressive flag set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_aspectratio16x9)*