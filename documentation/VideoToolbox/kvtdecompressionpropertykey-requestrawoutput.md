# kVTDecompressionPropertyKey_RequestRAWOutput

**Framework**: Videotoolbox  
**Kind**: var

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_RequestRAWOutput: CFString
```

#### Discussion

```not specified
@constant       kVTDecompressionPropertyKey_RequestRAWOutput
@abstract
	For decoders which produce RAW output, this property requests that the VTDecompressionSession provide output which has not been processed.
@discussion
	When a decoder produces RAW output (signalled by kVTDecompressionPropertyKey_DecoderProducesRAWOutput) the VTDecompressionSession will automatically
	invoke a VTRAWProcessingSession with default settings and emit processed frames by default, or when kVTDecompressionPropertyKey_RequestRAWOutput is set
	to kCFBooleanFalse.
	If a client wants to run a VTRAWProcessingSession on the RAW output themselves in order to control the post-decode processing of the decoded CVPixelBuffers,
	they must set kVTDecompressionPropertyKey_RequestRAWOutput to kCFBooleanTrue.
	If kVTDecompressionPropertyKey_RequestRAWOutput has been enabled and the decoder produces RAW output, the VTDecompressionSession 
	will return CVPixelBuffers in the decoder's native RAW format.  Any destinationImageBufferAttributes set on the VTDecompressionSession will be ignored.
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
- [let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString](kvtdecompressionpropertykey_decoderproducesrawoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_requestrawoutput)*