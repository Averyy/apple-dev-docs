# VTIsHardwareDecodeSupported(_:)

**Framework**: Videotoolbox  
**Kind**: func

Returns a Boolean value that indicates whether the current system supports hardware decode for the specified codec.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func VTIsHardwareDecodeSupported(_ codecType: CMVideoCodecType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the current system supports hardware decode; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `codecType`: The codec for which to test for hardware decode support.

## See Also

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
- [Video Encoder List Keys](video-encoder-list-keys.md)
  Dictionary key constants to use to retrieve video encoder information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtishardwaredecodesupported(_:))*