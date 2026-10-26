# kVTRAWProcessingPropertyKey_MetadataForSidecarFile

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS 26.0+

## Declaration

```swift
let kVTRAWProcessingPropertyKey_MetadataForSidecarFile: CFString!
```

```c
extern CFStringRef const kVTRAWProcessingPropertyKey_MetadataForSidecarFile;
```

#### Discussion

This property, if supported, returns the current processing metadata on the RAW Processor. The returned value can be used by the caller to create, or overwrite an existing sidecar file.

This property is not supported by all RAWProcessors. The metadata returned represents a fully-formed sidecar file, and should be compatible with the MediaExtension FormatReader.

## See Also

### Properties
- [let kVTRAWProcessingPropertyKey_OutputColorAttachments: CFString!](./kvtrawprocessingpropertykey_outputcolorattachments.md)
  The color-related image buffer keys and values that will be attachments to the returned pixel buffers.
- [kVTRAWProcessingPropertyKey_MetalDeviceRegistryID](./kvtrawprocessingpropertykey_metaldeviceregistryid.md)
  This property requests that the Metal device corresponding to the specified registryID be used for any Metal related processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtrawprocessingpropertykey_metadataforsidecarfile)*