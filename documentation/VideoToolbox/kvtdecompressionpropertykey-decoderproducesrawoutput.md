# kVTDecompressionPropertyKey_DecoderProducesRAWOutput

**Framework**: Videotoolbox  
**Kind**: var

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString
```

#### Discussion

```not specified
@constant       kVTDecompressionPropertyKey_DecoderProducesRAWOutput
@abstract
	Indicates whether the decoder can produce RAW output requiring a VTRAWProcessingSession for post-decode processing.
@discussion
	If this property is not implemented, it is assumed that the decoder does not produce RAW output.
	If the decoder reports that it produces RAW output the VTDecompressionSession will internally invoke a VTRAWProcessingSession by default to produce
	processed output.
	If the client sets kVTDecompressionPropertyKey_RequestRAWOutput, the VTDecompressionSession will do no processing and return the decoder's native RAW
	output, and any requested destinationImageBufferAttributes on the VTDecompressionSession will be ignored.
```

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_decoderproducesrawoutput)*