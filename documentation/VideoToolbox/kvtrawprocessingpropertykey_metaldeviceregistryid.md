# kVTRAWProcessingPropertyKey_MetalDeviceRegistryID

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

This property requests that the Metal device corresponding to the specified registryID be used for any Metal related processing.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern CFStringRef const kVTRAWProcessingPropertyKey_MetalDeviceRegistryID;
```

## Discussion

This property is not supported by all RAW processors.

## See Also

### Properties
- [let kVTRAWProcessingPropertyKey_OutputColorAttachments: CFString!](./kvtrawprocessingpropertykey_outputcolorattachments.md)
  The color-related image buffer keys and values that will be attachments to the returned pixel buffers.
- [let kVTRAWProcessingPropertyKey_MetadataForSidecarFile: CFString!](./kvtrawprocessingpropertykey_metadataforsidecarfile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtrawprocessingpropertykey_metaldeviceregistryid)*