# kVTVideoEncoderList_DisplayName

**Framework**: Videotoolbox  
**Kind**: var

The encoder’s display name key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTVideoEncoderList_DisplayName: CFString
```

#### Discussion

The associated value is a doc://com.apple.documentation/documentation/corefoundation/cfstring-rfh with the encoder’s display name.

This value will be the same as the value of [`kVTVideoEncoderList_CodecName`](kvtvideoencoderlist_codecname.md) if there is only one encoder for that format; otherwise, it will be the same as the value of [`kVTVideoEncoderList_EncoderName`](kvtvideoencoderlist_encodername.md).

## See Also

- [let kVTVideoEncoderList_EncoderID: CFString](kvtvideoencoderlist_encoderid.md)
  A key that identifies the encoder ID.
- [let kVTVideoEncoderList_EncoderName: CFString](kvtvideoencoderlist_encodername.md)
  A key for the encoder’s name.
- [let kVTVideoEncoderList_CodecType: CFString](kvtvideoencoderlist_codectype.md)
  The encoder’s codec type key.
- [let kVTVideoEncoderList_CodecName: CFString](kvtvideoencoderlist_codecname.md)
  The encoder’s codec name key.
- [let kVTVideoEncoderList_GPURegistryID: CFString](kvtvideoencoderlist_gpuregistryid.md)
- [let kVTVideoEncoderList_InstanceLimit: CFString](kvtvideoencoderlist_instancelimit.md)
- [let kVTVideoEncoderList_IsHardwareAccelerated: CFString](kvtvideoencoderlist_ishardwareaccelerated.md)
- [let kVTVideoEncoderList_PerformanceRating: CFString](kvtvideoencoderlist_performancerating.md)
- [let kVTVideoEncoderList_QualityRating: CFString](kvtvideoencoderlist_qualityrating.md)
- [let kVTVideoEncoderList_SupportedSelectionProperties: CFString](kvtvideoencoderlist_supportedselectionproperties.md)
- [let kVTVideoEncoderList_SupportsFrameReordering: CFString](kvtvideoencoderlist_supportsframereordering.md)
- [let kVTVideoEncoderListOption_IncludeStandardDefinitionDVEncoders: CFString](kvtvideoencoderlistoption_includestandarddefinitiondvencoders.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderlist_displayname)*