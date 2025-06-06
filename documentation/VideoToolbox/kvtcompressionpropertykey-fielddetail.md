# kVTCompressionPropertyKey_FieldDetail

**Framework**: Videotoolbox  
**Kind**: var

Field ordering for encoded interlaced frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_FieldDetail: CFString
```

#### Discussion

If a video encoder enforces specific field ordering, this property will be read-only ([`VTSessionSetProperty(_:key:value:)`](vtsessionsetproperty(_:key:value:).md) returns [`kVTPropertyReadOnlyErr`](kvtpropertyreadonlyerr.md)). The field detail is set on the format description for output samples, and may affect source frame scaling. `NULL` is a valid value for this property.

## See Also

- [let kVTCompressionPropertyKey_AspectRatio16x9: CFString](kvtcompressionpropertykey_aspectratio16x9.md)
  A Boolean value indicating whether the DV video stream should have the 16x9 flag set.
- [let kVTCompressionPropertyKey_CleanAperture: CFString](kvtcompressionpropertykey_cleanaperture.md)
  The clean aperture for encoded frames.
- [let kVTCompressionPropertyKey_FieldCount: CFString](kvtcompressionpropertykey_fieldcount.md)
  The field count indicating whether the frames should be encoded progressive (1) or interlaced (2).
- [let kVTCompressionPropertyKey_PixelAspectRatio: CFString](kvtcompressionpropertykey_pixelaspectratio.md)
  The pixel aspect ratio for encoded frames.
- [let kVTCompressionPropertyKey_ProgressiveScan: CFString](kvtcompressionpropertykey_progressivescan.md)
  A Boolean value indicating whether the DV video stream should have the progressive flag set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_fielddetail)*