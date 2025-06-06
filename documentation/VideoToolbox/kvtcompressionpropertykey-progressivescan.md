# kVTCompressionPropertyKey_ProgressiveScan

**Framework**: Videotoolbox  
**Kind**: var

A Boolean value indicating whether the DV video stream should have the progressive flag set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_ProgressiveScan: CFString
```

#### Discussion

This property is supported by the DV25/50 family of encoders. If false, content is encoded as interlaced. If true, content is encoded as progressive. The value of this property fixes the [`kVTCompressionPropertyKey_FieldCount`](kvtcompressionpropertykey_fieldcount.md) and [`kVTCompressionPropertyKey_FieldDetail`](kvtcompressionpropertykey_fielddetail.md) properties.

## See Also

- [let kVTCompressionPropertyKey_AspectRatio16x9: CFString](kvtcompressionpropertykey_aspectratio16x9.md)
  A Boolean value indicating whether the DV video stream should have the 16x9 flag set.
- [let kVTCompressionPropertyKey_CleanAperture: CFString](kvtcompressionpropertykey_cleanaperture.md)
  The clean aperture for encoded frames.
- [let kVTCompressionPropertyKey_FieldCount: CFString](kvtcompressionpropertykey_fieldcount.md)
  The field count indicating whether the frames should be encoded progressive (1) or interlaced (2).
- [let kVTCompressionPropertyKey_FieldDetail: CFString](kvtcompressionpropertykey_fielddetail.md)
  Field ordering for encoded interlaced frames.
- [let kVTCompressionPropertyKey_PixelAspectRatio: CFString](kvtcompressionpropertykey_pixelaspectratio.md)
  The pixel aspect ratio for encoded frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_progressivescan)*