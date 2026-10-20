# kVTDecompressionPropertyKey_PixelTransferProperties

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kVTDecompressionPropertyKey_PixelTransferProperties;
```

#### Discussion

This property value is a [`CFDictionary`](../CoreFoundation/cfdictionary.md) object containing properties from `VTPixelTransferProperties.h`.

## See Also

### Post-Decompression Processing
- [let kVTDecompressionPropertyKey_DecoderProducesRAWOutput: CFString](./kvtdecompressionpropertykey_decoderproducesrawoutput.md)
  A value that indicates whether the decoder can produce RAW output requiring a RAW processing session for post-decode processing.
- [let kVTDecompressionPropertyKey_GeneratePerFrameHDRDisplayMetadata: CFString](./kvtdecompressionpropertykey_generateperframehdrdisplaymetadata.md)
  A key that indicates to generate per frame HDR Metadata and attach it to the resulting decoded pixel buffers.
- [let kVTDecompressionPropertyKey_PropagatePerFrameHDRDisplayMetadata: CFString](./kvtdecompressionpropertykey_propagateperframehdrdisplaymetadata.md)
- [let kVTDecompressionPropertyKey_RequestRAWOutput: CFString](./kvtdecompressionpropertykey_requestrawoutput.md)
  For decoders that produce RAW output, this property requests that the decompression session provides unprocessed output.
- [let kVTDecompressionPropertyKey_UsingGPURegistryID: CFString](./kvtdecompressionpropertykey_usinggpuregistryid.md)
- [let kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID: CFString](./kvtvideodecoderspecification_preferreddecodergpuregistryid.md)
- [let kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID: CFString](./kvtvideodecoderspecification_requireddecodergpuregistryid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_pixeltransferproperties)*