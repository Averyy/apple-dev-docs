# kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata

**Framework**: Video Toolbox  
**Kind**: var

A key that indicates to generate per frame HDR Metadata and attach it to the resulting decoded pixel buffers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata: CFString
```

#### Discussion

If the color space and YCbCr matrix match a supported HDR format such as HLG ([`kCMFormatDescriptionTransferFunction_ITU_R_2100_HLG`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionTransferFunction_ITU_R_2100_HLG)) the system analyzes the decoded frame and adds the metadata as an attachment to the pixel buffers.

## See Also

- [let kVTDecompressionPropertyKey_PixelTransferProperties: CFString](kvtdecompressionpropertykey_pixeltransferproperties.md)
  Specific pixel transfer features to be used during decompression.
- [let kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_requireddecodergpuregistryid.md)
- [let kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID: CFString](kvtvideodecoderspecification_preferreddecodergpuregistryid.md)
- [let kVTDecompressionPropertyKey_UsingGPURegistryID: CFString](kvtdecompressionpropertykey_usinggpuregistryid.md)
- [let kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata: CFString](kvtdecompressionpropertykey_propagateperframehdrdisplaymetadata.md)
- [let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString](kvtdecompressionpropertykey_decoderproducesrawoutput.md)
- [let kVTDecompressionPropertyKey_RequestRAWOutput: CFString](kvtdecompressionpropertykey_requestrawoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_generateperframehdrdisplaymetadata)*