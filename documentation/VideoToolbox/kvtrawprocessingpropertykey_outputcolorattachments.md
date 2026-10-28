# kVTRAWProcessingPropertyKey_OutputColorAttachments

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

The color-related image buffer keys and values that will be attachments to the returned pixel buffers.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTRAWProcessingPropertyKey_OutputColorAttachments: CFString!
```

```c
extern CFStringRef const kVTRAWProcessingPropertyKey_OutputColorAttachments;
```

## Discussion

This property may not be supported by all RAW Processors. Only color-related keys from `CVImageBuffer.h` are permitted in the returned dictionary.

## See Also

### Properties
- [let kVTRAWProcessingPropertyKey_MetadataForSidecarFile: CFString!](./kvtrawprocessingpropertykey_metadataforsidecarfile.md)
- [kVTRAWProcessingPropertyKey_MetalDeviceRegistryID](./kvtrawprocessingpropertykey_metaldeviceregistryid.md)
  This property requests that the Metal device corresponding to the specified registryID be used for any Metal related processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtrawprocessingpropertykey_outputcolorattachments)*