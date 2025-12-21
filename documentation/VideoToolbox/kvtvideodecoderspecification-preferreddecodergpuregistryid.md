# kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
let kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID: CFString
```

## See Also

- [let kVTDecompressionPropertyKey_PixelTransferProperties: CFString](kvtdecompressionpropertykey_pixeltransferproperties.md)
  Specific pixel transfer features to be used during decompression.
- [let kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_requireddecodergpuregistryid.md)
- [let kVTDecompressionPropertyKey_UsingGPURegistryID: CFString](kvtdecompressionpropertykey_usinggpuregistryid.md)
- [let kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_propagateperframehdrdisplaymetadata.md)
- [let kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_generateperframehdrdisplaymetadata.md)
  A key that indicates to generate per frame HDR Metadata and attach it to the resulting decoded pixel buffers.
- [let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString](kvtdecompressionpropertykey_decoderproducesrawoutput.md)
  A value that indicates whether the decoder can produce RAW output requiring a RAW processing session for post-decode processing.
- [let kVTDecompressionPropertyKey_RequestRAWOutput: CFString](kvtdecompressionpropertykey_requestrawoutput.md)
  For decoders that produce RAW output, this property requests that the decompression session provides unprocessed output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderspecification_preferreddecodergpuregistryid)*