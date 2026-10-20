# VTRegisterSupplementalVideoDecoderIfAvailable(_:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Registers a video decoder for the specified codec type, if one exists on the current system.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 11.0+
- tvOS 26.2+
- visionOS 26.2+

## Declaration

```swift
func VTRegisterSupplementalVideoDecoderIfAvailable(_ codecType: CMVideoCodecType)
```

```c
extern void VTRegisterSupplementalVideoDecoderIfAvailable(CMVideoCodecType codecType);
```

#### Discussion

Call this function to find and register video decoders that aren’t registered by default.

## Parameters

- `codecType`: A codec type for which to register a decoder.

## See Also

### Codec Support
- [func VTIsHardwareDecodeSupported(CMVideoCodecType) -> Bool](./vtishardwaredecodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the current system supports hardware decode for the specified codec.
- [func VTRegisterProfessionalVideoWorkflowVideoEncoders()](./vtregisterprofessionalvideoworkflowvideoencoders%28%29.md)
  Loads encoders appropriate for the client’s professional video workflows.
- [func VTRegisterProfessionalVideoWorkflowVideoDecoders()](./vtregisterprofessionalvideoworkflowvideodecoders%28%29.md)
  Loads decoders appropriate for the client’s professional video workflows.
- [func VTCopySupportedPropertyDictionaryForEncoder(width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, encoderIDOut: UnsafeMutablePointer<CFString?>?, supportedPropertiesOut: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus](./vtcopysupportedpropertydictionaryforencoder%28width,height,codectype,encoderspecification,encoderidout,supportedpropertiesout%29.md)
  Builds a list of supported properties and encoder ID for an encoder.
- [func VTCopyVideoEncoderList(CFDictionary?, UnsafeMutablePointer<CFArray?>) -> OSStatus](./vtcopyvideoencoderlist%28_,_%29.md)
  Builds a list of available video encoders.
- [Video Encoder List Keys](./video-encoder-list-keys.md)
  Dictionary key constants to use to retrieve video encoder information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtregistersupplementalvideodecoderifavailable(_:))*