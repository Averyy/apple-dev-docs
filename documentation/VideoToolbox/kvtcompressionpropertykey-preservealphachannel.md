# kVTCompressionPropertyKey_PreserveAlphaChannel

**Framework**: Video Toolbox  
**Kind**: var

A key that specifies whether to encode the alpha channel of input video frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_PreserveAlphaChannel: CFString
```

#### Discussion

Set this property to false in cases where you’re not interested in preserving alpha, or if you know the alpha channel to be fully opaque.

This property isn’t supported by all encoders.

## See Also

- [let kVTCompressionPropertyKey_Depth: CFString](kvtcompressionpropertykey_depth.md)
  The pixel depth of the encoded video.
- [let kVTCompressionPropertyKey_H264EntropyMode: CFString](kvtcompressionpropertykey_h264entropymode.md)
  The entropy encoding mode for H.264 compression.
- [let kVTCompressionPropertyKey_HDRMetadataInsertionMode: CFString](kvtcompressionpropertykey_hdrmetadatainsertionmode.md)
- [let kVTCompressionPropertyKey_OutputBitDepth: CFString](kvtcompressionpropertykey_outputbitdepth.md)
- [let kVTCompressionPropertyKey_ProfileLevel: CFString](kvtcompressionpropertykey_profilelevel.md)
  The profile and level for the encoded bitstream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_preservealphachannel)*