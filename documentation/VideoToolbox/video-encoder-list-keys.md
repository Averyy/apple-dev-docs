# Video Encoder List Keys

**Framework**: Video Toolbox

Dictionary key constants to use to retrieve video encoder information.

#### Overview

Use these keys to pass to the [`VTCopyVideoEncoderList(_:_:)`](vtcopyvideoencoderlist(_:_:).md) function.

## Topics

### Encoder Keys
- [let kVTVideoEncoderList_EncoderID: CFString](kvtvideoencoderlist_encoderid.md)
  A key that identifies the encoder ID.
- [let kVTVideoEncoderList_EncoderName: CFString](kvtvideoencoderlist_encodername.md)
  A key for the encoder’s name.
- [let kVTVideoEncoderList_DisplayName: CFString](kvtvideoencoderlist_displayname.md)
  The encoder’s display name key.
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

## See Also

- [func VTIsHardwareDecodeSupported(CMVideoCodecType) -> Bool](vtishardwaredecodesupported(_:).md)
  Returns a Boolean value that indicates whether the current system supports hardware decode for the specified codec.
- [func VTRegisterProfessionalVideoWorkflowVideoEncoders()](vtregisterprofessionalvideoworkflowvideoencoders().md)
  Loads encoders appropriate for the client’s professional video workflows.
- [func VTRegisterProfessionalVideoWorkflowVideoDecoders()](vtregisterprofessionalvideoworkflowvideodecoders().md)
  Loads decoders appropriate for the client’s professional video workflows.
- [func VTRegisterSupplementalVideoDecoderIfAvailable(CMVideoCodecType)](vtregistersupplementalvideodecoderifavailable(_:).md)
  Registers a video decoder for the specified codec type, if one exists on the current system.
- [func VTCopySupportedPropertyDictionaryForEncoder(width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, encoderIDOut: UnsafeMutablePointer<CFString?>?, supportedPropertiesOut: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus](vtcopysupportedpropertydictionaryforencoder(width:height:codectype:encoderspecification:encoderidout:supportedpropertiesout:).md)
  Builds a list of supported properties and encoder ID for an encoder.
- [func VTCopyVideoEncoderList(CFDictionary?, UnsafeMutablePointer<CFArray?>) -> OSStatus](vtcopyvideoencoderlist(_:_:).md)
  Builds a list of available video encoders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/video-encoder-list-keys)*