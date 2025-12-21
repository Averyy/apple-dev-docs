# kVTDecompressionPropertyKey_RequestRAWOutput

**Framework**: Video Toolbox  
**Kind**: var

For decoders that produce RAW output, this property requests that the decompression session provides unprocessed output.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_RequestRAWOutput: CFString
```

#### Discussion

When a decoder produces RAW output the [`VTDecompressionSession`](vtdecompressionsession.md) automatically invokes a [`VTRAWProcessingSession`](vtrawprocessingsession.md) with default settings and emits processed frames by default, or when `kVTDecompressionPropertyKey_RequestRAWOutput` is set to `kCFBooleanFalse`. If you want to run a [`VTRAWProcessingSession`](vtrawprocessingsession.md) on the RAW output to control the post-decode processing of the decoded `CVPixelBuffer` objects, you must set `kVTDecompressionPropertyKey_RequestRAWOutput` to `kCFBooleanTrue`. If `kVTDecompressionPropertyKey_RequestRAWOutput` is enabled and the decoder produces RAW output, the [`VTDecompressionSession`](vtdecompressionsession.md) returns `CVPixelBuffer` objects in the decoder’s native RAW format, and ignores any specified image buffer attributes.

## See Also

- [let kVTDecompressionPropertyKey_PixelTransferProperties: CFString](kvtdecompressionpropertykey_pixeltransferproperties.md)
  Specific pixel transfer features to be used during decompression.
- [let kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_requireddecodergpuregistryid.md)
- [let kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_preferreddecodergpuregistryid.md)
- [let kVTDecompressionPropertyKey_UsingGPURegistryID: CFString](kvtdecompressionpropertykey_usinggpuregistryid.md)
- [let kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_propagateperframehdrdisplaymetadata.md)
- [let kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_generateperframehdrdisplaymetadata.md)
  A key that indicates to generate per frame HDR Metadata and attach it to the resulting decoded pixel buffers.
- [let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString](kvtdecompressionpropertykey_decoderproducesrawoutput.md)
  A value that indicates whether the decoder can produce RAW output requiring a RAW processing session for post-decode processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_requestrawoutput)*