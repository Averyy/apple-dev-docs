# kVTCompressionPropertyKey_H264EntropyMode

**Framework**: Video Toolbox  
**Kind**: var

The entropy encoding mode for H.264 compression.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_H264EntropyMode: CFString
```

#### Discussion

If supported by an H.264 encoder, this property controls whether the encoder should use Context-based Adaptive Variable Length Coding (CAVLC) or Context-based Adaptive Binary Arithmetic Coding (CABAC). CABAC generally gives better compression at the expense of higher computational overhead. The default value is encoder-specific and may change depending on other encoder settings.

> **Note**:  Changing the default entropy mode may result in a configuration that is not compatible with a requested Profile and Level.  Results in this case are undefined, and could include encode errors or a noncompliant output stream.

## Topics

### Entropy Modes
- [let kVTH264EntropyMode_CAVLC: CFString](kvth264entropymode_cavlc.md)
- [let kVTH264EntropyMode_CABAC: CFString](kvth264entropymode_cabac.md)

## See Also

- [let kVTCompressionPropertyKey_PreserveAlphaChannel: CFString](kvtcompressionpropertykey_preservealphachannel.md)
  A key that specifies whether to encode the alpha channel of input video frames.
- [let kVTCompressionPropertyKey_Depth: CFString](kvtcompressionpropertykey_depth.md)
  The pixel depth of the encoded video.
- [let kVTCompressionPropertyKey_HDRMetadataInsertionMode: CFString](kvtcompressionpropertykey_hdrmetadatainsertionmode.md)
- [let kVTCompressionPropertyKey_OutputBitDepth: CFString](kvtcompressionpropertykey_outputbitdepth.md)
- [let kVTCompressionPropertyKey_ProfileLevel: CFString](kvtcompressionpropertykey_profilelevel.md)
  The profile and level for the encoded bitstream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_h264entropymode)*