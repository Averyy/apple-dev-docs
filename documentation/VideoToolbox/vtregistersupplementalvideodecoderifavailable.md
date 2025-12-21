# VTRegisterSupplementalVideoDecoderIfAvailable(_:)

**Framework**: Video Toolbox  
**Kind**: func

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

#### Discussion

Call this function to find and register video decoders that aren’t registered by default.

## Parameters

- `codecType`: A codec type for which to register a decoder.

## See Also

- [func VTIsHardwareDecodeSupported(CMVideoCodecType) -> Bool](vtishardwaredecodesupported(_:).md)
  Returns a Boolean value that indicates whether the current system supports hardware decode for the specified codec.
- [func VTRegisterProfessionalVideoWorkflowVideoEncoders()](vtregisterprofessionalvideoworkflowvideoencoders().md)
  Loads encoders appropriate for the client’s professional video workflows.
- [func VTRegisterProfessionalVideoWorkflowVideoDecoders()](vtregisterprofessionalvideoworkflowvideodecoders().md)
  Loads decoders appropriate for the client’s professional video workflows.
- [func VTCopySupportedPropertyDictionaryForEncoder(width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, encoderIDOut: UnsafeMutablePointer<CFString?>?, supportedPropertiesOut: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus](vtcopysupportedpropertydictionaryforencoder(width:height:codectype:encoderspecification:encoderidout:supportedpropertiesout:).md)
  Builds a list of supported properties and encoder ID for an encoder.
- [func VTCopyVideoEncoderList(CFDictionary?, UnsafeMutablePointer<CFArray?>) -> OSStatus](vtcopyvideoencoderlist(_:_:).md)
  Builds a list of available video encoders.
- [Video Encoder List Keys](video-encoder-list-keys.md)
  Dictionary key constants to use to retrieve video encoder information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtregistersupplementalvideodecoderifavailable(_:))*