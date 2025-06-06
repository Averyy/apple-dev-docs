# VTCopySupportedPropertyDictionaryForEncoder(width:height:codecType:encoderSpecification:encoderIDOut:supportedPropertiesOut:)

**Framework**: Videotoolbox  
**Kind**: func

Builds a list of supported properties and encoder ID for an encoder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func VTCopySupportedPropertyDictionaryForEncoder(width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, encoderIDOut: UnsafeMutablePointer<CFString?>?, supportedPropertiesOut: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus
```

## Parameters

- `width`: 
- `height`: 
- `codecType`: 
- `encoderSpecification`: 
- `encoderIDOut`: 
- `supportedPropertiesOut`: 

## See Also

- [func VTIsHardwareDecodeSupported(CMVideoCodecType) -> Bool](vtishardwaredecodesupported(_:).md)
  Returns a Boolean value that indicates whether the current system supports hardware decode for the specified codec.
- [func VTRegisterProfessionalVideoWorkflowVideoEncoders()](vtregisterprofessionalvideoworkflowvideoencoders().md)
  Loads encoders appropriate for the client’s professional video workflows.
- [func VTRegisterProfessionalVideoWorkflowVideoDecoders()](vtregisterprofessionalvideoworkflowvideodecoders().md)
  Loads decoders appropriate for the client’s professional video workflows.
- [func VTRegisterSupplementalVideoDecoderIfAvailable(CMVideoCodecType)](vtregistersupplementalvideodecoderifavailable(_:).md)
  Registers a video decoder for the specified codec type, if one exists on the current system.
- [func VTCopyVideoEncoderList(CFDictionary?, UnsafeMutablePointer<CFArray?>) -> OSStatus](vtcopyvideoencoderlist(_:_:).md)
  Builds a list of available video encoders.
- [Video Encoder List Keys](video-encoder-list-keys.md)
  Dictionary key constants to use to retrieve video encoder information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcopysupportedpropertydictionaryforencoder(width:height:codectype:encoderspecification:encoderidout:supportedpropertiesout:))*