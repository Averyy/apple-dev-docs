# kVTCompressionPropertyKey_Depth

**Framework**: Video Toolbox  
**Kind**: var

The pixel depth of the encoded video.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_Depth: CFString
```

#### Discussion

This property is only supported by video encoders for formats that are tied to particular pixel formats (for example, 16-bit RGB, 24-bit RGB).

## See Also

- [let kVTCompressionPropertyKey_PreserveAlphaChannel: CFString](kvtcompressionpropertykey_preservealphachannel.md)
  A key that specifies whether to encode the alpha channel of input video frames.
- [let kVTCompressionPropertyKey_H264EntropyMode: CFString](kvtcompressionpropertykey_h264entropymode.md)
  The entropy encoding mode for H.264 compression.
- [let kVTCompressionPropertyKey_HDRMetadataInsertionMode: CFString](kvtcompressionpropertykey_hdrmetadatainsertionmode.md)
- [let kVTCompressionPropertyKey_OutputBitDepth: CFString](kvtcompressionpropertykey_outputbitdepth.md)
- [let kVTCompressionPropertyKey_ProfileLevel: CFString](kvtcompressionpropertykey_profilelevel.md)
  The profile and level for the encoded bitstream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_depth)*