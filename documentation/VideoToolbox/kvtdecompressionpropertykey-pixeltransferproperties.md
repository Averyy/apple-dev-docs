# kVTDecompressionPropertyKey_PixelTransferProperties

**Framework**: Video Toolbox  
**Kind**: var

Specific pixel transfer features to be used during decompression.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_PixelTransferProperties: CFString
```

#### Discussion

This property value is a doc://com.apple.documentation/documentation/corefoundation/cfdictionary-rum object containing properties from `VTPixelTransferProperties.h`.

## See Also

- [let kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_requireddecodergpuregistryid.md)
- [let kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_preferreddecodergpuregistryid.md)
- [let kVTDecompressionPropertyKey_UsingGPURegistryID: CFString](kvtdecompressionpropertykey_usinggpuregistryid.md)
- [let kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_propagateperframehdrdisplaymetadata.md)
- [let kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_generateperframehdrdisplaymetadata.md)
  A key that indicates to generate per frame HDR Metadata and attach it to the resulting decoded pixel buffers.
- [let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString](kvtdecompressionpropertykey_decoderproducesrawoutput.md)
- [let kVTDecompressionPropertyKey_RequestRAWOutput: CFString](kvtdecompressionpropertykey_requestrawoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_pixeltransferproperties)*