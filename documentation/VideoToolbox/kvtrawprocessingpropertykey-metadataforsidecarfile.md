# kVTRAWProcessingPropertyKey_MetadataForSidecarFile

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- macOS 26.0+

## Declaration

```swift
let kVTRAWProcessingPropertyKey_MetadataForSidecarFile: CFString!
```

#### Discussion

This property, if supported, returns the current processing metadata on the RAW Processor. The returned value can be used by the caller to create, or overwrite an existing sidecar file.

This property is not supported by all RAWProcessors. The metadata returned represents a fully-formed sidecar file, and should be compatible with the MediaExtension FormatReader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtrawprocessingpropertykey_metadataforsidecarfile)*