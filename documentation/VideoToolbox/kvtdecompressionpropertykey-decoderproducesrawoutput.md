# kVTDecompressionPropertyKey_DecoderProducesRAWOutput

**Framework**: Video Toolbox  
**Kind**: var

A value that indicates whether the decoder can produce RAW output requiring a RAW processing session for post-decode processing.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString
```

#### Discussion

If this property isn’t implemented, it’s assumed that the decoder does not produce RAW output. If the decoder reports that it produces RAW output, the [`VTDecompressionSession`](vtdecompressionsession.md) internally invokes a [`VTRAWProcessingSession`](vtrawprocessingsession.md) by default to produce processed output.

If the client sets [`kVTDecompressionPropertyKey_RequestRAWOutput`](kvtdecompressionpropertykey_requestrawoutput.md), the [`VTDecompressionSession`](vtdecompressionsession.md) performs no processing and returns the decoder’s native RAW output, and ignores any requested image buffer attributes.

## See Also

- [let kVTDecompressionPropertyKey_PixelTransferProperties: CFString](kvtdecompressionpropertykey_pixeltransferproperties.md)
  Specific pixel transfer features to be used during decompression.
- [let kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_requireddecodergpuregistryid.md)
- [let kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_preferreddecodergpuregistryid.md)
- [let kVTDecompressionPropertyKey_UsingGPURegistryID: CFString](kvtdecompressionpropertykey_usinggpuregistryid.md)
- [let kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_propagateperframehdrdisplaymetadata.md)
- [let kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_generateperframehdrdisplaymetadata.md)
  A key that indicates to generate per frame HDR Metadata and attach it to the resulting decoded pixel buffers.
- [let kVTDecompressionPropertyKey_RequestRAWOutput: CFString](kvtdecompressionpropertykey_requestrawoutput.md)
  For decoders that produce RAW output, this property requests that the decompression session provides unprocessed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_decoderproducesrawoutput)*