# VTCopyVideoEncoderList(_:_:)

**Framework**: Video Toolbox  
**Kind**: func

Builds a list of available video encoders.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCopyVideoEncoderList(_ options: CFDictionary?, _ listOfVideoEncodersOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Discussion

The caller must release the returned list using [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).

## Parameters

- `options`: Not currently supported. Pass   for this parameter.
- `listOfVideoEncodersOut`: Pointer to a   of available video encoders.

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
- [Video Encoder List Keys](video-encoder-list-keys.md)
  Dictionary key constants to use to retrieve video encoder information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcopyvideoencoderlist(_:_:))*